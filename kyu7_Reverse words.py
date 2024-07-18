def reverse_words(text):
  return " ".join([i[::-1] for i in text.split(" ")])

print(reverse_words("This is"))