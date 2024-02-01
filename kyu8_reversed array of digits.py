def digitize(n):
    d = [int(i) for i in list(str(n))]
    d.reverse()
    return d

print(digitize(634561))

# Alternative
# def digitize(n):
#     return [int(x) for x in str(n)[::-1]]