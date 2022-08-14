a,b = input().strip().split(':')
usr_time = float(a + '.' + b)
if 7.00 <= usr_time <= 8.00:
    print('breakfast time')
if 12.00 <= usr_time <= 13.00:
    print('lunch time')
if 18.00 <= usr_time <= 19.00:
    print('dinner time')