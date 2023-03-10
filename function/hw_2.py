s = {}
def a(b):
    c = b.lower().split(' ')
    for i in c:
        s[i] = c.count(i)
a("Money, money, money, it’s always sunny, in the richmen’s world")
print(s)