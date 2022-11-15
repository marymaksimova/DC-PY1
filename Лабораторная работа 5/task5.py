import random
import string


from random import sample
def get_random_password(length = 8) -> str:
    letters = (string.ascii_lowercase + string.ascii_uppercase + string.digits)
    password = ''
    d = random.sample(letters , 8)
    password += "".join(d)
    return password
print(get_random_password())