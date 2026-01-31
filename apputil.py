import string

def palindrome(word):
    # Checks if a word is a palindrome, ignoring spaces, punctuation, and case.
    word = word.lower()
    # Remove spaces and punctuation
    word = word.replace(" ", "")
    # Remove punctuation
    word = word.translate(str.maketrans('', '', string.punctuation))
    # Reverse the word
    rword = "".join(reversed(word))

    # Compare the original word with the reversed word
    if word == rword:
        # print(f"{word} is a palindrome.")
        return True
    else:
        # print(f"{word} is not a palindrome.")
        return False    
    
    if __name__ == "__main__":
        word = input("Enter a word: ")
        print(palindrome(word))
    

def parenthesis(text):
    # Checks if the parentheses in the text are balanced
    balance = 0

    # Count opening and closing parentheses
    for char in text:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            # If balance goes negative, we have a closing before opening
            if balance < 0:
                return False

    # Check if all opened parentheses were closed
    if balance == 0:
        return True
    
    return False

    if __name__ == "__main__": 
        # print true or false based on balanced parentheses
        text = input("Enter a Text: ")
        print(parenthesis(text))    