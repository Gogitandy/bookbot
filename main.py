def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_character_count(text)
    print(char_count)

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

main()
