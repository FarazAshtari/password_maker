import random
print('''
==================
Password Generator
==================
 ''')

chars = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,123456789')

number = int(input('How many password ???'))
length = int(input('How many chars ???'))

print('this is your password :')

for psw in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)

print(password)


