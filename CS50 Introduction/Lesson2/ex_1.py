def camelcase():
    usr_input = input()
    for i in range(len(usr_input)):
        if usr_input[i].isupper():
            usr_input = usr_input.replace(usr_input[i], '_' + usr_input[i].lower())
    print(usr_input)


camelcase()