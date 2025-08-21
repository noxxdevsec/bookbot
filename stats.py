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


    


    