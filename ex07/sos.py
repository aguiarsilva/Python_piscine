import sys


def main():
    """
    Returns a string as Morse Code. Program supports spaces and alphanumeric char\
    The alphanumeric char is represented by dots and dashes.
    Complete Morse Code chars are separated by a single space.
    Space is represented by a slash /.
    """
    if len(sys.argv) != 2:
        raise AssertionError("wrong number of arguments")

    user_input = sys.argv[1]



    print(user_input)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
