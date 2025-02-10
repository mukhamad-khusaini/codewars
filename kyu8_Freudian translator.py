def to_freud(sentence):
  if(not sentence): return ""
  return " ".join(['sex' for i in sentence.split(" ")])