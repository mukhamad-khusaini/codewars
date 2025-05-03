def html_special_chars(data): 
    chr={
        "<": "&lt;",
        ">": "&gt;",
        "\"": "&quot;",
        "&": "&amp;"
    }

    return "".join([i if i not in chr else chr[i] for i in data])

print(html_special_chars("<h2>Hello World</h2>"))