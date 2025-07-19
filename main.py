from stats import get_num_words, get_char_occurences, get_sorted_list_char_occurences
import sys


def main():
  if len(sys.argv) < 2:
    print("error, not enough arguments have been passed in")
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  text = get_book_text(book_path)
  num_words = get_num_words(text)

  char_occurrences = get_char_occurences(text)
  sorted_list = get_sorted_list_char_occurences(char_occurrences)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for entry in sorted_list:
    char = entry["char"]
    count = entry["count"]
    if char.isalpha():
      print(f"{char}: {count}")

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()
