def equal(a,b):
    return a==b

def is_palindrome(n):
    x = str(n)
    for i in range(len(x)-1):
        if equal(x[i], x[len(x)-i-1]):
            continue
        else:
            return False
    return True

output = filter(is_palindrome, range(1,1000))
print(list(output))

help(filter)