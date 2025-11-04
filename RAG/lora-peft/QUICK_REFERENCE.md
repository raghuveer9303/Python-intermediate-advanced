# ⚡ LoRA/PEFT Quick Reference

## 🎯 Perplexity in 30 Seconds

**Perplexity = How surprised the model is by text**

- **Low perplexity (10-30)**: Model is confident ✅
- **High perplexity (100+)**: Model is confused ❌
- **Formula**: `perplexity = exp(cross_entropy_loss)`
- **Lower is better!**

```python
# Calculate perplexity
loss = model_outputs.loss
perplexity = torch.exp(loss).item()
```

---

## 🚀 LoRA vs QLoRA (One Line Difference)

```python
# LoRA: Uncompressed base (14 GB for 7B model)
model = AutoModelForCausalLM.from_pretrained("model", torch_dtype=torch.float16)

# QLoRA: Compressed base (4 GB for 7B model) ← SAVE 10 GB!
bnb_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained("model", quantization_config=bnb_config)
```

**Use QLoRA for 80% of cases!**

---

## ⚙️ Recommended Config (80% of Cases)

```python
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=16,                    # Rank: balanced
    lora_alpha=32,           # Scaling: 2x influence
    lora_dropout=0.05,       # Regularization: 5%
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],  # Attention
    bias="none"
)
```

**This works for most tasks!**

---

## ✅ Quick Verification Checklist

1. ✅ Trainable params: 0.1-5% of total (not 0% or 100%)
2. ✅ Training loss: Decreasing over time
3. ✅ Perplexity: Lower after training
4. ✅ Adapters found: Check with `verify_lora_working()`

---

## 📊 Memory Comparison

| Method | VRAM (7B model) | Use When |
|--------|-----------------|----------|
| Full Fine-tune | 14+ GB | Maximum quality needed |
| LoRA | 14 GB | High-end GPU available |
| QLoRA | 4 GB | **Most cases (80%)** ✅ |

---

## 🔍 Finding Target Modules

```python
# Print all Linear layers
for name, module in model.named_modules():
    if isinstance(module, torch.nn.Linear):
        print(name)

# Common patterns:
# LLaMA/Mistral: ["q_proj", "k_proj", "v_proj", "o_proj"]
# GPT-2: ["c_attn", "c_proj"]
# OPT: ["q_proj", "k_proj", "v_proj", "out_proj"]
```

---

## 📈 Key Metrics

| Metric | Good Value | What It Means |
|--------|------------|---------------|
| Perplexity | 10-50 | Model confidence |
| Training Loss | Decreasing | Model learning |
| Trainable % | 0.1-5% | LoRA working |
| Accuracy | > 0.85 | Task performance |

---

## 🎯 Decision Tree

```
Start: Use QLoRA
    ↓
Need maximum quality?
    ↓ Yes
Have high-end GPU (24+ GB)?
    ↓ Yes
Use LoRA
    ↓ No
Stick with QLoRA (still good!)
```

---

## 💡 Key Takeaways

1. **Perplexity**: Lower = better (10-30 is excellent)
2. **QLoRA**: Use for 80% of cases (saves memory)
3. **Config**: r=16, alpha=32, attention layers (covers most cases)
4. **Verify**: Check trainable params, loss, perplexity
5. **Start simple**: Use recommended config, iterate based on results

---

**Remember**: The best configuration is what works for YOUR data and YOUR task!

