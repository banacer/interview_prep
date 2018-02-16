def reverse_int(n):
    if n==0:
        return 0
    num = 0
    positive = True if n>0 else False
    if not positive:
        n*=-1
    while n > 0:
        num*=10
        num+= n%10
        n/10
    if not positive:
        return -1*num
    return num


if '__name__'  == '__main__':
    assert reverse_int(123) == 321
    assert reverse_int(-1000) == -1