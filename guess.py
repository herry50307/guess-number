# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:05:05 2021

@author: DSC Handsome
"""

import random
start = int(input("請輸入起始值: "))
end = int(input("請輸入結束值: "))
r=random.randint(start,end)

count=0
while True:
    num=int(input("請輸入數字: "))
    count+=1
    if r==num:
        print("恭喜猜中")
        print("這是你猜的第",count,"次")
        break
    elif r>num:
        print("你猜的比正確答案小")
    elif r<num:
        print("你猜的比正確答案大")
    else:
            print("這是你猜的第",count,"次")