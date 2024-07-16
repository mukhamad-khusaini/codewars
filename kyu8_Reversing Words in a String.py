def reverse(st):
    # Your Code Here
    return " ".join([i for i in st.split(" ") if i != ""][::-1])

print(reverse("Hello  world!"))