import string

def palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    word = word.translate(str.maketrans('', '', string.punctuation))
    rword = "".join(reversed(word))

    if word == rword:
        print(rword)
        print(f"{word} is a palindrome.")
        return True
    else:
        print(rword)
        print(f"{word} is not a palindrome.")
        return False    

# word = input("Enter a word: ")

# palindrome(word)
    

def parenthesis(text):
    open_parenthesis = 0
    close_parenthesis = 0

    for char in text:
        if char == '(':
            open_parenthesis += 1
        elif char == ')':
            close_parenthesis += 1

    if open_parenthesis == close_parenthesis:
        print("The parentheses are balanced.")
        return True
    else:
        print("The parentheses are not balanced.")
        return False


text = input("Enter a Text: ")

parenthesis(text)
