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

def sort_dictionary(dictionary):
    character_list = []
    for i in dictionary:
        character_dict = {}
        char_value = dictionary[i]
        character_dict["char"] = i
        character_dict["num"] = char_value
        character_list.append(character_dict)
    
    return character_list

def sort_on(dict):
    return dict["num"]