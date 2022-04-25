# 팩토리얼
n = int(input('n> '))


# iter
def factorial_iter(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    return fac

# recursive
def factorial_recursive(n):
    if 0 <= n <= 1 : return n
    elif n < 0: return False
    else:
        return n * factorial_recursive(n-1)

# 성능의 비교를 위해 시간 측정
import time

## iter
start_iter = time.time()
fibo_i = factorial_iter(n)
end_iter = time.time()
print(f'!: {fibo_i}, time: {end_iter - start_iter}')

## recursive
start_re = time.time()
fibo = factorial_recursive(n)
end_re = time.time()
print(f'!: {fibo}, time: {end_re - start_re}')

## -> 반복 방식의 시간 복잡도 O(n), 순환 방식의 시간 복잡도 O(n)이기 때문에 동일할 것으로 판단됨
