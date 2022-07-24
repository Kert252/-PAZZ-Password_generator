
import random as r

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

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sym = '*@#%?!$&^'

lenght = int(input("Password lenght: "))
amount = int(input("Amount of passwords: "))


def createPas():
    pas = ""
    for j in range(1, amount+1):
        for i in range(lenght):
            x = r.randint(1, 4)
            if x == 1:
                y = r.choice(lower)
                pas = pas + y
            elif x == 2:
                y = r.choice(upper)
                pas = pas + y
            elif x == 3:
                y = r.choice(num)
                pas = pas + y
            elif x == 4:
                y = r.choice(sym)
                pas = pas + y
        print(f"{j}: {pas}")
        pas = ""


createPas()
