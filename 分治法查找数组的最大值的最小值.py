# -*- coding: utf-8 -*-
"""
Created on Sun May 16 14:02:30 2021

@author: lenovo
"""

import time


def find_max_min(Array,left,right):
    left=int(left)#保证下标为整数
    right=int(right)#保证下标为整数
    if right-left<=1:#求解子问题：当前数组含元素小于等于2,按照大小分类讨论
       if(Array[left]<Array[right]):
           return(Array[left],Array[right])
       else:
           return(Array[right],Array[left])
    else:#划分  
        mid= (left + right) // 2 #求中间下标值，折半划分
        (a,b)=find_max_min(Array,left,mid)#对左子数组调用find_max_min
        (c,d)=find_max_min(Array,mid+1,right)#对右子数组调用find_max_min
        if(a<c):
            if(b<d):
                return (a,d)
            else:
                return (a,b)
        else:
            if(b<d):
                return (c,d)
            else:
                return (c,b)
    


def main():
    #2 3 4 99 6 4 3 78 323 2
    #9 4 2 4 7 56 34 22 89
    #7 2 3 33 28 90 54 0
    print("输入待查找数组：")
    Array=[]
    a=input().split(" ")#对输入的字符串按空格划分为单个字符
    for aa in a:
        Array.append(int(aa))#将单个字符处理后加入数组
    left=0
    right=len(Array)-1
    #初始化初始下标
    time1 = time.perf_counter()#运行前时间
    (MIN,MAX)=find_max_min(Array,left,right)#对待求解数组调用find_max_min
    time2 = time.perf_counter()#运行后时间
    print("MAX = %d"%MAX)
    print("MIN = %d"%MIN)
    #输出结果
    print("程序运行时间：%f"%(time2 - time1))#输出运行耗时
    
    
if __name__ == '__main__':
    main()
