import random
import string

code = []

code.append(random.choice(string.ascii_lowercase))
code.append(random.choice(string.digits))
code.append(random.choice(string.ascii_uppercase))

while len(code) < 6:
    code.append(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits))

s_code = "".join(code)
print(s_code)