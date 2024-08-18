def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    print(text, count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()
