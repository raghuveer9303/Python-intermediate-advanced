"""
LoRA & PEFT Exercises - Practice the 80/20 Essentials
Complete these exercises to master LoRA/QLoRA
"""

from examples import (
    setup_lora_basic,
    setup_qlora_basic,
    find_target_modules,
    calculate_perplexity,
    calculate_perplexity_batch,
    verify_lora_working,
    train_lora_example
)


# ============================================================================
# EXERCISE 1: Basic LoRA Setup
# ============================================================================

def exercise_1():
    """
    Setup basic LoRA configuration
    
    Instructions:
    1. Use setup_lora_basic() to create a LoRA model
    2. Print the trainable parameters
    3. Verify that only ~0.1-5% of parameters are trainable
    4. Check that adapters are found
    """
    # TODO: Implement your solution
    # model, tokenizer = setup_lora_basic()
    # checks = verify_lora_working(model)
    # print(f"Trainable: {checks['trainable_percentage']:.2f}%")
    
    pass


# ============================================================================
# EXERCISE 2: QLoRA Setup
# ============================================================================

def exercise_2():
    """
    Setup QLoRA configuration (memory-efficient)
    
    Instructions:
    1. Use setup_qlora_basic() to create a QLoRA model
    2. Compare memory usage with LoRA (should be ~75% less)
    3. Verify adapters work the same way
    4. Check trainable parameters (should be similar to LoRA)
    """
    # TODO: Implement your solution
    # model, tokenizer = setup_qlora_basic()
    # checks = verify_lora_working(model)
    # print("QLoRA setup complete!")
    
    pass


# ============================================================================
# EXERCISE 3: Finding Target Modules
# ============================================================================

def exercise_3():
    """
    Find target modules for a new model
    
    Instructions:
    1. Load a model you haven't used before
    2. Use find_target_modules() to discover layer names
    3. Identify attention and MLP layers
    4. Create a LoRA config with appropriate target modules
    """
    from transformers import AutoModelForCausalLM
    
    # TODO: Try a different model
    # model_name = "gpt2"  # or any other model
    # model = AutoModelForCausalLM.from_pretrained(model_name)
    # targets = find_target_modules(model)
    # print(f"Target modules: {targets}")
    
    pass


# ============================================================================
# EXERCISE 4: Calculate Perplexity
# ============================================================================

def exercise_4():
    """
    Calculate perplexity for model evaluation
    
    Instructions:
    1. Load a model (base or fine-tuned)
    2. Create test texts relevant to your domain
    3. Calculate perplexity for each text
    4. Calculate average perplexity
    5. Interpret results (lower = better, 10-50 is good)
    """
    # TODO: Implement your solution
    # test_texts = [
    #     "Your domain-specific text 1",
    #     "Your domain-specific text 2",
    #     "Your domain-specific text 3"
    # ]
    # 
    # model, tokenizer = setup_lora_basic()
    # avg_ppl, individual_ppl = calculate_perplexity_batch(model, tokenizer, test_texts)
    # print(f"Average perplexity: {avg_ppl:.2f}")
    # print(f"Individual perplexities: {individual_ppl}")
    
    pass


# ============================================================================
# EXERCISE 5: Compare LoRA Configurations
# ============================================================================

def exercise_5():
    """
    Compare different LoRA configurations
    
    Instructions:
    1. Create 3 different LoRA configs:
       - Minimal: r=8, only q_proj and v_proj
       - Standard: r=16, all attention layers
       - Comprehensive: r=32, attention + MLP layers
    2. Compare trainable parameters for each
    3. Compare training time (if you train)
    4. Compare final perplexity
    5. Determine which works best for your use case
    """
    from peft import LoraConfig, TaskType, get_peft_model
    from transformers import AutoModelForCausalLM
    
    # TODO: Implement your solution
    # base_model = AutoModelForCausalLM.from_pretrained("model-name")
    # 
    # configs = [
    #     LoraConfig(r=8, target_modules=["q_proj", "v_proj"]),
    #     LoraConfig(r=16, target_modules=["q_proj", "k_proj", "v_proj", "o_proj"]),
    #     LoraConfig(r=32, target_modules=["q_proj", "k_proj", "v_proj", "o_proj", 
    #                                     "gate_proj", "up_proj", "down_proj"])
    # ]
    # 
    # for i, config in enumerate(configs):
    #     model = get_peft_model(base_model, config)
    #     trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    #     print(f"Config {i+1}: {trainable:,} trainable parameters")
    
    pass


# ============================================================================
# EXERCISE 6: Verify Learning Happened
# ============================================================================

