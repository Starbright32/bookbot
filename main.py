def main():
  file_path = "../bookbot/books/frankenstein.txt"
  file_contents = get_book_text(file_path)
  num_words = number_words(file_contents)
  print(f"Found {num_words} total words")

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def number_words(file_contents):
  list_of_words = file_contents.split()
  return len(list_of_words)

main()
