def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i%2==0]