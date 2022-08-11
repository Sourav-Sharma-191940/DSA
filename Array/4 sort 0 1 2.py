# def color(nums):
#     for i in range(0, len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]>nums[j]:
#                 nums[i],nums[j]=nums[j],nums[i]
            
# nums=list(map(int,input("Enter array: ").split()))
# color(nums)
# print(nums)
#time complexity= O(N^2)
#space complexity=O(1)

def count(arr, n):
    count0=0
    count1=0
    count2=0
    for i in range(0, len(arr)):
        if arr[i]==0:
            count0=count0+1
        if arr[i]==1:
            count1=count1+1   
        if arr[i]==2:
            count2=count2+1

    for i in range(0,count0):
        arr[i] = 0

    for i in range( count0, (count0 + count1)) :
        arr[i] = 1

    for i in range((count0 + count1),len(arr)) :
        arr[i] = 2
    
    result=[]
    for i in range(count0):
        result.append(0)
    for i in range(count1):
        result.append(1)
    for i in range(count2):
        result.append(2)
    return result
    

def printArray(arr, n):
 
    for i in range(0,n):
        print( arr[i] , end=" ")
    print()
    
    
arr = list(map(int, input().split()))
n = len(arr)
count(arr, n)
printArray(arr, n)

#time complexity= O(N)
#space complexity=O(N) & O(1)

# 3)Using dutch flag algorithm
def dutch(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low=low+1
            mid=mid+1
        elif arr[mid]==1:
            mid=mid+1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1
    return arr
    
a=list(map(int,input("Enter array: ").split()))
x=dutch(a)
print(x)
# Time Complexity: O(n). 
# Space Complexity: O(1). 
