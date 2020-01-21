from math import ceil, floor


def karatsubaFun(x, y):
    # base case if less than 2 digit return simple mutiplication
    if x < 10 and y < 10:
        return x * y

    # calculate te size of numbers.
    m = min(len(str(x)), len(str(y)))
    m2 = ceil(m / 2)
    # m2 = floor(m / 2)

    # split digit sequences in middle.
    high1 = floor(x / (10 ** m2))
    low1 = x % (10 ** m2)

    high2 = floor(y / (10 ** m2))
    low2 = y % (10 ** m2)

    # recursive step
    z0 = karatsubaFun(high1, high2)
    z1 = karatsubaFun(low1, low2)
    z2 = karatsubaFun((low1 + high1), (low2 + high2)) - z0 - z1

    return z0 * (10 ** (m2 * 2)) + z2 * (10 ** m2) + z1


a = 31415926535897932384626433832795789
b = 31415926535897932384626433832795789
print('a * b=', karatsubaFun(b, a))
print('a * b=', a * b)
if karatsubaFun(b, a)==a*b:
    print('same')
