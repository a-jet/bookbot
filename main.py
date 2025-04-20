from stats import get_word_count, get_sorted_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def main():

    import sys
    args = sys.argv
    if not len(args) == 2:
        print("Usage: python3 main.py <path_to_book>")
    path = args[1]

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    content=get_book_text(path)
    print(f"Found {get_word_count(content)} total words")
    print("--------- Character Count -------")
    s_char_count = get_sorted_char_count(content)
    for entry in s_char_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["count"]}")

main()