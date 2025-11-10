from stats import number_words, number_char

def main():
  file_path = "../bookbot/books/frankenstein.txt"
  file_contents = get_book_text(file_path)

  num_words = number_words(file_contents)
  print(f"Found {num_words} total words")

  num_char = number_char(file_contents)
  print(num_char)


def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

main()
