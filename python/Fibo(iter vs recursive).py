# 순환방식의 피보나치수열과 반복 방식의 피보나치수열 시간 비교
n = int(input('n > '))

# iter
def fibo_iter(n):
    if 0 <= n < 2: return n # 0 혹은 1일 경우 그대로 리턴
    elif 0 > n: return False # 음수를 입력하면 오류 리턴

    pre_0 = 0
    pre_1 = 1
    
    
    for i in range(2,n+1):

        tmp = pre_0 + pre_1 # 다음번 수를 계산
        pre_0 = pre_1 # n-2번째 수를 n-1번째 수로 갱신
        pre_1 = tmp # n-1번째 수를 새로 구한 수로 갱신
        
    return tmp

# recursive
def fibo(n):
    if 0 <= n < 2: return n # 0 혹은 1일 경우 그대로 리턴
    elif 0 > n: return False # 음수를 입력하면 오류
    else:
        return fibo(n-1) + fibo(n-2)

# 성능의 비교를 위해 시간 측정
import time

## iter
start_iter = time.time()
fibo_i = fibo_iter(n)
end_iter = time.time()
print(f'fibo: {fibo_i}, time: {end_iter - start_iter}')

## recursive
start_re = time.time()
fibo = fibo(n)
end_re = time.time()
print(f'fibo: {fibo}, time: {end_re - start_re}')

## 단순 코드 실행 시간 차이지만 반복의 방식이 순환의 방식보다 빠름
## -> 반복 방식의 시간 복잡도 O(n), 순환 방식의 시간 복잡도 O(2^n)이기 때문에 반복의 방식이 빠름
