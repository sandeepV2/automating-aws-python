# Use transform functions like filter, map, sorted

tt = range(10)

filt = lambda x : x % 2 == 0

print filter(filt, tt)

print map(filt, tt)

print sorted(tt)
