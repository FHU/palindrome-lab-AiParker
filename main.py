#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    word = word.replace(" ", "").lower()

    return word == word[::-1]

if __name__ == '__main__': 
    #REMOVE PASS AND YOUR CODE GOES HERE
    user_input = input("Enter a word: ")
    print(palindrome(user_input))
