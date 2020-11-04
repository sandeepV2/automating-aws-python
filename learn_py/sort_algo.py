
def bubble_sort(a_list):
    """
    On every pass, maximum element is moved to the last position.
    It is like largest bubble floating on top.
    """
    count = 0
    for pass_num in range(len(a_list)-1, 0, -1):
        for j in range(pass_num):
            if a_list[j] > a_list[j+1]:
                a_list[j],a_list[j+1]=a_list[j+1],a_list[j]
        if count == 3:
            return a_list
        count += 1

    return a_list


def selection_sort(a):
    """
    Selects maximum position and swaps to last.
    number of exchanges are reduced compare to bubble sort.
    """
    for fill_slot in range(len(a)-1, 0, -1):
        max_pos = 0
        for i in range(1, fill_slot+1):
            if a[i] > a[max_pos]:
                max_pos = i

        a[max_pos],a[fill_slot]=a[fill_slot],a[max_pos]

    return a


def merge_sort(a):

    if len(a) > 1:
        mid = len(a)//2
        left_half = a[:mid]
        right_half = a[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a[k] = left_half[i]
                i += 1
            else:
                a[k] = right_half[j]
                j += 1

            k += 1

        while i < len(left_half):
            a[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a[k] = right_half[j]
            j += 1
            k += 1

    print "Merging", a


def quick_sort(a_list, first, last):
    """
    Deos Devide and conquere same as merge sort
    but without using the space.
    """
    split_point = partion(a_list, first, last)

    quick_sort(a_list, first, split_point -1)     
    quick_sort(a_list, split_point +1, last)

def partion(a_list, first, last):

    pivote = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark < right_mark and a_list[left_mark] <= pivote:
            left_mark += 1

        while right_mark > left_mark and a_list[right_mark] >= pivote:
            right_mark -= 1
        if right_mark > left_mark:
            done = True
        else:
            # Exchange until lesser elements are left and larger elements
            # are to the right. 
            a_list[left_mark],a_list[right_mark] = a_list[right_mark],a_list[left_mark]

    # Exchange the pivote with right_mark.
    a_list[first],a_list[right_mark]=a_list[right_mark],a_list[first]

    return right_mark

tt = range(10)
tt.reverse()
print tt
#print bubble_sort(tt)
#print selection_sort(tt)
#print merge_sort(tt)
tt = [5, 8, 2, 3, 7]
print quick_sort(tt, 0, len(tt)-1)
