def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    return text

def count_words(book_text):
    word_count = len(book_text.split())
    print(f"Found {word_count} total words")


count_words(main())