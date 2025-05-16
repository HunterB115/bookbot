from stats import count_words
from stats import count_characters

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    print(f"{num_words} words found in the document")
    print(char_dict)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()