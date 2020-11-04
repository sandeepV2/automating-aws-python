# Object evaluating to false.

class Myclass:
    def __bool__(self):
        return False
    def __len__(self):
        return 0

obj = Myclass()
print obj
if obj:
    print 'sfsdf'



#Any : Any of the element in the list evaluates to true
#All : All of the elements in the list evaluates to true
