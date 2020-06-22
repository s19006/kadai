def n_gram(word, y):
    return (word[x: x+y] for x in range(len(word)  - y + 1))

a = "paraparaparadise"
b = "paragraph"
X = set(n_gram(a, 2))
Y = set(n_gram(b, 2))
print(X)
print(Y)
print(X | Y)
print(X & Y)
print(X - Y)
