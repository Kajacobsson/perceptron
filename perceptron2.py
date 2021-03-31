import random
import sys

w1 = random.random()
w2 = random.random()

t = 1.0

def increase_weight():
    global w1, w2
    if x1 == 1:
        w1 = w1 + 0.2
    elif x2 == 1:
        w2 = w2 + 0.2
    elif x1 == 1 and x2 == 1:
        w1 = w1 + 0.2
        w2 = w2 + 0.2

def decrease_weight():
    global w1, w2
    if x1 == 1:
        w1 = w1 - 0.2
    elif x2 == 1:
        w2 = w2 - 0.2
    elif x1 == 1 and x2 == 1:
        w1 = w1 - 0.2
        w2 = w2 - 0.2


while True:
    x1 = input("Does it have four legs? (yes/no)")
    x2 = input("Is it green? (yes/no)")

    x1 = x1.lower()
    x2 = x2.lower()

    if x1 == "yes":
        x1 = 1
    else:
        x1 = 0

    if x2 == "yes":
        x2 = 1
    else:
        x2 = 0

    var1 = (x1 * w1)
    var2 = (x2 * w2)

    if (var1 + var2) <= t:
        print("Fly inte")
    if (var1 + var2) > t:
        print("Fly")

    fix = input("Was this the correct output? (yes/no)")

    fix = fix.lower()

    if fix == "yes":
        stop = input("Exit the program? (yes/no)")
        stop = stop.lower()
        if stop == "yes":
            sys.exit()
        else:
            continue
    else:
        if x1 == 1 or x2 == 1:
            increase_weight()
        else:
            decrease_weight()