def exercise_6():
    """
    Verify that your model actually learned something
    
    Instructions:
    1. Calculate perplexity before training
    2. Train the model (or load a trained model)
    3. Calculate perplexity after training
    4. Compare before/after
    5. Check that perplexity decreased (improved)
    6. If perplexity didn't decrease, troubleshoot:
       - Check learning rate
       - Check target modules
       - Check data format
    """
    # TODO: Implement your solution
    # model, tokenizer = setup_lora_basic()
    # 
    # # Before training
    # test_texts = ["Your test text"]
    # before_ppl, _ = calculate_perplexity_batch(model, tokenizer, test_texts)
    # print(f"Before training: {before_ppl:.2f}")
    # 
    # # Train (or load trained model)
    # # model = train_lora_example(model, tokenizer)
    # 
    # # After training
    # after_ppl, _ = calculate_perplexity_batch(model, tokenizer, test_texts)
    # print(f"After training: {after_ppl:.2f}")
    # 
    # improvement = ((before_ppl - after_ppl) / before_ppl) * 100
    # print(f"Improvement: {improvement:.2f}%")
    
    pass


# ============================================================================
# EXERCISE 7: Troubleshooting Common Issues
# ============================================================================

def exercise_7():
    """
    Practice troubleshooting common LoRA issues
    
    Instructions:
    1. Create a LoRA config with wrong target modules
    2. Verify it fails (no adapters found)
    3. Fix the configuration
    4. Verify it works
    5. Document what went wrong and how you fixed it
    """
    from peft import LoraConfig, TaskType, get_peft_model
    from transformers import AutoModelForCausalLM
    
    # TODO: Implement your solution
    # Wrong target modules
    # wrong_config = LoraConfig(
    #     task_type=TaskType.CAUSAL_LM,
    #     r=16,
    #     target_modules=["wrong_name_1", "wrong_name_2"]  # Wrong!
    # )
    # 
    # model = AutoModelForCausalLM.from_pretrained("model-name")
    # model = get_peft_model(model, wrong_config)
    # checks = verify_lora_working(model)
    # # Should show warning about no adapters
    # 
    # # Fix with correct target modules
    # correct_config = LoraConfig(
    #     task_type=TaskType.CAUSAL_LM,
    #     r=16,
    #     target_modules=["q_proj", "v_proj"]  # Correct!
    # )
    # model = get_peft_model(model, correct_config)
    # checks = verify_lora_working(model)
    # # Should show adapters found
    
    pass


# ============================================================================
# EXERCISE 8: Optimize Configuration
# ============================================================================

def exercise_8():
    """
    Optimize LoRA configuration for your specific task
    
    Instructions:
    1. Start with recommended config (r=16, alpha=32, attention layers)
    2. Train and evaluate (check perplexity)
    3. If results are poor:
       - Try increasing r (16 → 32)
       - Try adding MLP layers
       - Try adjusting alpha (32 → 64)
    4. Document what works best for your task
    5. Compare training time vs quality trade-off
    """
    # TODO: Implement your solution
    # Start with baseline
    # baseline_config = LoraConfig(r=16, lora_alpha=32, ...)
    # 
    # # Test baseline
    # baseline_ppl = evaluate_config(baseline_config)
    # 
    # # Try improvements
    # improved_config = LoraConfig(r=32, lora_alpha=64, ...)
    # improved_ppl = evaluate_config(improved_config)
    # 
    # # Compare
    # print(f"Baseline: {baseline_ppl:.2f}")
    # print(f"Improved: {improved_ppl:.2f}")
    
    pass


# ============================================================================
# RUN ALL EXERCISES
# ============================================================================

def run_all_exercises():
    """Run all exercises"""
    print("=" * 60)
    print("LORA & PEFT EXERCISES")
    print("=" * 60)
    
    exercises = [
        ("Exercise 1: Basic LoRA Setup", exercise_1),
        ("Exercise 2: QLoRA Setup", exercise_2),
        ("Exercise 3: Finding Target Modules", exercise_3),
        ("Exercise 4: Calculate Perplexity", exercise_4),
        ("Exercise 5: Compare Configurations", exercise_5),
        ("Exercise 6: Verify Learning", exercise_6),
        ("Exercise 7: Troubleshooting", exercise_7),
        ("Exercise 8: Optimize Configuration", exercise_8),
    ]
    
    for name, func in exercises:
        print(f"\n{name}")
        print("-" * 60)
        try:
            func()
        except Exception as e:
            print(f"Error: {e}")
        print()
    
    print("=" * 60)
    print("Complete the exercises above!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_exercises()

