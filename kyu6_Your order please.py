def order(sentence):
  listed=sentence.split(" ")
  ordered=[]
  res=[]
  for i in range(len(listed)):
    spread=list(listed[i])
    for x in spread:
      if(x.isdigit()==True):
        ordered.append(int(x))

  ordered.sort()
  for i in range(len(ordered)):
    for x in range(len(listed)):
        if(str(ordered[i]) in list(listed[x])):
            res.append(listed[x])
            

  return " ".join(res)


print(order(""))