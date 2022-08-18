from inflect import *

names = []


def main():
    people()
    print('Adieu, adieu, to', end = ' ')
    if len(names) > 2:
        for i in range(len(names)-2):
            print(names[i] + ', ')
        print(names[-2] + ' and ' + names[-1])
    if len(names) == 2:
        print(names[0] + ' and ' + names[1])
    if len(names) == 1:
        print(names[0])



def people():
    while True:
        try:
            s = input()
            names.append(s)
        except:
            break


main()