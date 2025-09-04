def get_strings(city):
    uniq=list(set(city.lower()))
    return ",".join([ uniq[i] + ":" + city.lower().count(uniq[i])*"*" for i in range(len(uniq))])

print(get_strings("Chicago"))