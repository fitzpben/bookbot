import sys
import re

def count_words(file_contents):
    word_count = 0

    word_list = file_contents.split()

    word_count = len(word_list)

    return word_count

def count_char(file_contents):
    char_count_dict = {}

    file_contents = file_contents.lower()
    
    for character in file_contents:
        if re.findall("[a-z]", character):
            try:
                char_count_temp = char_count_dict[character]
                char_count_dict.update({character: char_count_temp + 1})
            except:
                char_count_dict.update({character: 1})

    return char_count_dict

def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count_dict = count_char(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(word_count)
    print("")
    for key, value in sorted(char_count_dict.items(), key=lambda item: item[1], reverse=reversed):
        line = f"The '{key}' character was found {value} times"
        print(line)
    print("--- End report ---")

if __name__ == '__main__':
   sys.exit(main())