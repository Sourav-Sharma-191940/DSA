#Brute force method
def twoSum(arr, target):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1, n):
            if arr[i]+arr[j]==target:
               print("The sum found on index: ", i , j)
           
arr=list(map(int,input("Enter array: ").split()))
target=int(input("Enter no. to find sum"))
twoSum(arr, target)
#time compleity=O(n^2)

#by using hash table as its lookup time is O(1)
    
    