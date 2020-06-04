a = "Hi He Lied Because Boron Cloud Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause Arthur King Can."
b = a.split(" ")
c = [(b[idx - 1][0], idx) for idx in [1, 5, 6, 7, 8, 9, 15, 16, 19]]
d = [(b[idx - 1][:2], idx) for idx in [2, 3, 4, 10, 11, 12, 13, 14, 17, 18, 20]]
cd = {x: y for (x, y) in c + d}
print(cd)

