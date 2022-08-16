def twtrr():
    s = input()
    alp = 'AEIOUaeiou'
    for i in range(len(alp)):
        if alp[i] in s:
            s = s.replace(alp[i],'')
    print(s)


twtrr()