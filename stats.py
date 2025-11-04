letter_count = {}
format_dict = []
def count_words(book_text):
    word_count = len(book_text.split())
    return f"Found {word_count} total words"



def sort_on(letters):
    return letters["count"]


def character_count(book_text):
    book = book_text.lower()
    letters = list(book)
    for letter in letters:
        try:
           letter_count[letter] += 1
        except KeyError:
            letter_count[letter] = 1
    for lett in letter_count:
        new_dict = {"letter": lett, "count": letter_count[lett]}
        format_dict.append(new_dict)
        format_dict.sort(reverse=True,key=sort_on)
    return format_dict