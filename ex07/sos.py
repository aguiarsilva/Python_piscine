import sys


def main():
    """
    Returns a string as Morse Code. Program supports spaces and \
            alphanumeric char
    The alphanumeric char is represented by dots and dashes.
    Complete Morse Code chars are separated by a single space.
    Space is represented by a slash /.
    """

    if len(sys.argv) != 2:
        raise AssertionError("wrong number of arguments")

    user_input = sys.argv[1]

    for char in user_input:
        if not (char.isalnum() or char.isspace()):
            raise AssertionError("wrong type of argument")

    converted_text = text_to_morse(user_input)
    print(converted_text)


def text_to_morse(text):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/ '}

    return ' '.join([morse_dict[ch] for ch in text.upper()
                     if ch in morse_dict])


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)
