"""
RAG Chunking Exercises - Practice the 80/20 Essentials
Complete these exercises to master chunking strategies
"""

from examples import (
    chunk_fixed_size,
    chunk_by_sentences,
    chunk_by_paragraphs,
    chunk_recursive,
    chunk_with_metadata,
    get_chunk_stats,
    print_chunk_stats
)


# ============================================================================
# EXERCISE 1: Basic Fixed-Size Chunking
# ============================================================================

def exercise_1():
    """
    Create fixed-size chunks from a long text.
    
    Instructions:
    1. Use the sample text below
    2. Chunk it into 256-character chunks with 25-character overlap
    3. Print the number of chunks created
    4. Print the first and last chunk
    """
    text = """
    Artificial Intelligence (AI) is transforming the way we work and live.
    Machine learning algorithms can now recognize patterns in data that humans cannot see.
    Deep learning models have achieved remarkable success in image recognition, natural language processing, and game playing.
    The future of AI holds promise for solving complex problems in healthcare, climate change, and education.
    However, we must also consider the ethical implications of AI and ensure it benefits all of humanity.
    """
    
    # TODO: Implement your solution here
    # chunks = ...
    # print(f"Created {len(chunks)} chunks")
    # print(f"First chunk: {chunks[0]}")
    # print(f"Last chunk: {chunks[-1]}")
    
    pass


# ============================================================================
# EXERCISE 2: Sentence-Aware Chunking
# ============================================================================

def exercise_2():
    """
    Use sentence-aware chunking to preserve sentence boundaries.
    
    Instructions:
    1. Use the text from exercise_1
    2. Chunk it using sentence-aware chunking with 512-character target size
    3. Use 2 sentence overlap
    4. Verify that no chunks split sentences in the middle
    5. Print statistics
    """
    text = """
    Natural Language Processing (NLP) is a branch of AI that focuses on understanding human language.
    Modern NLP models can translate between languages, answer questions, and generate text.
    Large language models like GPT have revolutionized the field.
    These models are trained on vast amounts of text data.
    They learn patterns and relationships in language.
    """
    
    # TODO: Implement your solution here
    # chunks = ...
    # print_chunk_stats(chunks, "Sentence-Aware Chunking Stats")
    
    pass


# ============================================================================
# EXERCISE 3: Paragraph-Based Chunking
# ============================================================================

def exercise_3():
    """
    Chunk a document by paragraphs while respecting size limits.
    
    Instructions:
    1. Use the text below (has clear paragraphs)
    2. Chunk by paragraphs with max 1024 characters
    3. Print which chunks were created
    4. Verify paragraphs aren't split unless they exceed max size
    """
    text = """
    Python is a versatile programming language used in many domains.

    Web development frameworks like Django and Flask make Python popular for building web applications.
    These frameworks provide tools for handling HTTP requests, database connections, and user authentication.

    Data science libraries like Pandas and NumPy enable analysts to work with large datasets.
    Scientists use Python for statistical analysis, machine learning, and data visualization.

    Python's simplicity makes it an excellent choice for beginners.
    The language's readability reduces the learning curve for new programmers.
    """
    
    # TODO: Implement your solution here
    # chunks = ...
    # for i, chunk in enumerate(chunks):
    #     print(f"\nChunk {i+1}:")
    #     print(chunk[:150] + "..." if len(chunk) > 150 else chunk)
    
    pass


# ============================================================================
# EXERCISE 4: Chunking with Metadata
# ============================================================================

def exercise_4():
    """
    Create chunks with metadata for tracking.
    
    Instructions:
    1. Chunk the text using fixed-size chunking (512 chars, 50 overlap)
    2. Add metadata including chunk_id, source, and chunk_size
    3. Print the metadata for all chunks
    4. Find the chunk with the largest size
    """
    text = """
    Vector databases are specialized databases designed for storing and querying high-dimensional vectors.
    They are essential for similarity search in machine learning applications.
    Popular vector databases include Pinecone, Weaviate, and Milvus.
    These databases use approximate nearest neighbor algorithms for fast search.
    """
    
    # TODO: Implement your solution here
    # chunks_with_meta = ...
    # for chunk in chunks_with_meta:
    #     print(f"Chunk {chunk['chunk_id']}: {chunk['chunk_size']} chars from {chunk['source']}")
    
    pass


# ============================================================================
# EXERCISE 5: Compare Chunking Strategies
# ============================================================================

