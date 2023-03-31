def fibo(n,f0 = 1,f1 = 1):
    if n >0 :
        print(f0)
        fibo(n-1,f1,f0+f1)

def fibo1(n):
    if n<=1:
        return 1
    else:
        return fibo1(n-1)+fibo1(n-2)
    
