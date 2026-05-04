import sys

def main():
    """
    This program counts characters in a string (Upper, Lower, Digits, Spaces, Punctuation and total number).
    If no argument is provided, the user is prompted to input an argument to be counted.
    When the number of arguments is greater than 1, exception throws an AssertionError and exits.
    """

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        text += '\n'
    else:
        text = sys.argv[1]

    if len(sys.argv) > 2:
        raise AssertionError("more than 1 argument provided. Max 1 argument")

    count_upper = 0
    count_lower = 0
    count_punctuation = 0
    count_digits = 0
    count_spaces = 0
    count_total = 0

    for char in text:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digits += 1
        elif char.isspace():
            count_spaces += 1
        else:
            count_punctuation += 1
    
    count_total = count_upper + count_lower + count_punctuation + count_digits + count_spaces

    print(f"The text contains {count_total} characters:\n{count_upper} upper letters\n{count_lower} lower letters\n{count_punctuation} punctuation marks\n{count_spaces} spaces\n{count_digits} digits")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
