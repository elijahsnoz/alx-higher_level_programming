#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
thestring = f"last digit of {number} is {lastdigit}"
if lastdigit > 5:
    print(f"{thestring} and is greater than 5")
elif lastdigit == 0:
    print(f"{thestring} and is 0")
elif lastdigit < 6  and not 0:
    print(f"{thestring} and is less than 6 and not 0")