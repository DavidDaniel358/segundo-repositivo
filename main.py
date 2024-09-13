import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

longitud = int(input("Cual sera la longitud de la contrasena?"))

password = ""

for i in range(longitud):

    password += random.choice(caracteres)

print(password)
