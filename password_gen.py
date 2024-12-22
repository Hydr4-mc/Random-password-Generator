import random
import string

size_of_pasword = 10
posible_digits = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*" + "?"

print("".join(random.choices(posible_digits, k=size_of_pasword)))