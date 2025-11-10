"""
This function takes a filepath as input and 
returns the contents of the file as a string 
"""
def get_book_text(file_path):

  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def number_words(file_contents):

  list_of_words = file_contents.split()
  num_words = len(list_of_words) 

  print(f"Found {num_words} total words")

"""
Prints the entire contents of the book to the console 
"""
def main():
  file_path = "../bookbot/books/frankenstein.txt"

  file_contents = get_book_text(file_path)
  number_words(file_contents)
  

main()
