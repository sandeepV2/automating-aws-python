tt = range(10)


ele = 1


def rec_search(arr, start, end, ele):

    if end < start:
        return False

    if arr[start] == ele:
        return True

    if arr[end] == ele:
        return True

    return rec_search(arr, start + 1, end -1, ele)


print rec_search(tt, 0, 9, ele)


def is_pali(str_, s, e):

    if e < s:
        return False

    if str_[s] != str_[e]:
        return False

    is_pali(str_, s+1, e-1)

    return True

print is_pali('gadag', 0, 4)



def powerSet(str_,  idx, cur):

    n = len(str_)

    if idx == n:
        print cur
        return


    powerSet(str_, idx + 1, cur + str_[idx])
    powerSet(str_, idx +1, cur)


print powerSet('abcd', 0, "")

