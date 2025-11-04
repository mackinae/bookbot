import sys
from stats import count_words, character_count, sort_on, format_dict
book_path = sys.argv[-1]

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    
    text = get_book_text(book_path)
    return text

print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
{count_words(main())}
--------- Character Count -------""")
character_count(main())
for lett in format_dict:
    if lett["letter"].isalpha(): 
        print(f"{lett["letter"]}: {lett["count"]}")
print("============= END ===============")