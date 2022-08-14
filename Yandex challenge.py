from collections import Counter

unique_w = set()
count_e = set()
all_e = []

T = int(input("Количество переговорок: "))
for i in range(T):
    s = input()
    for j in range(len(s)-3):
        w = s[j] + s[j+1] + s[j+2]
        w1 = s[j+1] + s[j+2] + s[j+3]
        e = s[j] + s[j+1] + s[j+2] + s[j+3]
        all_e.append(e[:3] + ' ' + e[1:])
        unique_w.add(w)
        unique_w.add(w1)
        count_e.add(w + ' ' + w1)
print(len(unique_w))
print(len(count_e))

counter = Counter(all_e)
for i in counter:
    print(i, counter[i])




