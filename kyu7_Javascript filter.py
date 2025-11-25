def search_names(logins):
    return list(filter(lambda a: a[0].__contains__("_") or a[1].__contains__("_"),logins))

print(search_names([[ "foobar_", "foo@foo.com" ], [ "bar", "bar@bar.com" ] ]))