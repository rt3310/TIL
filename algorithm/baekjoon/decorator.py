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

def incache(func):
    sentinel = object()
    cache = {}
    def wrapper(*args, **kwargs):
        key = hash(str(args) + str(kwargs))
        result = cache.get(key, sentinel)
        if result is not sentinel:
            return result
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

# tracktime 선언: 실행시간 반환
# tracktime 미선언: 결과값 반환

@tracktime
def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

@tracktime
@incache
def fibo_incache(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibo_incache(n-1) + fibo_incache(n-2)

def test():
    print(fibo(30), '초')
    print(fibo_incache(30), '초')
    print(fibo_incache(1000), '초')
    
# test()
print(fibo(1000) - fibo_incache(1000), '초')