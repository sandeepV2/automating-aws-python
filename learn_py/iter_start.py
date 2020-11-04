# use iterator functions like enumerator, zip, iter, next


days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

i = iter(days)
print i.next()

# use sentinal to stop the iter function

# example to iter lines in the file

with open('test.txt', 'r') as fp:
    for line in iter(fp.readline, 'stop\n'):
        print line



# implement enumerate function.

