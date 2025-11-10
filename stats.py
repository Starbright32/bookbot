def number_words(file_contents):
  list_of_words = file_contents.split()
  return len(list_of_words)

def number_char(file_contents):
  # Convert to lowercase 
  lowercase_words = file_contents.lower()
  # Empty dicitionary 
  number_of_characters = {}
  
  # Iterate through string of words 
  for char in lowercase_words:
    if char not in number_of_characters:
      number_of_characters[char] = 1 
    elif char in number_of_characters:
      number_of_characters[char] += 1
  
  return number_of_characters