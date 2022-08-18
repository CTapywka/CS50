import random

def main():
    n = get_level()
    score = 0
    err = 0
    for i in range(10):
        try:
            qw, ans = generate_integer(n)
            print(qw, end = ' ')
            usr_ans = int(input())
            if usr_ans == ans:
                score += 1
                print('Right!')
            else:
                err += 1
                print('EEE!')
        except:
            print('Print correct digit!')
    print(f'Your score is {score} / 10.')




def get_level():
    while True:
        try:
            lvl = int(input('Choose level(1, 2 or 3): '))
            if 1 <= lvl <= 3:
                return lvl
            else:
                print('You print incorrect digit!')
        except:
            print('You print incorrect digit!')


def generate_integer(level):
    if level == 1:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        s = a + b
    if level == 2:
        a = random.randint(10, 99)
        b = random.randint(10, 99)
        s = a + b
    if level == 3:
        a = random.randint(100, 999)
        b = random.randint(100, 999)
        s = a + b

    return (f'{a} + {b} = ', s)


if __name__ == "__main__":
    main()