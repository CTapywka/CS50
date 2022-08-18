import random

gue_num = random.randint(1, 100)


def game():
    print('Print digit between 1 and 100!')
    while True:
        try:
            usr_ans = int(input())
            while usr_ans != gue_num:
                if usr_ans < gue_num:
                    print('Too small!')
                    usr_ans = int(input())
                elif usr_ans > gue_num:
                    print('Too large!')
                    usr_ans = int(input())
            print('Right!')
            break
        except:
            print('Print correct digit!')


game()