def search_ele(a_list, n, item):

    if n == len(a_list):
        return False

    if item == a_list[n]:
        return True


    return search_ele(a_list, n+1, item)


def search_ele_while(a_list, n, item):

    found = False
    pos = 0
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    return found


def sorted_search(a_list, n, item):
    found = False
    pos = 0
    while pos < n:
        if a_list[pos] == item:
            found = True
        elif a_list[pos] > item:
            break
        pos += 1

    return found

def sorted_s(a_list, n, item):

    if a_list[n] > item or n == len(a_list):
        return False

    if item == a_list[n]:
        return True


    return search_ele(a_list, n+1, item)

def bin_search(a_list, f, r, item):
    mid = (f + r) // 2

    if a_list[mid] == item:
        return mid
    elif  item < a_list[mid]:
        return bin_search(a_list, f, mid-1, item)
    elif item > a_list[mid]:
        return bin_search(a_list, mid+1, r, item)

    return -1


list_array = [1,2,32,8,17,19,42,13,0]
#print search_ele(list_array, 0, 42)
#print search_ele_while(list_array, 0, 17)
print sorted_search(range(70, 100), 30, 56)
print bin_search(range(56, 78), 0, 22, 57)

