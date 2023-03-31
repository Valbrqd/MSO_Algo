def trisel(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                l[i],l[j] = l[j],l[i]
    print(l)


def randomelist(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0,100))
    return l

trisel(randomelist(10))
