a = "Hi He Lied Because Boron Cloud Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause Arthur King Can."

y = [1, 5, 6, 7, 8, 9, 15, 16, 19]
b = a.split(" ")
c = {}
for d, word in enumerate(b):
    if d + 1 in y:
        c[d + 1] = word[0]
    else:
        c[d + 1] = word[:2]
print(c)

