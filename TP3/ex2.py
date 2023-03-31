def syracuse(n,lst=[[]]):
    lst[0].append(n)
    if n > 1:
        if not n % 2:
            syracuse(n//2,lst)
        else:
            syracuse(3*n+1,lst)
    else :
        lst.append(lst[0].index(1)+1)
        lst.append(max(lst[0]))

    return lst

n = 13

print(syracuse(n))