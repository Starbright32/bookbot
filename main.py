from stats import number_words, number_char, sorted_list
import sys 

def main():
  #file_path = "books/frankenstein.txt"


  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  elif len(sys.argv) == 2:
    file_path = sys.argv[1]

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  file_contents = get_book_text(file_path)

  num_words = number_words(file_contents)
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")

  num_char = number_char(file_contents)
  print("--------- Character Count -------")
  result = sorted_list(num_char)
  for item in result:
    if item["char"].isalpha() == False:
      break
    print(f"{item["char"]}: {item["num"]}")


  print("============= END ===============")


def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

main()
