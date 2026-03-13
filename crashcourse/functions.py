        
def analyze_words (text: str, min_length = 3, top_n=3, sort_by = "frequency") -> list[tuple[str,int]]:
    normalized_text = text.lower()
    choice = sort_by.lower()
    
    cleaned_text = "".join(char for char in normalized_text if char.isspace() or char.isalpha())
    split_text = cleaned_text.split()
    
    word_check = [word for word in split_text if len(word) >= min_length ]
        
    frequency = {}
    
    for word in word_check:
        if word in frequency:
            frequency[word]+=1
            
        else:
            frequency[word]=1
    
    freq_result = frequency.items()

    if choice == "frequency":
        sort_item = sorted(freq_result, key=lambda item: item[1], reverse=True)
    else:
        sort_item = sorted(freq_result, key=lambda item: item[0])
    
    top_items = sort_item[0:top_n]
    
    return top_items
        
if __name__ == "__main__":
    while True:
        user_input = input("Input: ")
        sort_by = input("sort by WORD or FREQUENCY: ")
        if user_input:
            result = analyze_words(user_input, 2, 2, sort_by)
            print(result)
            break
        print("Invalid input")