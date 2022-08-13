users_ans = input()
if 'hello' in users_ans.lower():
    print('$0')
elif users_ans.lower()[0] == 'h':
    print('$20')
else:
    print('$100')