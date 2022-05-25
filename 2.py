def beegeek(n, k):
    s = ''
    for i in range(n, k+1):
        a, b = i%3==0, i%7==0
        if a and b:
            s += 'BeeGeek '
        elif a:
            s += 'Bee '
        elif b:
            s += 'Geek '
        else:
            s += str(i)+' '
    return s

