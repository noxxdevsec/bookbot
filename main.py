from stats import count_num_of_words
from stats import count_num_of_characters


def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_content = file.read()
    return file_content



def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_num_of_words(book_text)
    num_characters = count_num_of_characters(book_text)

    print(f"{num_words} words found in the document ")
    print(num_characters)


main()

