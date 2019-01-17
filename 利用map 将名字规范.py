def Name_rule(in_put):
    x = in_put.lower()
    x = x.capitalize()
    print(x)
    return x

list(map(Name_rule, (["RIMPEDDO", "REPKER", "FengFeng"])))


