import random
import string

size_of_pasword = int(input("how long do you want the password?"))
posible_digits = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*" + "?"

print("".join(random.choices(posible_digits, k=size_of_pasword)))
useless=str(input())
