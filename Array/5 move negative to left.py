#1)Bruteforce approach
def negArr(arr):
    n=len(arr)
    for _ in range(0, n):
        for j in range(_+1, n):
            if arr[_]>arr[j]:
                arr[_],arr[j]=arr[j],arr[_]
                
arr=list(map(int, input().split()))
negArr(arr)
print(arr)

# Time complexity: O(N^2) 
# Auxiliary Space: O(1) 

# 2)Shift to left
def leftArr(arr):
    n=len(arr)
    j=0
    for i in range(0, n):
        if arr[i]<0:
            arr[i],arr[j]=arr[j],arr[i]
            j=j+1
    print(arr)

arr=list(map(int, input().split()))
leftArr(arr) 

# Time complexity: O(N) 
# Auxiliary Space: O(1) 

#3)two pointer approach
def seperate(arr, left, right):
    while right>=left :
        if arr[left]< 0 and arr[right]<0:
            left=left+1
        elif arr[left]> 0 and arr[right]<0:
            arr[left],arr[right]=arr[right],arr[left]
            right=right-1
            left=left+1 
        elif arr[left]> 0 and arr[right]>0:
            right=right-1
        else:
            right=right-1
            left=left+1
    print(arr)        

arr=list(map(int, input().split()))
n=len(arr)
seperate(arr, 0, n-1)
# Time Complexity: O(N)
# Auxiliary Space: O(1)

# 4)By dutch national flag algorithm (two color)
    