"""
ft_package is a collection of simple utilities for math,
strings and lists
"""

__version__ = "0.0.1"

from .ft_package import (
    is_even, is_odd, factorial, is_prime,
    reverse, count_vowels, capitalize_words,
    unique, flatten, chunk
)

__all__ = [
        'is_even', 'is_odd', 'factorial', 'is_prime',
        'reverse', 'count_vowels', 'capitalize_words',
        'unique', 'flatten', 'chunk'
]
