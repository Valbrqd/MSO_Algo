def triRapide(l):
    if len(l) == 1:
        return l
    else:
        pivot = l[len(l)//2]
        l1 = []
        l2 = []
        for i in l:
            if i < pivot:
                l1.append(i)
            elif i > pivot:
                l2.append(i)
        return triRapide(l1) + [pivot] + triRapide(l2)
    
def randomelist(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0,100))
    return l

print(triRapide(randomelist(10)))