"""
    Word Filter & Counter: A program that analyzes user text.
"""

def counter(user_input: str) -> dict[str, int]:
    """ This is a function that takes in string as a user input and analyses it.

    Args:
        user_input (str): The user input

    Returns:
        dict[str,int]: A dictionary containing the analyzed word   
"""
    frequency = {}
    words = user_input.lower()
    cleaned_text = "".join(char for char in words if char.isalpha() or char.isspace())
    split_text = cleaned_text.split()
    
    for word in split_text:
        if (len(word) < 3):
            continue
        elif (word in frequency):
            frequency[word]+=1
        else:
            frequency[word]=1
    return frequency

if __name__ == "__main__":
    while True:
        user_input = input("User Input: ")
        if user_input:
            result = counter(user_input)
            print(result)
            break
        print("Invalid input")