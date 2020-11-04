
test_dict = {}


list_p = [0, 1, 0, 1, 2, 4, 6, 0]


for p in list_p:
    p = str(p)
    if p in test_dict.keys():
        test_dict[p] += 1
    else:
        test_dict[p] = 1

print test_dict

# use of default dict to intialize with default value.

from collections import defaultdict


num_d = defaultdict(int)

print num_d
for p in list_p:
    p = str(p)
    num_d[p] += 1

print num_d


from collections import Counter


c1 = Counter(map(str, list_p))

print c1['0']
print sum(c1.values())
print len(list_p)



