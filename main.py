import sys
from stats import count_num_of_words
from stats import count_num_of_characters
from stats import create_sorted_list


def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_content = file.read()
    return file_content



def main():

    if len(sys.argv) < 2:

        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_num_of_words(book_text)
    num_characters = count_num_of_characters(book_text)

    sorted_list = create_sorted_list(num_characters)



    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()

