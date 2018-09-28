import random
import string

x = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
print(x)
