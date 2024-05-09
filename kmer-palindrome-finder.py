#!/usr/bin/env python
# coding: utf-8

# In[6]:


import itertools


DNA_CHARS = "ACGT"
TRANSLATION_TABLE = str.maketrans("ACGT", "TGCA")

def dna_kmer_generator(k):
    """
    Generate all possible DNA k-mers of length k as a generator.
    
    Parameters:
        k (int): The length of the k-mer.
    
    Yields:
        str: A DNA k-mer.
    """
    for ktup in itertools.product(DNA_CHARS, repeat=k):
        yield "".join(ktup)

def revcomp(kmer):
    """
    Compute the reverse complement of a DNA k-mer.
    
    Parameters:
        kmer (str): The DNA k-mer.
    
    Returns:
        str: The reverse complement of the k-mer.
    """
    return kmer.translate(TRANSLATION_TABLE)[::-1]

def num_palindromes(mylist):
    """
    Count how many DNA k-mers in the list are palindromic.
    
    Parameters:
        mylist (iterable[str]): An iterable of DNA k-mers.
    
    Returns:
        int: The number of palindromic k-mers.
    """
    return sum(1 for kmer in mylist if kmer[:len(kmer)//2] == revcomp(kmer[len(kmer)//2:])[::-1])


# In[ ]:




