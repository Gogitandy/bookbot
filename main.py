def main():
    book_path = "books/frakenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(text, count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

main()
