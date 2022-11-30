#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = number % 10
if (number < 0):
    lastDig = -((-number) % 10)
print(f"Last digit of {number} is {lastDig}", end=" ")
if (lastDig > 5):
    print("and is greater than 5")
elif (lastDig == 0):
    print("and is 0")
else:
    print("and is less than 6 and not 0")
