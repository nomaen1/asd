def a(w):
    b1 = list(w)
    b2 = set(w)
    if len(b1) == len(b2):
        return False
    return True
print(a("азиза"))