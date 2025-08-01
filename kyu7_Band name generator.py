def band_name_generator(name):
    return f"The {name[0].upper()}{name[1:]}" if name[0]!=name[-1] else f"{name[0].upper()}{name[1:]}{name[1:]}"

print(band_name_generator("knife"))