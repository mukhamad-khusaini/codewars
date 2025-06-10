def filter_lucky(lst):
    return [i for i in lst if "7" in str(i)]


print(filter_lucky([1,2,3,4,5,7,8,9,0,7,57,7,4,778]))