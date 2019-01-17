L = [("Rimm",100), ("FengFeng",95), ("Lisi", 87), ("Ubuntu", 111)]

def by_name(n):
    x = sorted(n[0], key=str.lower)
    return x

out = sorted(L, key=by_name)
print(out)

def by_score(n):
    x = sorted(range(n[1]), key=abs)
    return x

o = sorted(L, key=by_score, reverse=True)
print(o)

