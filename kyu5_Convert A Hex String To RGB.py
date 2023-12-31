def hex_string_to_RGB(h): 
    r = int(h[1:3], 16)
    g = int(h[3:5], 16)
    b = int(h[5:7], 16)

    return {
        "r": r,
        "g": g,
        "b": b
    }

print(hex_string_to_RGB("#FF9933"))