def exercise_5():
    """
    Compare different chunking strategies on the same text.
    
    Instructions:
    1. Use the same text for all three strategies
    2. Compare fixed-size, sentence-aware, and paragraph-based chunking
    3. Print statistics for each
    4. Analyze which produces the most chunks and which produces the largest average chunk
    """
    text = """
    Retrieval-Augmented Generation (RAG) combines the power of language models with external knowledge.
    RAG systems retrieve relevant information from a knowledge base before generating responses.
    This approach reduces hallucinations and provides more accurate information.
    
    The RAG pipeline consists of three main steps: indexing, retrieval, and generation.
    First, documents are chunked and embedded into a vector database.
    Then, relevant chunks are retrieved based on query similarity.
    Finally, the language model uses retrieved chunks to generate accurate responses.
    
    Chunking is a critical component of RAG systems.
    Poor chunking strategies can lead to information loss or irrelevant retrieval.
    Good chunking preserves context while maintaining manageable chunk sizes.
    """
    
    # TODO: Implement your solution here
    # chunks_fixed = ...
    # chunks_sentences = ...
    # chunks_paragraphs = ...
    # 
    # print("Fixed-size chunking:")
    # print_chunk_stats(chunks_fixed)
    # print("\nSentence-aware chunking:")
    # print_chunk_stats(chunks_sentences)
    # print("\nParagraph-based chunking:")
    # print_chunk_stats(chunks_paragraphs)
    
    pass


# ============================================================================
# EXERCISE 6: Handle Edge Cases
# ============================================================================

def exercise_6():
    """
    Handle edge cases in chunking.
    
    Instructions:
    1. Test chunking with empty text
    2. Test chunking with text shorter than chunk_size
    3. Test chunking with text that has no sentence boundaries
    4. Test chunking with text that has no paragraph breaks
    5. Ensure your functions handle all these cases gracefully
    """
    # Edge case 1: Empty text
    empty_text = ""
    
    # Edge case 2: Text shorter than chunk size
    short_text = "This is a short text."
    
    # Edge case 3: Text with no sentence boundaries
    no_sentences = "word1 word2 word3 word4 word5" * 100
    
    # Edge case 4: Text with no paragraph breaks
    no_paragraphs = "This is one long paragraph. " * 50
    
    # TODO: Test each edge case
    # print("Testing empty text:")
    # chunks = chunk_fixed_size(empty_text)
    # print(f"Result: {chunks}")
    
    pass


# ============================================================================
# EXERCISE 7: Custom Chunking Strategy
# ============================================================================

def exercise_7():
    """
    Create a custom chunking strategy.
    
    Instructions:
    1. Create a function that chunks by sections (marked by "##" headers)
    2. If a section is too large, recursively chunk it using sentences
    3. Maintain overlap between sections
    4. Test it on a markdown-style document
    """
    markdown_text = """
    ## Introduction
    This is the introduction section. It contains multiple sentences.
    Each sentence provides important context for the topic.
    
    ## Main Content
    This is the main content section. It has detailed information.
    The information is organized into paragraphs for clarity.
    This section might be longer than the previous one.
    
    ## Conclusion
    This is the conclusion section. It summarizes the key points.
    """
    
    # TODO: Implement custom chunking function
    # def chunk_by_sections(text, max_size=512):
    #     ...
    # 
    # chunks = chunk_by_sections(markdown_text)
    # for i, chunk in enumerate(chunks):
    #     print(f"Section Chunk {i+1}: {chunk[:100]}...")
    
    pass


# ============================================================================
# EXERCISE 8: Optimize Chunk Size
# ============================================================================

def exercise_8():
    """
    Find the optimal chunk size for a given document.
    
    Instructions:
    1. Create a function that tests different chunk sizes
    2. Calculate statistics for each chunk size (256, 512, 1024, 2048)
    3. Consider: number of chunks, average size, size variance
    4. Recommend the best chunk size based on your criteria
    """
    text = """
    Machine learning is a subset of artificial intelligence.
    It focuses on algorithms that can learn from data.
    Supervised learning uses labeled data to train models.
    Unsupervised learning finds patterns in unlabeled data.
    Reinforcement learning learns through interaction with an environment.
    Deep learning uses neural networks with multiple layers.
    These networks can learn complex representations of data.
    Transfer learning applies knowledge from one task to another.
    """
    
    # TODO: Implement optimization function
    # def find_optimal_chunk_size(text, sizes=[256, 512, 1024, 2048]):
    #     ...
    # 
    # optimal = find_optimal_chunk_size(text)
    # print(f"Recommended chunk size: {optimal}")
    
    pass


# ============================================================================
# SOLUTIONS RUNNER
# ============================================================================

def run_all_exercises():
    """Run all exercises (uncomment as you complete them)."""
    print("=" * 60)
    print("RAG CHUNKING EXERCISES")
    print("=" * 60)
    
    # Uncomment exercises as you complete them
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # exercise_5()
    # exercise_6()
    # exercise_7()
    # exercise_8()
    
    print("\n" + "=" * 60)
    print("Complete the exercises above!")
    print("=" * 60)


if __name__ == "__main__":
    run_all_exercises()

