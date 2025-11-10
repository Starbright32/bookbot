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

def sort_on(number_of_characters):
  return number_of_characters["num"]

def sorted_list(number_of_characters):
  result = []
  for char, count in number_of_characters.items():
    if not char.isalpha(): 
      continue
    result.append({"char": char, "num": count})

  result.sort(reverse=True, key=sort_on)
  return result 
