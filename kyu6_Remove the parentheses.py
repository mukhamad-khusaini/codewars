def remove_parentheses(st):
    result=[]
    content=st.split("(")
    while content:
        result.append(content[0])
        content.pop(0)
        print(content)

# print(remove_parentheses("in(g) ngarso(suy(sdasd)n)Tulodo"))