# 递归
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# 基础
def fib_(n):
    a, b = 1, 1
    if n == 1 or n == 2:
        return 1
    else:
        i = 3
        while i <= n:
            a, b = b, a+b
            i += 1
        return b
    
for i in range(1,1000):
    print(fib_(i))
#     print(fib(i)) 递归占内存，慢
