def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    sorted_chars = sort_char_count(char_count)
    print_report(book_path, word_count, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}

    for char in text:
        lowered = char.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1

    return char_count

def print_report(path, count, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print("")

    for item in chars:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End Report ---")


def sort_on(dict):
    return dict["num"]

def sort_char_count(chars):
    char_list = []

    for ch in chars:
        char_list.append({"char": ch, "num": chars[ch]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list

main()
