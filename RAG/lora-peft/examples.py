"""
LoRA & PEFT Examples - The 80/20 Essentials
Focus on what works 80% of the time
"""

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig
)
from peft import LoraConfig, TaskType, get_peft_model
from datasets import load_dataset
from trl import SFTTrainer, SFTConfig


# ============================================================================
# 1. BASIC LORA SETUP (80% of cases)
# ============================================================================

def setup_lora_basic(model_name="meta-llama/Llama-2-7b-hf"):
    """
    Basic LoRA setup - recommended starting point
    Works for 80% of use cases
    """
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token  # Important!
    
    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    
    # LoRA configuration (recommended for 80% of cases)
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,                    # Rank: balanced capacity
        lora_alpha=32,           # Scaling: 2x influence (alpha/r = 2.0)
        lora_dropout=0.05,       # Regularization: 5%
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],  # Attention layers
        bias="none"              # Don't train biases
    )
    
    # Apply LoRA
    model = get_peft_model(model, lora_config)
    
    # Check what's trainable
    model.print_trainable_parameters()
    # Output: trainable params: ~8M || all params: 7B || trainable%: 0.12%
    
    return model, tokenizer


# ============================================================================
# 2. QLORA SETUP (Memory-efficient, 80% of cases)
# ============================================================================

def setup_qlora_basic(model_name="meta-llama/Llama-2-7b-hf"):
    """
    QLoRA setup - same as LoRA but with 4-bit base model
    Saves 75% memory, works on consumer GPUs
    """
    
    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    # 4-bit quantization config (ONLY DIFFERENCE from LoRA)
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,                    # Compress base to 4-bit
        bnb_4bit_use_double_quant=True,       # Extra quantization
        bnb_4bit_quant_type="nf4",            # Quantization type
        bnb_4bit_compute_dtype=torch.bfloat16 # Compute precision
    )
    
    # Load model with quantization
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=bnb_config,  # ← This makes it QLoRA
        device_map="auto"
    )
    
    # Same LoRA config as before
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        bias="none"
    )
    
    # Apply LoRA (adapters still trainable in full precision)
    model = get_peft_model(model, lora_config)
    
    model.print_trainable_parameters()
    
    return model, tokenizer


# ============================================================================
# 3. FINDING TARGET MODULES (Important for any model)
# ============================================================================

def find_target_modules(model):
    """
    Find which modules to target for LoRA
    Essential for models you haven't used before
    """
    
    import torch.nn as nn
    
    # Find all Linear layers
    linear_layers = []
    for name, module in model.named_modules():
        if isinstance(module, nn.Linear):
            linear_layers.append(name)
    
    # Categorize by type
    attention_layers = [name for name in linear_layers 
                       if any(x in name for x in ["q_proj", "k_proj", "v_proj", "o_proj", "c_attn", "c_proj"])]
    
    mlp_layers = [name for name in linear_layers 
                  if any(x in name for x in ["gate_proj", "up_proj", "down_proj", "fc1", "fc2"])]
    
    # Extract unique patterns (remove layer indices)
    def get_pattern(name):
        parts = name.split(".")
        for part in reversed(parts):
            if "proj" in part or "attn" in part:
                return part
        return name.split(".")[-1]
    
    attention_patterns = list(set([get_pattern(name) for name in attention_layers]))
    
    print(f"Found {len(linear_layers)} Linear layers")
    print(f"Attention layers: {len(attention_layers)}")
    print(f"Recommended target modules: {attention_patterns[:4]}")
    
    return attention_patterns[:4]  # Return first 4 (usually q, k, v, o)


# ============================================================================
# 4. TRAINING EXAMPLE (Complete workflow)
# ============================================================================

