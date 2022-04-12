#Find maximum and minimum element in an array
# 1)Bruteforce approach
# def maxmin(arr):
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
    
# arr=list(map(int,input().split()))
# x=len(arr)-1
# maxmin(arr)
# print(arr[x], arr[0])
#Time complexity=O(n^2)

#method 2
def minmax(arr, min, max):
    # when have only one Element
    if len(arr)==1:
        min=arr[0]
        max=arr[0]
    # for more than one element, we initilize min and max by giving the values arr[0] and arr[1]
    elif arr[0]>arr[1]:
        min=arr[1]
        max=arr[0] 
    else:
        min=arr[0]
        max=arr[0]
    
    for i in range(2, len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    return min, max
            
arr=list(map(int,input().split()))
x=minmax(arr, 0, 0)
print(x)
# Time complexity=O(n)
#3)Divide and conuer.         
    
        
