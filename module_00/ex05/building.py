from curses.ascii import isdigit, isspace
import sys


def print_upper_letters(phrase: str) -> None:
    """
    This function prints the count of all upper case letters
    in a phrase passed as argument

    Parameters:
        phrase (str): The phrase to be analyzed
    """
    count = 0
    for letter in phrase:
        if letter.isupper():
            count += 1
    print(f'{count} upper letters')


def print_lower_letters(phrase: str) -> None:
    """
    This function prints the count of all lower case letters
    in a phrase passed as argument

    Parameters:
        phrase (str): The phrase to be analyzed
    """
    count = 0
    for letter in phrase:
        if letter.islower():
            count += 1
    print(f'{count} lower letters')


def print_punctuation_marks(phrase: str) -> None:
    """
    This function prints the count of all punctuation marks
    in a phrase passed as argument

    Parameters:
        phrase (str): The phrase to be analyzed
    """
    count = 0
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for letter in phrase:
        if letter in punc:
            count += 1
    print(f'{count} punctuation marks')


def print_spaces_count(phrase: str) -> None:
    """
    This function prints the count of all spaces
    in a phrase passed as argument

    Parameters:
        phrase (str): The phrase to be analyzed
    """
    count = 0
    for letter in phrase:
        if letter.isspace():
            count += 1
    print(f'{count} spaces')
    

def print_digits_count(phrase: str) -> None:
    """
    This function prints the count of all digits
    in a phrase passed as argument

    Parameters:
        phrase (str): The phrase to be analyzed
    """
    count = 0
    for letter in phrase:
        if letter.isdigit():
            count += 1
    print(f'{count} digits')


def main():
    if len(sys.argv) > 2:
        raise AssertionError(
            "Error! Too much arguments.\nCorrect usage: python building.py arg"
        )
    if len(sys.argv) == 1 or not sys.argv[1]:
        phrase = ""
        while not phrase:
            phrase = input("What is the text to count?\n")
    else:
        phrase = sys.argv[1]
    print(f"The text contains {len(phrase)} characters:")
    print_upper_letters(phrase)
    print_lower_letters(phrase)
    print_punctuation_marks(phrase)
    print_spaces_count(phrase)
    print_digits_count(phrase)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"Error: {e}")
