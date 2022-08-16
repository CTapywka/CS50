def coke():
    n = 50
    while n > 0:
        print(f'Осталось заплатить {n} центов.')
        insrt = int(input('Вставьте монету. '))
        if insrt in [25, 10, 5]:
            n -= insrt
            print()
        elif insrt not in [25, 10, 5]:
            print('Подходят только монеты номиналом 25, 10 и 5 центов.')
            print()
    if n == 0:
        print('Вот ваша кола!')
    elif n < 0:
        print(f'Вот ваша кола и сдача {abs(n)} центов!')
coke()