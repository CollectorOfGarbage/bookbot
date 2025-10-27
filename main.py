from stats import word_count, char_count, dict_to_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def sort_on(items):
    return items[1]


def main():
    # print(get_book_text("./books/frankenstein.txt"))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        total_count = word_count(get_book_text(path))
        print(f"Found {total_count} total words")
        print("--------- Character Count -------")
        c_count = char_count(get_book_text(path))
        #print(c_count)
        #a = [c_count]
        #a.sort(key=sort_on)
        a = dict_to_list(c_count)
        for item in a:
            if item["char"].isalpha():
                print(f'{item["char"]}: {item["num"]}')


main()
