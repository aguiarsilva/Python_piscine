import sys
import ft_filter


def main():
    """
    Returns a list of words from s that have a length greater \
            than n. Words must be separated by spaces. \
    Strings do not contain any special charachters (punctuation or invisible).
    If the number of arguments is different than 2 or if type is wrong, \
            the program prints an AssertionError.
    """
    if len(sys.argv) != 2:
        raise AssertionError("wrong number of arguments. Only 2 allowed.")

    if not isinstance(sys.argv[1], str) or isinstance(sys.argv[2], int):
        raise AssertionError("wrong type of arguments. First arg \
                must be a str and second an int.")
    
    user_input = sys.argv[1].split()

    result = list(ft_filter(lambda s, n: [word for word in s if len(word) > n]))
    return result


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
