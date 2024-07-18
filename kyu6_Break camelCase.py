def solution(s):
    l=[i.isupper() for i in s]
    d=[f' {s[i]}' if s[i].isupper() else s[i] for i in range(len(l))]
    return ''.join(d)

print(solution("hanyaOrangOrangYangBerimanSaja"))

# Alternative
# def solution(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)