
import random as r
from settings import *


print("""
 ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄
█       █       █       █       █
█    ▄  █   ▄   █▄▄▄▄   █▄▄▄▄   █
█   █▄█ █  █▄█  █▄▄▄▄█  █▄▄▄▄█  █
█    ▄▄▄█       █ ▄▄▄▄▄▄█ ▄▄▄▄▄▄█
█   █   █   ▄   █ █▄▄▄▄▄█ █▄▄▄▄▄
█▄▄▄█   █▄▄█ █▄▄█▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█

made by Kert252
""")

hm = ['settings.lEnabled', 'settings.uEnabled',
'settings.numEnabled', 'settings.symEnabled']


def generate(lh):
    print("\nPasswords generated: ")
    pref = ""
    for j in hm:
        if j == 'settings.lEnabled' and eval(j) == True:
            pref = pref + lower
        if j == 'settings.uEnabled' and eval(j) == True:
            pref = pref + upper
        if j == 'settings.numEnabled' and eval(j) == True:
            pref = pref + num
        if j == 'settings.symEnabled' and eval(j) == True:
            pref = pref + sym
    pref = list(pref)
    for i in range(lh[1]):
        password = []
        r.shuffle(pref)
        for i in range(lh[0]):
            password.append(r.choice(pref))
        r.shuffle(password)
        print("".join(password))


def printOp():
    print(f"""
    1. [Generate passwords]
    2. lowercase = {bool(settings.lEnabled)}
    3. uppercase = {settings.uEnabled}
    4. numbers = {settings.numEnabled}
    5. symbols = {settings.symEnabled}
    """)


def choice():
    while True:
        try:
            choice = int(input("Enter a number: "))
            if choice >= 1 and choice <= 5:
                if choice == 1:
                    check = False
                    for i in hm:
                        if eval(i) == True:
                            check = True
                    if check == True:
                        break
                    else:
                        print("Enable at least 1 option")
                if choice == 2:
                    if bool(settings.lEnabled) == True:
                        settings.lEnabled = False
                        printOp()
                    else:
                        settings.lEnabled = True
                        printOp()
                if choice == 3:
                    if bool(settings.uEnabled) == True:
                        settings.uEnabled = False
                        printOp()
                    else:
                        settings.uEnabled = True
                        printOp()
                if choice == 4:
                    if bool(settings.numEnabled) == True:
                        settings.numEnabled = False
                        printOp()
                    else:
                        settings.numEnabled = True
                        printOp()
                if choice == 5:
                    if bool(settings.symEnabled) == True:
                        settings.symEnabled = False
                        printOp()
                    else:
                        settings.symEnabled = True
                        printOp()
            else:
                print("Please enter a valid number! \n")
        except ValueError:
            print("Please enter a valid integer! \n")


def choice2():
    while True:
        try:
            lenght = int(input("Password lenght: "))
            break
        except ValueError:
            print("Please enter an integer! \n")

    while True:
        try:
            amount = int(input("Amount of passwords: "))
            break
        except ValueError:
            print("Please enter an integer! \n")

    return [lenght, amount]


while True:
    printOp()
    choice()
    print("")
    generate(choice2())
    input("\nHit any key to continue. ")
