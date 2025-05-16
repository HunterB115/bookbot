from stats import count_words, count_characters, sort_dictionary, sort_on

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    sorted_dict = sort_dictionary(char_dict)
    sorted_dict.sort(reverse=True, key=sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()