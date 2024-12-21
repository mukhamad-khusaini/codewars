def parse_float(string):
    try:
        return float(string)
    except:
        return None
    
print(parse_float('1.0'))