# 🎯 LoRA & PEFT: The 80-20 Guide

## 📚 What is Perplexity?

### Simple Definition
**Perplexity** measures how "surprised" a language model is by the text it sees. Lower perplexity = better model performance.

### Intuition
- **Low perplexity (e.g., 10-50)**: Model is confident, predicts well
- **High perplexity (e.g., 100+)**: Model is confused, struggles to predict

### Formula
```
Perplexity = 2^(cross_entropy_loss)
```

**Lower is better!**

### Example
```
Text: "The cat sat on the mat"
Good model: Perplexity = 15 (low, confident)
Bad model: Perplexity = 200 (high, confused)
```

### How to Calculate
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained("model-name")
tokenizer = AutoTokenizer.from_pretrained("model-name")

text = "Your test text here"
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    perplexity = torch.exp(loss).item()

print(f"Perplexity: {perplexity:.2f}")
```

---

## 🎯 The 80-20 Rule for LoRA/PEFT

### The 20% That Gives 80% of Value

**Focus on these 4 concepts:**
1. **What is PEFT?** (Parameter-Efficient Fine-Tuning)
2. **LoRA vs QLoRA** (the only difference: compressed base)
3. **Key configuration** (r, alpha, target_modules)
4. **How to verify it works** (metrics and testing)

---

## 1️⃣ What is PEFT?

### The Problem
- Fine-tuning large models requires updating billions of parameters
- Very expensive (GPU memory, time, cost)
- Full fine-tuning: 14 GB+ VRAM for 7B model

### The Solution: PEFT
- **Freeze** the base model (don't train original weights)
- **Add small adapters** (train only these tiny modules)
- **Result**: Train 0.1-5% of parameters instead of 100%

### Types of PEFT
1. **LoRA** (Low-Rank Adaptation) - Most popular
2. **QLoRA** (Quantized LoRA) - LoRA with 4-bit base model
3. **Adapters** - Alternative approach
4. **Prompt Tuning** - Different strategy

**80% of cases use LoRA/QLoRA** ✅

---

## 2️⃣ LoRA vs QLoRA

### The Only Difference

| Aspect | LoRA | QLoRA |
|--------|------|-------|
| Base Model | Uncompressed (16-bit) | Compressed (4-bit) |
| Memory | ~14 GB (7B model) | ~4 GB (7B model) |
| Adapters | Same (trainable) | Same (trainable) |
| Quality | Baseline | 98-99% of LoRA |
| Hardware | High-end GPU needed | Consumer GPU works |

### Decision Tree
```
Start here: QLoRA (covers 80% of cases)
    ↓
Need maximum quality?
    ↓
Use LoRA (if you have high-end GPU)
```

### Code Difference (One Line!)

```python
# LoRA
model = AutoModelForCausalLM.from_pretrained("model", torch_dtype=torch.float16)

# QLoRA (only difference)
bnb_config = BitsAndBytesConfig(load_in_4bit=True)  # ← This line!
model = AutoModelForCausalLM.from_pretrained("model", quantization_config=bnb_config)
```

---

## 3️⃣ Key Configuration (The Essentials)

### The 4 Critical Parameters

#### 1. Rank (r)
- **What**: Adapter capacity (how expressive)
- **Values**: 4-64 (most use 16)
- **Rule**: Higher = more capacity, more memory
- **80% case**: Use r=16

#### 2. Alpha (lora_alpha)
- **What**: Scaling factor for adapter influence
- **Values**: 8-128 (most use 32)
- **Rule**: alpha/r = 1-4 is good
- **80% case**: Use alpha=32 with r=16

#### 3. Target Modules
- **What**: Which layers get adapters
- **Values**: Layer names (e.g., "q_proj", "v_proj")
- **Rule**: Start with attention projections
- **80% case**: `["q_proj", "k_proj", "v_proj", "o_proj"]`

#### 4. Dropout
- **What**: Regularization (prevents overfitting)
- **Values**: 0.0-0.2 (most use 0.05)
- **Rule**: Higher = more regularization
- **80% case**: Use 0.05

### Recommended Starting Config (80% of Cases)

```python
from peft import LoraConfig, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,                    # Rank: balanced capacity
    lora_alpha=32,           # Scaling: 2x influence
    lora_dropout=0.05,       # Regularization: 5%
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],  # Attention layers
    bias="none"              # Don't train biases
)
```

**This works for 80% of use cases!**

---

## 4️⃣ How to Verify It Works

### Quick Checklist

1. ✅ **Trainable Parameters**: Should be 0.1-5% of total (not 0% or 100%)
2. ✅ **Training Loss**: Should decrease over time
3. ✅ **Adapter Weights**: Should change after training
4. ✅ **Task Metrics**: Should improve on your evaluation
5. ✅ **Perplexity**: Should decrease (lower is better)

### Key Metrics

| Metric | What It Means | Good Value |
|--------|---------------|------------|
| **Training Loss** | How well model fits data | Decreasing |
| **Perplexity** | Model confidence | Lower is better (10-50) |
| **Accuracy** | Task performance | > 0.85 |
| **ROUGE** | Generation quality | > 0.40 |

---

## 🚀 Quick Start

### Step 1: Install
```bash
pip install transformers peft trl datasets accelerate bitsandbytes
```

### Step 2: Load Model
```python
from transformers import AutoModelForCausalLM
from peft import LoraConfig, get_peft_model

model = AutoModelForCausalLM.from_pretrained("model-name")
```

### Step 3: Configure LoRA
```python
lora_config = LoraConfig(r=16, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(model, lora_config)
```

### Step 4: Train
```python
# Use SFTTrainer (see examples.py)
trainer.train()
```

### Step 5: Evaluate
```python
# Check perplexity (see examples.py)
perplexity = calculate_perplexity(model, test_data)
```

---

## 📊 Memory Comparison

### 7B Model Example

| Method | Base Model | Adapters | Total VRAM |
|--------|------------|----------|------------|
| Full Fine-tune | 14 GB | - | 14+ GB |
| LoRA | 14 GB | 10 MB | ~14 GB |
| QLoRA | 4 GB | 10 MB | ~4 GB |

**QLoRA saves 10 GB!** (75% reduction)

---

## 🎯 Decision Guide

### Use QLoRA If:
- ✅ Consumer GPU (12-16 GB)
- ✅ Cost-sensitive
- ✅ Most use cases (80%)

### Use LoRA If:
- ✅ High-end GPU (24+ GB)
- ✅ Need maximum quality
- ✅ Want to merge adapters

### Use Full Fine-tune If:
- ✅ Very large domain shift
- ✅ Unlimited resources
- ✅ Need absolute best quality

**80% of cases: Start with QLoRA!**

---

## 📖 Next Steps

1. **Read examples.py** - See practical code
2. **Complete exercises.py** - Practice hands-on
3. **Check perplexity_explained.md** - Deep dive on perplexity
4. **Experiment** - Try different configurations

---

## 💡 Key Takeaways

1. **PEFT** = Freeze base, train small adapters (99% parameter reduction)
2. **LoRA vs QLoRA** = Only difference is base model compression
3. **Configuration** = r=16, alpha=32, attention layers, dropout=0.05 (covers 80%)
4. **Verification** = Check trainable params, loss, perplexity, task metrics
5. **Start with QLoRA** = Works for most cases, less memory

**Remember**: The best configuration is the one that works for YOUR data and YOUR task. Start simple, measure results, iterate!

