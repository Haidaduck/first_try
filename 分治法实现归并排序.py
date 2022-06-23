# -*- coding: utf-8 -*-
"""
Created on Sun May 16 15:29:46 2021

@author: lenovo
"""

import time
import sys

MAX=sys.maxsize

def Merge(Array,left,mid,right):#对排序后的子数组结果进行合并
    global MAX
    m=mid-left+1#计算左子数组的长度
    n=right-mid#计算右子数组的长度
    L=[0 for x in range(0,m+2)]#创建长度为m+1的数组L
    R=[0 for x in range(0,n+2)]#创建长度为n+1的数组R
    #数组额外的位置保存哨兵
    for i in range(1,m+1):#将数组Array[left..mid]复制到L[1..m]
        L[i]=Array[left+i-1]
    for j in range(1,n+1):#将数组Array[mid+1..right]复制到R[1..m]
        R[j]=Array[mid+j]
    L[m+1]=MAX
    R[n+1]=MAX
#将哨兵放在末尾，哨兵值设置为整型数最大值
    i=1
    j=1
    for k in range(left,right+1):
        #对子数组Array按照从小到大的顺序包含L[1..m+1]和R[1..n+1]中的k-left个最小元素
        if(L[i]<=R[j]):#L[i]和R[j]是各自数组中未被复制回数组A的最小元素
            Array[k]=L[i]
            i=i+1
        else:
            Array[k]=R[j]
            j=j+1
        
def MergeSort(Array,left,right):
    if(left<right):#递归结束条件为left=right，即单个元素有序，否则继续分治
        mid=(left + right) // 2#求中间下标值，折半划分
        MergeSort(Array,left,mid)#对左子数组调用自身
        MergeSort(Array,mid+1,right)#对右子数组调用自身
        Merge(Array,left,mid,right)#对两个子数组结果进行合并

def main():
    #2 3 4 99 6 4 3 78 323 2
    #9 4 2 4 7 56 34 22 89
    #7 2 3 33 28 90 54 0
    print("输入待排序数组：")
    Array=[]
    a=input().split(" ")
    for aa in a:
        Array.append(int(aa))
    left=0
    right=len(Array)-1
    time1 = time.time()
    MergeSort(Array,left,right)
    print("排序后的数组为：")
    print(Array)
    time2= time.time()
    print("程序运行时间：%f"%(time2 - time1))
    print(MAX)
    
if __name__ == '__main__':
    main()

    