def train_lora_example(model, tokenizer):
    """
    Complete training example with LoRA
    """
    
    # Load dataset (example: Alpaca)
    dataset = load_dataset("tatsu-lab/alpaca", split="train[:1%]")
    
    # Format data
    def format_text(example):
        return {
            "text": f"Instruction: {example['instruction']}\n"
                   f"Input: {example['input']}\n"
                   f"Response: {example['output']}"
        }
    
    dataset = dataset.map(format_text)
    
    # Training configuration
    training_args = SFTConfig(
        output_dir="./lora_output",
        per_device_train_batch_size=2,
        gradient_accumulation_steps=8,  # Effective batch = 16
        num_train_epochs=1,
        learning_rate=2e-4,
        logging_steps=10,
        save_steps=200,
        bf16=True,  # Use bfloat16 (A100/H100) or fp16=True for consumer GPUs
        max_seq_length=1024,
        gradient_checkpointing=True,  # Save memory
    )
    
    # Create trainer
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        args=training_args,
        dataset_text_field="text",
    )
    
    # Train
    print("Starting training...")
    trainer.train()
    print("Training complete!")
    
    # Save adapters (only small files, not full model!)
    model.save_pretrained("./lora_output")
    tokenizer.save_pretrained("./lora_output")
    
    return model


# ============================================================================
# 5. CALCULATE PERPLEXITY (Important metric)
# ============================================================================

