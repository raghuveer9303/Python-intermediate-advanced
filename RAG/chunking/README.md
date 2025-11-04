# 📚 Chunking for RAG: The 80-20 Guide

## 🎯 The Core Principle (80-20 Rule)

**20% of chunking concepts give you 80% of the results.**

Focus on these essentials:
1. **Fixed-size chunking with overlap** (covers 80% of use cases)
2. **Understanding when to use semantic vs. fixed chunking**
3. **Choosing the right chunk size for your use case**
4. **Overlap strategy** (prevents information loss)

---

## 🤔 What is Chunking and Why Does It Matter?

### The Problem
- **LLM Context Limits**: Models have token limits (4K-128K tokens)
- **Embedding Limits**: Most embedding models handle 512-8192 tokens
- **Large Documents**: Can't fit entire documents in one chunk
- **Retrieval Quality**: Smaller, focused chunks improve retrieval precision

### The Solution
Split documents into smaller, manageable pieces (chunks) that:
- Fit within model limits
- Preserve context and meaning
- Enable efficient retrieval
- Maintain semantic coherence

---

## 🎯 The 4 Essential Concepts (The 20%)

### 1. Fixed-Size Chunking (80% of Cases)
**What**: Split text by character/token count  
**When**: Most documents, uniform structure  
**Why**: Simple, fast, works for most scenarios

```python
# Simple fixed-size chunking
chunk_size = 512
overlap = 50  # 10% overlap
```

### 2. Overlap Strategy (Critical!)
**What**: Overlapping chunks to preserve context  
**When**: Always (prevents boundary information loss)  
**Why**: Context at chunk boundaries is critical for understanding

**Rule of Thumb**: Overlap = 10-20% of chunk size

### 3. Semantic Chunking (20% Upgrade)
**What**: Split at natural boundaries (sentences, paragraphs)  
**When**: When preserving meaning is critical  
**Why**: Better than fixed-size because it respects structure

### 4. Chunk Size Selection (Practical)
- **512 tokens**: Small, precise, good for specific queries
- **1024 tokens**: Balanced (most common default)
- **2048 tokens**: Larger context, fewer chunks

---

## 📊 Quick Decision Tree

```
Start Here:
├─ Fixed-size (512-1024 chars) + 10-20% overlap
│  └─ Works for 80% of cases ✅
│
├─ Need better boundaries?
│  └─ Use sentence-aware chunking
│
└─ Complex documents?
   └─ Use semantic chunking (paragraphs, sections)
```

---

## 🔥 Common Patterns (The Essentials)

### Pattern 1: Fixed-Size with Overlap
```python
chunk_size = 512
overlap = 50  # ~10% overlap
```
**Use when**: Most documents, general purpose

### Pattern 2: Sentence-Aware
```python
chunk_size = 512
overlap_sentences = 2
```
**Use when**: Need to preserve sentence boundaries

### Pattern 3: Paragraph-Based
```python
max_chunk_size = 1024
min_chunk_size = 256
```
**Use when**: Documents have clear paragraph structure

---

## ⚠️ Common Pitfalls (Avoid These!)

### ❌ No Overlap
```python
# BAD: Information loss at boundaries
chunks = [text[i:i+512] for i in range(0, len(text), 512)]
```

### ✅ With Overlap
```python
# GOOD: Preserves context
chunks = chunk_with_overlap(text, size=512, overlap=50)
```

### ❌ Too Large Chunks
- Poor retrieval precision
- Harder to embed
- May exceed model limits

### ❌ Too Small Chunks
- Fragments meaning
- Too many chunks to process
- Loses context

### ❌ Ignoring Structure
- Splits mid-sentence
- Breaks paragraph flow
- Loses semantic coherence

---

## 📈 Choosing Chunk Size: Practical Guide

### Small Chunks (256-512 tokens)
**Good for**:
- Specific fact retrieval
- Question-answering
- High precision needs

**Bad for**:
- Complex reasoning
- Multi-part questions
- Context-heavy tasks

### Medium Chunks (512-1024 tokens) ⭐ **Most Common**
**Good for**:
- General purpose RAG
- Balanced precision/recall
- Most use cases

### Large Chunks (1024-2048 tokens)
**Good for**:
- Complex reasoning
- Multi-step questions
- Context-heavy retrieval

**Bad for**:
- Precision-focused tasks
- Limited embedding models

---

## 🎨 The Overlap Strategy Explained

### Why Overlap Matters

```
Document: "The cat sat on the mat. The dog barked loudly."

Chunk 1 (no overlap): "The cat sat on the mat."
Chunk 2 (no overlap): "The dog barked loudly."

Problem: If query is about "mat and dog", chunks are separate!

Chunk 1 (with overlap): "The cat sat on the mat. The dog"
Chunk 2 (with overlap): "on the mat. The dog barked loudly."

Benefit: Context preserved, better retrieval!
```

### Overlap Guidelines

- **10% overlap**: Minimal, for storage efficiency
- **20% overlap**: Recommended (good balance)
- **30% overlap**: Maximum (diminishing returns)

---

## 🚀 Quick Start Examples

### Example 1: Simple Fixed-Size (Most Common)
```python
from examples import chunk_fixed_size

text = "Your document text here..."
chunks = chunk_fixed_size(text, chunk_size=512, overlap=50)
```

### Example 2: Sentence-Aware (Better Boundaries)
```python
from examples import chunk_by_sentences

chunks = chunk_by_sentences(text, chunk_size=512, overlap_sentences=2)
```

### Example 3: Paragraph-Based (Semantic)
```python
from examples import chunk_by_paragraphs

chunks = chunk_by_paragraphs(text, max_chunk_size=1024)
```

---

## 📚 Advanced Topics (Beyond the 80%)

These are powerful but not essential for most use cases:

1. **Recursive Chunking**: Split by paragraphs, then sentences
2. **Token Counting**: Use actual tokenizers (tiktoken, transformers)
3. **Metadata Preservation**: Track chunk position, source, etc.
4. **Hybrid Strategies**: Combine multiple chunking methods
5. **Dynamic Sizing**: Adjust chunk size based on content

See `examples.py` for implementations of these.

---

## 🎯 Best Practices Summary

1. ✅ **Start with fixed-size + 10-20% overlap**
2. ✅ **Respect sentence boundaries** (avoid mid-sentence splits)
3. ✅ **Choose chunk size based on your embedding model**
4. ✅ **Test retrieval quality** with your specific documents
5. ✅ **Monitor chunk statistics** (size distribution, overlap)

---

## 📖 Next Steps

1. **Run examples.py** to see chunking in action
2. **Complete exercises.py** to practice
3. **Experiment** with your own documents
4. **Measure** retrieval quality with different strategies

---

## 🔗 Related Concepts

- **Embedding Models**: Chunk size affects embedding quality
- **Retrieval**: Smaller chunks = more precise, larger = more context
- **Vector Databases**: Chunk size affects indexing and search
- **Token Limits**: Always check your model's limits

---

## 💡 Key Takeaways

1. **80% of cases**: Fixed-size chunking (512-1024) + 10-20% overlap
2. **Always use overlap**: Prevents information loss at boundaries
3. **Respect structure**: Use sentence/paragraph boundaries when possible
4. **Test and iterate**: Chunk size affects retrieval quality
5. **Keep it simple**: Start simple, add complexity only when needed

---

**Remember**: The best chunking strategy is the one that works for YOUR documents and YOUR use case. Start simple, measure results, and iterate!

