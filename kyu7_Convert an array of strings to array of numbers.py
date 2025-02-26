def to_float_array(arr): 
    try:
        return [int(i) for i in arr]
    except:
        return [float(i) for i in arr]