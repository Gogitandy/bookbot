def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    print_report(book_path, word_count, char_count)

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
    sorted_chars = sort_char_count(chars)
    for dict in sorted_chars:
        for char, num in dict.items():
            if char.isalpha():
                print(f"The '{char}' character was found {num} times")

def sort_on(dict):
    return list(dict.values())[0]

def sort_char_count(chars):
    char_list = []

    for char, num in chars.items():
        char_list.append({char: num})

    char_list.sort(reverse=True, key=sort_on)

    return char_list

main()
