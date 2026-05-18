import sys
from ft_filter import ft_filter


def main():
    """
    Returns a list of words from s that have a length greater \
            than n. Words must be separated by spaces. \
    Strings do not contain any special charachters (punctuation or invisible).
    If the number of arguments is different than 2 or if type is wrong, \
            the program prints an AssertionError.
    """
    if len(sys.argv) != 3:
        raise AssertionError("wrong number of arguments. Only 2 allowed.")

    user_input = sys.argv[1]

    try:
        n = int(sys.argv[2])
    except ValueError:
        raise AssertionError("wrong type of arguments.")

    words = user_input.split()

    result = ft_filter(lambda w: len(w) > n, [word for word in words])
    print(list(result))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
