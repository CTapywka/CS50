usr_expr = input().strip()
x, y, z = usr_expr.split(' ')
if y == '+':
    ans = float(x) + float(z)
    print(round(ans,1))
if y == '-':
    ans = float(x) - float(z)
    print(round(ans, 1))
if y == '*':
    ans = float(x) * float(z)
    print(round(ans, 1))
if y == '/' and z != 0:
    ans = float(x) / float(z)
    print(round(ans, 1))
