# math utils
def is_even(n):
    """
    Checks if even number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return n % 2 == 0


def is_odd(n):
    """
    Checks if odd number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    return n % 2 != 0


def factorial(n):
    """
    Return the factorial of a number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n-1)


def is_prime(n):
    """
    Checks if a number is a prime number
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# string utils
def reverse(text):
    """
    Return the string reversed
    """
    return text[::-1]


def count_vowels(text):
    """
    Count how many vowels in a string
    """
    return sum(1 for char in text.lower() if char in 'aeiou')


def capitalize_words(text):
    """
    Capitalize each word on the string
    """
    return ' '.join(word.capitalize() for word in text.split())


# list utils
def unique(lst):
    """
    Return a list with the duplicates removed
    """
    result = []
    seen = set()
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten(nested_list):
    """
    Flatten a nested list
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(lst, size):
    """
    Use to split the list into chunks of given size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be greater than 0")
    return [lst[i:i+size] for i in range(0, len(lst), size)]
