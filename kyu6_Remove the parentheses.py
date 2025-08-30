def remove_parentheses(st):
    frst=st.split("(")[0]
    scnd=st.split(")")[-1]
    return frst+scnd

print(remove_parentheses("ing ngarso(suy(sdasd)n)Tulodo"))