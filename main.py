dict_character = {}
dict_list = []
wordcount = 0

def sweet_printing():
    print("--- Begin report of books/frankenstein.txt ---")
    print(wordcount, "words found in the document")
    print()
    for position in dict_list:
        print(f"The '{position["char"]}' character was found {position["num"]} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


def create_dictionary_list(dict):
    for char, count in dict.items():
        dict_list.append({"char":char, "num":count})
    dict_list.sort(reverse=True,key=sort_on)
    print("Hier: ", dict_list)
        



def count_characters(string):
    lowered_string = string.lower()
    split_words = lowered_string.split()
    for word in split_words:
        char_list = list(word)
        for char in char_list:
            if char in dict_character and char.isalpha():
                dict_character[char] += 1
            else:
                if char.isalpha():
                    dict_character[char] = 1
    print("Character counts: ", dict_character)



def count_words(string):
    #print("Wordcount: ", len(string.split()))
    return len(string.split())



def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        wordcount = count_words(file_contents)
        count_characters(file_contents)
        create_dictionary_list(dict_character)
        sweet_printing()




main()