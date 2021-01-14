import random

print("Simple Dice Rolling Game")

ans = input('Do you want to roll a die?(y/n): ')

while ans == 'y':
    n = random.randint(1, 6)
    print(n)

    ans = input('Would you like to role the dice again?(y/n): ')