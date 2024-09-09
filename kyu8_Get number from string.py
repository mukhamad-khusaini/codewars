def get_number_from_string(st):
    return int("".join([i for i in st if i.isnumeric()]))