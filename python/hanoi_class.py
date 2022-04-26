#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Hanoi:
    def __init__(self, n):
        self.n = n
        print("self.n = ", self.n)
        
    def hanoi(self, n, start, mid, end):
        if n==1:
            print("%d : %c -> %c" %(n, start, end))
        else:
            self.hanoi(n-1, start, end, mid)
            print("%d : %c -> %c" %(n, start, end))
            self.hanoi(n-1, mid, start, end)
        
        
class Main:
    def __init__(self, n):
        self.n = n
        
    def main(self):
        hanoiA = Hanoi(self.n)
        hanoiA.hanoi(self.n,"A", "B", "C")
        
#main
n = int(input("N : "))
m = Main(n)
m.main()

