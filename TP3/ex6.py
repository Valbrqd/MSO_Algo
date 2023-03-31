def dicho(lsti,lst,n):
    if len(lst) == 1 and lst[0] != n:
        return -1
    if lst[len(lst)//2] == n:
        print(lsti.index(n))
    elif lst[len(lst)//2] > n:
        dicho(lsti,lst[:len(lst)//2],n)
    elif lst[len(lst)//2] < n:
        dicho(lsti,lst[len(lst)//2:],n)


def randomelist(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0,100))
    return l

l = randomelist(100)
l.sort()

dicho(l,l,21)