def maxlist(list):
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return max(list)
    else:
        return max(maxlist(list[len(list)//2:]),maxlist(list[:len(list)//2]))
    
l = [1,2,3,4,5,6,7,8,9,10,11,12,20,14,15,16]
print(maxlist(l))