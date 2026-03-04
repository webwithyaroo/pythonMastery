"""
Word Frequency Counter

This module provides functionality to count the frequency
of words in a given text input after normalization.
"""


def counter():
    """Takes user input, Normalizes it, Removes punctuation and split text
        
    parameter: 
        a(string): The words 

    return:
        dic: The final result after performing all the operations 

    """
    
    dic = {}
    
    while True:
        words = input("How are you doing to day: ")
        if words:
            text = words.lower().strip()
            cleaned_text = "".join(char for char in text if char.isalpha() or char.isspace())
            
            text_split = cleaned_text.split()
            for text in text_split:
                if text in dic:
                    dic[text]+= 1
                else: 
                    dic[text]=1
        
            break
            
        print("Input a valid response")
 
    return dic
    
counter()

