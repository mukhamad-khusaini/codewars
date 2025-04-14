def sort_my_string(s):
    return "{} {}".format("".join([s[i] for i in range(len(s)) if i%2==0]),"".join([s[i] for i in range(len(s)) if i%2!=0]))