def count_num_of_words(text):
    words = text.split()
    return len(words)


def count_num_of_characters(text):
    total_characters={}
    new_text = text.lower()

    for char in new_text:
        if char in total_characters:
            total_characters[char] +=1
        else:
            total_characters[char] =1

    return total_characters

def create_sorted_list(unsorted_dict):
    sorted_list = []

    for key,value in unsorted_dict.items():
        sorted_list.append({"char":key,"num":value})

    sorted_list.sort(reverse=True, key=lambda item: item["num"])   
    
    return sorted_list


