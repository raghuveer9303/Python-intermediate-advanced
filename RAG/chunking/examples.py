"""
RAG Chunking Examples - The 80/20 Essentials
Focus on what works 80% of the time
"""

import re
from typing import List, Dict, Any
from collections import deque


# ============================================================================
# 1. FIXED-SIZE CHUNKING (Most Common - 80% of cases)
# ============================================================================

def chunk_fixed_size(text: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
    """
    Simple fixed-size chunking with overlap.
    
    Why overlap? Prevents information loss at chunk boundaries.
    Rule of thumb: overlap = 10-20% of chunk_size
    
    Args:
        text: Input text to chunk
        chunk_size: Size of each chunk in characters
        overlap: Number of characters to overlap between chunks
    
    Returns:
        List of text chunks
    """
    if not text:
        return []
    
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        
        # Move start by (chunk_size - overlap) to create overlap
        start = end - overlap
        if start >= len(text):
            break
    
    return chunks


# ============================================================================
# 2. SENTENCE-AWARE CHUNKING (Better boundaries - 20% upgrade)
# ============================================================================

def chunk_by_sentences(
    text: str, 
    chunk_size: int = 512, 
    overlap_sentences: int = 2
) -> List[str]:
    """
    Chunk by sentences, respecting sentence boundaries.
    Better than fixed-size because it doesn't cut mid-sentence.
    
    Args:
        text: Input text to chunk
        chunk_size: Approximate chunk size in characters
        overlap_sentences: Number of sentences to overlap between chunks
    
    Returns:
        List of text chunks
    """
    if not text:
        return []
    
    # Split into sentences (simple regex - can use spaCy/NLTK for better)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if not sentences:
        return [text]
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for sentence in sentences:
        sentence_size = len(sentence)
        
        # If adding this sentence would exceed chunk_size
        if current_size + sentence_size > chunk_size and current_chunk:
            # Save current chunk
            chunks.append(' '.join(current_chunk))
            
            # Start new chunk with overlap (last N sentences)
            overlap_count = min(overlap_sentences, len(current_chunk))
            overlap_sents = current_chunk[-overlap_count:] if overlap_count > 0 else []
            current_chunk = overlap_sents + [sentence]
            current_size = sum(len(s) for s in current_chunk)
        else:
            current_chunk.append(sentence)
            current_size += sentence_size
    
    # Don't forget the last chunk
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks


# ============================================================================
# 3. PARAGRAPH-BASED CHUNKING (Semantic boundaries)
# ============================================================================

def chunk_by_paragraphs(
    text: str, 
    max_chunk_size: int = 1024,
    min_chunk_size: int = 256
) -> List[str]:
    """
    Chunk by paragraphs. Each paragraph is a natural semantic unit.
    
    Args:
        text: Input text to chunk
        max_chunk_size: Maximum chunk size (if paragraph exceeds, split it)
        min_chunk_size: Minimum chunk size (merge small paragraphs)
    
    Returns:
        List of text chunks
    """
    if not text:
        return []
    
    # Split by double newlines (paragraphs)
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    
    if not paragraphs:
        return [text]
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para_size = len(para)
        
        # If paragraph is too large, split it
        if para_size > max_chunk_size:
            # Save current chunk first
            if current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = []
                current_size = 0
            
            # Split large paragraph using sentence-aware method
            para_chunks = chunk_by_sentences(para, chunk_size=max_chunk_size)
            chunks.extend(para_chunks)
            continue
        
        # If adding this paragraph would exceed max_chunk_size
        if current_size + para_size > max_chunk_size and current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            current_chunk = [para]
            current_size = para_size
        else:
            current_chunk.append(para)
            current_size += para_size
    
    # Handle last chunk
    if current_chunk:
        # Merge small final chunk with previous if needed
        if current_size < min_chunk_size and chunks:
            chunks[-1] = chunks[-1] + '\n\n' + '\n\n'.join(current_chunk)
        else:
            chunks.append('\n\n'.join(current_chunk))
    
    return chunks


# ============================================================================
# 4. RECURSIVE CHUNKING (Advanced - combines multiple strategies)
# ============================================================================

def chunk_recursive(
    text: str,
    chunk_size: int = 512,
    overlap: int = 50,
    separators: List[str] = None
) -> List[str]:
    """
    Recursive chunking: tries to split by separators first,
    falls back to fixed-size if needed.
    
    Args:
        text: Input text to chunk
        chunk_size: Target chunk size
        overlap: Overlap size
        separators: List of separators to try (in order of preference)
    
    Returns:
        List of text chunks
    """
    if separators is None:
        separators = ['\n\n', '\n', '. ', ' ', '']
    
    if not text or len(text) <= chunk_size:
        return [text] if text else []
    
    # Try each separator
    for sep in separators:
        if sep == '':
            # Last resort: fixed-size chunking
            return chunk_fixed_size(text, chunk_size, overlap)
        
        splits = text.split(sep)
        if len(splits) > 1:
            chunks = []
            current_chunk = []
            current_size = 0
            
            for split in splits:
                split_with_sep = split + sep if split != splits[-1] else split
                split_size = len(split_with_sep)
                
                if current_size + split_size > chunk_size and current_chunk:
                    chunks.append(sep.join(current_chunk))
                    current_chunk = [split]
                    current_size = split_size
                else:
                    current_chunk.append(split)
                    current_size += split_size
            
            if current_chunk:
                chunks.append(sep.join(current_chunk))
            
            # Recursively chunk any chunks that are still too large
            final_chunks = []
            for chunk in chunks:
                if len(chunk) > chunk_size:
                    final_chunks.extend(chunk_recursive(chunk, chunk_size, overlap, separators))
                else:
                    final_chunks.append(chunk)
            
            return final_chunks
    
    return [text]


# ============================================================================
# 5. CHUNKING WITH METADATA (Track position, source, etc.)
# ============================================================================

def chunk_with_metadata(
    text: str,
    chunk_size: int = 512,
    overlap: int = 50,
    source: str = None,
    chunk_fn: callable = None
) -> List[Dict[str, Any]]:
    """
    Chunk text and attach metadata to each chunk.
    
    Args:
        text: Input text to chunk
        chunk_size: Chunk size
        overlap: Overlap size
        source: Source document identifier
        chunk_fn: Function to use for chunking (default: chunk_fixed_size)
    
    Returns:
        List of dictionaries with chunk text and metadata
    """
    if chunk_fn is None:
        chunk_fn = chunk_fixed_size
    
    chunks = chunk_fn(text, chunk_size, overlap)
    
    result = []
    for i, chunk in enumerate(chunks):
        result.append({
            'chunk_id': i,
            'text': chunk,
            'source': source,
            'chunk_size': len(chunk),
            'start_char': text.find(chunk) if chunk in text else None,
        })
    
    return result


# ============================================================================
# 6. UTILITY FUNCTIONS
# ============================================================================

def get_chunk_stats(chunks: List[str]) -> Dict[str, Any]:
    """Get statistics about chunks."""
    if not chunks:
        return {}
    
    sizes = [len(chunk) for chunk in chunks]
    
    return {
        'num_chunks': len(chunks),
        'min_size': min(sizes),
        'max_size': max(sizes),
        'avg_size': sum(sizes) / len(sizes),
        'total_chars': sum(sizes),
    }


def print_chunk_stats(chunks: List[str], title: str = "Chunk Statistics"):
    """Print chunk statistics in a readable format."""
    stats = get_chunk_stats(chunks)
    print(f"\n{title}")
    print("-" * 40)
    print(f"Number of chunks: {stats['num_chunks']}")
    print(f"Min size: {stats['min_size']} chars")
    print(f"Max size: {stats['max_size']} chars")
    print(f"Avg size: {stats['avg_size']:.1f} chars")
    print(f"Total chars: {stats['total_chars']}")


# ============================================================================
# 7. DEMONSTRATION EXAMPLES
# ============================================================================

if __name__ == "__main__":
    # Sample text for demonstration
    sample_text = """
    Python is a high-level programming language known for its simplicity and readability.
    It was created by Guido van Rossum and first released in 1991.
    Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
    
    The language emphasizes code readability and allows programmers to express concepts in fewer lines of code.
    Python's syntax enables programmers to write clear, logical code for both small and large-scale projects.
    
    Python has a comprehensive standard library and a large ecosystem of third-party packages.
    It is widely used in web development, data science, artificial intelligence, and automation.
    """
    
    print("=" * 60)
    print("CHUNKING EXAMPLES - The 80/20 Essentials")
    print("=" * 60)
    
    # Example 1: Fixed-size chunking
    print("\n1. FIXED-SIZE CHUNKING (512 chars, 50 overlap)")
    print("-" * 60)
    chunks1 = chunk_fixed_size(sample_text, chunk_size=512, overlap=50)
    print_chunk_stats(chunks1)
    print("\nFirst chunk:")
    print(chunks1[0][:200] + "..." if len(chunks1[0]) > 200 else chunks1[0])
    
    # Example 2: Sentence-aware chunking
    print("\n\n2. SENTENCE-AWARE CHUNKING (512 chars, 2 sentence overlap)")
    print("-" * 60)
    chunks2 = chunk_by_sentences(sample_text, chunk_size=512, overlap_sentences=2)
    print_chunk_stats(chunks2)
    print("\nFirst chunk:")
    print(chunks2[0][:200] + "..." if len(chunks2[0]) > 200 else chunks2[0])
    
    # Example 3: Paragraph-based chunking
    print("\n\n3. PARAGRAPH-BASED CHUNKING (max 1024 chars)")
    print("-" * 60)
    chunks3 = chunk_by_paragraphs(sample_text, max_chunk_size=1024)
    print_chunk_stats(chunks3)
    print("\nFirst chunk:")
    print(chunks3[0][:200] + "..." if len(chunks3[0]) > 200 else chunks3[0])
    
    # Example 4: Chunking with metadata
    print("\n\n4. CHUNKING WITH METADATA")
    print("-" * 60)
    chunks4 = chunk_with_metadata(sample_text, chunk_size=512, source="python_intro.txt")
    print(f"Number of chunks: {len(chunks4)}")
    print("\nFirst chunk metadata:")
    for key, value in chunks4[0].items():
        if key != 'text':
            print(f"  {key}: {value}")
    
    print("\n" + "=" * 60)
    print("Examples complete!")

