def prime(x):
    if(n == 1):
        return 'composite'
    num = 2
    while x > num:
        if x % num == 0:
            return 'composite'
        else:
            num += 1
    return 'prime'
