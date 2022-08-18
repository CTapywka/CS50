def date():
    mounths = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
    }
    s = input().strip()
    date_list = []
    if '/' in s:
        date_list = s.split('/')
        a = date_list[0]
        if len(a) == 1:
            a = '0' + a
        b = date_list[1]
        if len(b) == 1:
            b = '0' + b
        print(f'{date_list[2]}-{a}-{b}')
    else:
        date_list = s.split()
        print(date_list)


date()