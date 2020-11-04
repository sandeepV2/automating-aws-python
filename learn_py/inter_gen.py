# factors of number

def get_factors(n):
    results = []
    for i in range(1, n+1):
        if n % i == 0:
            results.append(i)

    return results


def get_fact(n):
    for i in range(1, n+1):
        if n % i == 0:
            yield i



print get_factors(10)
print get_fact(10)
