from pyfiglet import *
import random

def figlet():
    f = Figlet(font = font())
    s = input('Print your text: ')
    print(f.renderText(s))


def font():
    print('Print "1", if you want random font, or print "2", if you want choose font.')
    while True:
        try:
            usr_ans = int(input())
            if usr_ans in [1, 2]:
                if usr_ans == 1:
                    return random.choice(FigletFont.getFonts())
                else:
                    return input()
        except:
            print('Вы ввели неправильные данные!')


figlet()
#print(pyfiglet.FigletFont.getFonts())