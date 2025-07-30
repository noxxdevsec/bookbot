def get_book_text(path_to_file):
    with open(path_to_file) as file:
        file_content = file.read()
    return file_content

def count_words(text):
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)

    print(f"{num_words} words found in the document ")


main()

