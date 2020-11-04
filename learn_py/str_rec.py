

def print_sub(str_, cur, index):

    if index == len(str_):
        print repr(cur,)
        return

    print_sub(str_, cur, index+1)
    print_sub(str_, cur+str_[index], index+1)



print_sub("ABC", "", 0)



def sum_sub(set_, sum_, subset, index):

    if sum_ == sum(subset):
        print subset

    if index == len(set_):
        return 0

    sum_sub(set_, sum_, subset, index+1)
    sum_sub(set_, sum_, subset + [set_[index]], index+1)


def rev_num(num):


sum_sub([10, 20, 35], 25, [], 0)
