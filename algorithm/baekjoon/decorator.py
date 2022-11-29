import time
import sys

# 재귀 depth 제한 변경
sys.setrecursionlimit(10000)

def tracktime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper

@tracktime
def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

def test():
    print(fibo(30), '초')
    
test()