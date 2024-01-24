def alphabet_position(text):
    return " ".join([str([chr(i) for i in range(97,123)].index(i)+1) for i in text.lower() if i in [chr(i) for i in range(97,123)]])

print(alphabet_position('Kamu Adalah Harapan Bangsa.'))


# Alternative
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())