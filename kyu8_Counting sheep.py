def count_sheeps(sheep):
  return len([i for i in sheep if i==True])


print(count_sheeps([True,False]))