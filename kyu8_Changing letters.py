def swap(st):
    #your code here
    return "".join([i.upper() if i.lower() in ['a','i','u','e','o'] else i for i in st ])