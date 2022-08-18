def pokupki():
    list = []
    dict = {}
    while True:
        try:
            s = input()
            list.append(s)
            dict[s] = list.count(s)
        except EOFError:
            break
    for key in dict:
        print(dict[key], key.upper())


pokupki()
