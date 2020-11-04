
a = [33,22,33, 11, 5]

max_ = a[0]

for i in range(1, len(a)):
    if a[i]  > max_:
        sec_ = max_
        max_ = a[i]

print max_, sec_

a = map(lambda x:x*10, range(9))

for i in range(len(a)):
    flag = True
    for j in range(len(a)):
        if a[j] > a[i]:
            flag = False
            break
    if flag:
        max_ = a[i]

print max_

