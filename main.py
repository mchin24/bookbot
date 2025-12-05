import sys
from stats import count_words, character_usage, get_sorted_usage

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    report = get_sorted_usage(character_usage(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in report:
        if not item["char"].isalpha():
            continue
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

    print("============= END ===============")

main()