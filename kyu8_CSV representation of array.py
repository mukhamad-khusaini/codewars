def array_to_csv(array):
    return '\n'.join([','.join(map(str, row)) for row in array])
