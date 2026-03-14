        



def clean_text(text: str, sort_by):
    
    normalized_text = text.lower()
    choice = sort_by.lower()
    cleaned_text = "".join(char for char in normalized_text if char.isspace() or char.isalpha())
    
    split_text(cleaned_text)
    
    return cleaned_text

def split_text(cleaned_text: str):
    split_text = cleaned_text.split()
    return split_text

def filter_words(min_length: int):
    word_check = [word for word in split_text if len(word) >= min_length ]
    
    count_frequency(word_check)
    
    return word_check

def count_frequency(word_check: list):
    frequency = {}
    
    for word in word_check:
        if word in frequency:
            frequency[word]+=1
            
        else:
            frequency[word]=1
    
    sort_result(frequency)
    return frequency

def sort_result(frequency, sort_by, top_n):
    freq_result = frequency.items()
    
    if sort_by == "frequency":
        sort_item = sorted(freq_result, key=lambda item: item[1], reverse=True)
    else:
        sort_item = sorted(freq_result, key=lambda item: item[0])
    
    top_items = sort_item[0:top_n]
    
    return top_items





def analyze_words (text: str, min_length = 3, top_n=3, sort_by = "frequency") -> list[tuple[str,int]]:

    cln_text = clean_text(text, sort_by)
    spt_text = split_text(cln_text)
    fit_word = filter_words(spt_text)
    result = sort_result(fit_word)
  
    return result

    
        
if __name__ == "__main__":
    while True:
        user_input = input("Input: ")
        sort_by = input("sort by WORD or FREQUENCY: ")
        if user_input:
            result = analyze_words(user_input, 2, 2, sort_by)
            print(result)
            break
        print("Invalid input")
        
        