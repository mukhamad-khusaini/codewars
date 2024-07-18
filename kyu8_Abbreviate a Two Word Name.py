def abbrev_name(name):
    return '.'.join([i[0].upper() for i in name.split(" ")])

print(abbrev_name("ahmad zahroni"))