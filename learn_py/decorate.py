

def square_num(x):
    return x**2


def sub_1(x):
    return x-1


def handle_str(func):
    
    def convert(x):
        return func(float(x))

    return convert



print sub_1(2)
print square_num(2)

print handle_str(square_num)('2')

@handle_str
def dec_num(x):
    return x * x

print dec_num('3')

