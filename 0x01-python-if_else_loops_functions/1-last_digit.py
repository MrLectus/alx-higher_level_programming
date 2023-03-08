#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
check = abs(number) % 10
if number < 0:
    check *= -1

if check > 5:
    print(f"Last digit of {number} is {check} and is greater than 5")
elif check % 10 == 0:
    print(f"Last digit of {number} is {check} and is 0")
else:
    print(
        f"Last digit of {number} is {check} and is\
 less than 6 and not 0"
    )
