import random, string

s = ''.join(random.choice(string.ascii_letters) for x in range(10))
print(s)