def calculate_perplexity(model, tokenizer, text):
    """
    Calculate perplexity for a single text
    Lower perplexity = better model
    """
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    inputs = {k: v.to(model.device) for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
        perplexity = torch.exp(loss).item()
    
    return perplexity


def calculate_perplexity_batch(model, tokenizer, texts):
    """
    Calculate average perplexity for multiple texts
    """
    
    perplexities = []
    for text in texts:
        try:
            ppl = calculate_perplexity(model, tokenizer, text)
            perplexities.append(ppl)
        except:
            continue
    
    if perplexities:
        avg_perplexity = sum(perplexities) / len(perplexities)
        return avg_perplexity, perplexities
    else:
        return None, []


# ============================================================================
# 6. VERIFY LORA IS WORKING (Essential checks)
# ============================================================================

def verify_lora_working(model):
    """
    Verify that LoRA adapters are actually working
    Essential checks before training
    """
    
    checks = {
        "trainable_params": 0,
        "total_params": 0,
        "trainable_percentage": 0.0,
        "adapters_found": False,
        "weights_changing": False
    }
    
    # Check trainable parameters
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    total = sum(p.numel() for p in model.parameters())
    
    checks["trainable_params"] = trainable
    checks["total_params"] = total
    checks["trainable_percentage"] = (trainable / total) * 100
    
    # Check if adapters exist
    adapter_count = 0
    for name, module in model.named_modules():
        if "lora" in name.lower():
            adapter_count += 1
    
    checks["adapters_found"] = adapter_count > 0
    
    # Print results
    print("\n=== LoRA Verification ===")
    print(f"Trainable params: {trainable:,} / {total:,} ({checks['trainable_percentage']:.2f}%)")
    print(f"Adapters found: {adapter_count}")
    
    # Validation
    if checks["trainable_percentage"] < 0.01:
        print("⚠️  Warning: Very few trainable parameters (< 0.01%)")
        print("   Check target_modules configuration!")
    elif checks["trainable_percentage"] > 10:
        print("⚠️  Warning: Too many trainable parameters (> 10%)")
        print("   May not be using LoRA correctly!")
    else:
        print("✅ Trainable parameters look good!")
    
    if adapter_count == 0:
        print("❌ No adapters found! LoRA not applied correctly.")
    else:
        print(f"✅ {adapter_count} adapters found!")
    
    return checks


# ============================================================================
# 7. BEFORE/AFTER COMPARISON (Test learning)
# ============================================================================

def compare_before_after(base_model, fine_tuned_model, tokenizer, test_texts):
    """
    Compare base model vs fine-tuned model
    """
    
    print("\n=== Before/After Comparison ===")
    
    # Base model perplexity
    base_ppl, _ = calculate_perplexity_batch(base_model, tokenizer, test_texts)
    print(f"Base model perplexity: {base_ppl:.2f}" if base_ppl else "N/A")
    
    # Fine-tuned model perplexity
    tuned_ppl, _ = calculate_perplexity_batch(fine_tuned_model, tokenizer, test_texts)
    print(f"Fine-tuned model perplexity: {tuned_ppl:.2f}" if tuned_ppl else "N/A")
    
    # Improvement
    if base_ppl and tuned_ppl:
        improvement = ((base_ppl - tuned_ppl) / base_ppl) * 100
        print(f"Improvement: {improvement:.2f}%")
        
        if improvement > 0:
            print("✅ Model improved after fine-tuning!")
        else:
            print("⚠️  Model didn't improve (check configuration)")
    
    # Generate examples
    print("\n=== Generation Examples ===")
    for text in test_texts[:2]:
        prompt = text[:100]  # First 100 chars
        
        # Base model
        base_inputs = tokenizer(prompt, return_tensors="pt")
        base_outputs = base_model.generate(**base_inputs, max_new_tokens=50)
        base_result = tokenizer.decode(base_outputs[0], skip_special_tokens=True)
        
        # Fine-tuned model
        tuned_inputs = tokenizer(prompt, return_tensors="pt")
        tuned_outputs = fine_tuned_model.generate(**tuned_inputs, max_new_tokens=50)
        tuned_result = tokenizer.decode(tuned_outputs[0], skip_special_tokens=True)
        
        print(f"\nPrompt: {prompt}")
        print(f"Base: {base_result[:150]}...")
        print(f"Tuned: {tuned_result[:150]}...")


# ============================================================================
# 8. COMPLETE WORKFLOW EXAMPLE
# ============================================================================

def complete_workflow_example():
    """
    Complete end-to-end example
    """
    
    print("=" * 60)
    print("COMPLETE LORA WORKFLOW EXAMPLE")
    print("=" * 60)
    
    model_name = "meta-llama/Llama-2-7b-hf"  # Replace with your model
    
    # Step 1: Setup (choose LoRA or QLoRA)
    print("\n1. Setting up model...")
    try:
        # Try QLoRA first (works on more hardware)
        model, tokenizer = setup_qlora_basic(model_name)
        print("✅ Using QLoRA (4-bit base)")
    except:
        # Fallback to LoRA if QLoRA fails
        model, tokenizer = setup_lora_basic(model_name)
        print("✅ Using LoRA (16-bit base)")
    
    # Step 2: Verify LoRA is working
    print("\n2. Verifying LoRA setup...")
    checks = verify_lora_working(model)
    
    if not checks["adapters_found"]:
        print("❌ LoRA not working! Check configuration.")
        return
    
    # Step 3: Find target modules (if needed)
    print("\n3. Checking target modules...")
    target_modules = find_target_modules(model)
    print(f"✅ Target modules: {target_modules}")
    
    # Step 4: Calculate initial perplexity
    print("\n4. Calculating initial perplexity...")
    test_texts = [
        "The quick brown fox jumps over the lazy dog",
        "Python is a programming language",
        "Machine learning is a subset of artificial intelligence"
    ]
    
    initial_ppl, _ = calculate_perplexity_batch(model, tokenizer, test_texts)
    print(f"Initial perplexity: {initial_ppl:.2f}" if initial_ppl else "N/A")
    
    # Step 5: Train (commented out - uncomment to actually train)
    print("\n5. Training...")
    print("(Training commented out - uncomment train_lora_example() to train)")
    # model = train_lora_example(model, tokenizer)
    
    # Step 6: Calculate final perplexity
    print("\n6. Calculating final perplexity...")
    final_ppl, _ = calculate_perplexity_batch(model, tokenizer, test_texts)
    print(f"Final perplexity: {final_ppl:.2f}" if final_ppl else "N/A")
    
    if initial_ppl and final_ppl:
        improvement = ((initial_ppl - final_ppl) / initial_ppl) * 100
        print(f"Improvement: {improvement:.2f}%")
    
    print("\n" + "=" * 60)
    print("Workflow complete!")
    print("=" * 60)


# ============================================================================
# MAIN: Run examples
# ============================================================================

if __name__ == "__main__":
    print("LoRA & PEFT Examples - The 80/20 Essentials")
    print("=" * 60)
    
    # Run complete workflow
    complete_workflow_example()
    
    # Uncomment to run individual examples:
    # model, tokenizer = setup_qlora_basic()
    # verify_lora_working(model)
    # perplexity = calculate_perplexity(model, tokenizer, "Test text")

