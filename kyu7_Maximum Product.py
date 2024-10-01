def adjacent_element_product(array):
    return max([array[i]*array[i+1] for i in range(len(array)) if i!=len(array)-1])


print(adjacent_element_product([1, 0, 1, 0, 1000]))