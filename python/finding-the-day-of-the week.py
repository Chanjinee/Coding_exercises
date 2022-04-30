#!/usr/bin/env python
# coding: utf-8

# In[1]:


#날짜 입력받기 & eco checking
year = int(input("year> "))
month = int(input("month> "))
day = int(input("day> "))
print("year = ",year)
print("month = ",month)
print("day = ",day)

#year
year_sum = 0 #변수 initialization
for i in range(1, year): #2021인 경우 아직 지나가지 않았으므로 range는 1년 전까지 
    if (i%4 == 0) and (not(i%100 == 0)) or (i%400 ==0): #윤년 판별
        year_sum += 366#윤년인경우
    else:
        year_sum += 365 #윤년이 아닌 경우

#month
month_sum = 0
    #윤년을 판별하여 2월을 더해줌 
if year % 4 == 0 and year % 400 == 0 and year % 4 != 0: # 윤년확인
    for i in range(1,month):
        if i in (1,3,5,7,8,10,12): #31일까지 있는 달
            month_sum += 31
        elif i in (4,6,9,11): #30일까지 있는 달
            month_sum += 30
        elif i == 2:
            month_sum += 29
else:
    for i in range(1,month):
        if i in (1,3,5,7,8,10,12):
            month_sum += 31
        elif i in (4,6,9,11):
            month_sum += 30
        elif i == 2:
            month_sum += 28
            
#day

#총 날짜수
date_sum = year_sum + month_sum + day


#요일확인
if date_sum % 7 == 0:
    print("{}년 {}월 {}일은 일요일입니다.".format(year, month, day))
elif date_sum % 7 == 1:
    print("{}년 {}월 {}일은 월요일입니다.".format(year, month, day))
elif date_sum % 7 == 2:
    print("{}년 {}월 {}일은 화요일입니다.".format(year, month, day))
elif date_sum % 7 == 3:
    print("{}년 {}월 {}일은 수요일입니다.".format(year, month, day))
elif date_sum % 7 == 4:
    print("{}년 {}월 {}일은 목요일입니다.".format(year, month, day))
elif date_sum % 7 == 5:
    print("{}년 {}월 {}일은 금요일입니다.".format(year, month, day))
elif date_sum % 7 == 6:
    print("{}년 {}월 {}일은 토요일입니다.".format(year, month, day))

