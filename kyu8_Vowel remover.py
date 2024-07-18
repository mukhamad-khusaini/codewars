def shortcut( s ):
    arr=['a','i','u','e','o']
    return "".join([i if i not in arr else "" for i in s])