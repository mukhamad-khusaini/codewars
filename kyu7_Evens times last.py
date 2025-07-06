def even_last(numbers): 
    if not numbers: return 0
    return sum([numbers[i] for i in range(len(numbers)) if i%2==0])*numbers[-1]