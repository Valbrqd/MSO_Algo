def triFusion(l):
    if len(l) == 1:
        return l
    else:
        return fusion(triFusion(l[:len(l)//2]),triFusion(l[len(l)//2:]))
        

def fusion(l1,l2):
    l = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            l.append(l1[0])
            l1.pop(0)
        else:
            l.append(l2[0])
            l2.pop(0)
    if len(l1) > 0:
        l.extend(l1)
    if len(l2) > 0:
        l.extend(l2)
    return l

def randomelist(n):
    import random
    l = []
    for i in range(n):
        l.append(random.randint(0,100))
    return l

print(triFusion(randomelist(10)))