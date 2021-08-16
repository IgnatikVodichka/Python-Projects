

def remove_duplicate_words(s):
    b = " ".join(sorted(set(s.split()), key=s.index))
    return b


print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
print(remove_duplicate_words("my cat is my cat fat"))
