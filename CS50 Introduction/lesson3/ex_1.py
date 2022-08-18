while True:
    try:
        x = int(input())
        y = int(input())
        result = x / y
    except ValueError:
        print('Введите корректные числа')
    except ZeroDivisionError:
        print('Вы ввели ноль')
    else:
        result = int(result * 100)
        if result > 100:
            print('Введите корректные числа')
        if result <= 1:
            print('E')
            break
        if 100 >= result >= 99:
            print('F')
            break
        if 1 < result < 99:
            print(f'{result}%')
            break