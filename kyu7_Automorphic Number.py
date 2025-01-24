def automorphic(n):
    return 'Automorphic' if str(n) == str(n*n)[-len(str(n)):] else "Not!!"

print("12345"[-2:])