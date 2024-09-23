def switcheroo(s):
    return ''.join(['b' if i=="a" else 'a' if i=="b" else i for i in s ])