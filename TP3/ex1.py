def Dcroiss(n):
    if n > 0:
        print(n)
        Dcroiss(n-1)

Dcroiss(5)

print("=====")
def croiss(n):
    if n > 0:
        croiss(n-1)
        print(n)

croiss(5)