def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_occurences(text):
  occurence_dict = {}
  for c in text:
    char = c.lower()
    if char in occurence_dict:
      occurence_dict[char] += 1
    else:
      occurence_dict[char] = 1
  return occurence_dict

def sort_on(items):
  return items["count"]

def get_sorted_list_char_occurences(occurence_dict):
  char_occurences = []
  for char, count in occurence_dict.items():
    char_occurences.append({"char": char, "count": count})
  char_occurences.sort(reverse=True, key=sort_on)
  return char_occurences
