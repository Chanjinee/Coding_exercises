#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

#n값 받기
n = int(input("n값을 입력하세요."))

#리스트 생성
eratosthenes = list(range(1,n+1))
print("Before: ", eratosthenes)

#소수를 받을 리스트 생성
pList = []

#sqrt(n)이하의 소수를 찾는다
for i in range(2, int(math.sqrt(n))+1):
    vf = 0 #소수판별을 위한 변수 초기화
    for j in range(2, i):
        if i % j == 0:
            vf += 1 #소수인지 확인
    if vf == 0:
        pList.append(i)
#제대로 소수들이 들어갔는지 확인
print("pList: ", pList)

#리스트에서 소수의 배수를 제거
eratosthenes.remove(1) #1 제거
for i in pList:
    for j in eratosthenes:
        if j > i and j % i == 0:
            eratosthenes.remove(j)
            
print("After: ",eratosthenes)

