#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time
 
#리스트 안에 들어갈 정수 원소의 갯수
n = int(input("리스트의 원소 갯수를 입력하세요."))

#원소를 담을 빈 리스트 생성
a = []

#리스트에 추가
for i in range(n):
    num = int(input())
    a.append(num)
    
#시간 비교를 위한 복사본 생성
b = list(a)

#시간 측정 시작
start1 = time.time()  

lena = len(a)

for i in range(lena - 1): #index 1부터 계속 나아감
    for j in range(lena - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    
end1 = time.time()
print("sorted a",a)
print("1) Running Bubble takes %.10f"%(end1 - start1))

#sort
start2 = time.time()
b.sort()
end2 = time.time()
print("1) Running 'sort()' takes %.10f"%(end2 - start2))

