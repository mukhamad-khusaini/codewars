def name_value(my_list):
  return [sum([sum([ord(s)-96 for s in x]) for x in my_list[i].split(" ")])*(i+1) for i in range(len(my_list))]

print(name_value(["abc","abc abc"]))