""" 
    This module uses a function to calculate the frequency   of characters in a given text
"""

def counter(user_input: str) -> dict[str,int]:
    
    """ This is a function that takes users input as a string and return the character frequency as a dictionary

    Args:
        user_input (str): An input string to analyse 

    Returns:
        dict[str,int]: A dictionary with character or letters as keys and frequency counts as values
    """
    
    
    
    normalized_text = user_input.lower().strip()
    cleaned_text = "".join(char for char in normalized_text if char.isalpha() or char.isspace())
    
    
    frequency = {}
    
    for word in cleaned_text:
        for text_char in word:
            if text_char in frequency:
                frequency[text_char]+=1
            else:
                frequency[text_char]=1
    
    return frequency


if __name__ == "__main__":
    while True:
        user_input = input("type in your response: ")
        if user_input:   
            result = counter(user_input)
            print(f'result {result}')
            break
        print("Invalid response")