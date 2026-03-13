        
def counter_2 (text: str, min_length = 3, top_n=3) -> list[tuple[str,int]]:
    normalized_text = text.lower()
    cleaned_text = "".join(char for char in normalized_text if text.isspace() or text.isalpha())
    split_text = cleaned_text.split()
    
    word_check = [word for word in split_text if len(word) >= min_length ]
        
    frequency = {}
    
    for word in word_check:
        if word in frequency:
            frequency[word]+=1
            
        else:
            frequency[word]=1
    
    freq_result = frequency.items()
    sort_item = sorted(freq_result, key=lambda item: item[1], reverse=True)
    top_items = sort_item[0:top_n]
    
    return top_items
        
if __name__ == "__main__":
    while True:
        user_input = input("Input: ")
        if user_input:
            result = counter_2(user_input, 2, 2)
            print(result)
            break
        print("Invalid input")