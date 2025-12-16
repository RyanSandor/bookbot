from stats import get_num_words
from stats import get_num_char
from stats import chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    path_to_book = sys.argv[1]
    text = get_book_text(path_to_book)
    num_words = get_num_words(text)
    dic = get_num_char(text)
    sorted_dict = chars_dict_to_sorted_list(dic)
    print_report(path_to_book, num_words, sorted_dict)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()