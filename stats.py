def count_words(book_text):
    num_words = len(book_text.split())
    return num_words

def count_characters(book_text):
    char_dict = {}
    lowercase_text = book_text.lower()
    split_words = lowercase_text.split()
    for i in split_words:
        for c in i:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    return char_dict