def ensure_question(s):
    if s=="":return "?"
    return s if s[len(s)-1]=="?" else s+"?"