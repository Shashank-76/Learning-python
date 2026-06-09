def rem(l, word):
    n = []
    for item in l:
        n.append(item.replace(word, ""))
    return n

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))