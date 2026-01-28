import string


def palindrome(word):
    """
    Check whether a given word or phrase is a palindrome.

    The function ignores case, spaces, and punctuation.

    Args:
        word (str): The word or phrase to check.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    cleaned_word = word.lower()
    cleaned_word = cleaned_word.replace(" ", "")
    cleaned_word = cleaned_word.translate(
        str.maketrans("", "", string.punctuation)
    )

    reversed_word = "".join(reversed(cleaned_word))

    print(reversed_word)

    if cleaned_word == reversed_word:
        print(f"{cleaned_word} is a palindrome.")
        return True

    print(f"{cleaned_word} is not a palindrome.")
    return False


def parenthesis(text):
    """
    Check whether parentheses in a string are balanced.

    Args:
        text (str): The text to analyze.

    Returns:
        bool: True if parentheses are balanced, False otherwise.
    """
    open_parenthesis = 0
    close_parenthesis = 0

    for char in text:
        if char == "(":
            open_parenthesis += 1
        elif char == ")":
            close_parenthesis += 1

    if open_parenthesis == close_parenthesis:
        print("The parentheses are balanced.")
        return True

    print("The parentheses are not balanced.")
    return False


text = input("Enter a text: ")
parenthesis(text)
