def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        #print(file_contents)
        words = count_words(file_contents)
        characters = count_characters(file_contents)
        character_sorted_list = chars_dict_to_sorted_list(characters)



        print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    for item in character_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
        
        
def count_words(contents):
    words = contents.split()
    number_of_words = len(words)
    print(number_of_words)
def count_characters(contents):
    char_dict ={}
    n = len(contents)
    for i in range(0,n):
        char = contents[i].lower()
        if char in char_dict:
            char_dict[char]+=1
        else:
            char_dict[char] = 1
    return char_dict
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
main()