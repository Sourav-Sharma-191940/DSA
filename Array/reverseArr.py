#program to reverse a given array
#1)By iterative approach
def reverseArr(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start=start+1
        end=end-1
#map function use to convert all entries into specific type like here converting all input into int.        
array= list(map(int,input("Enter array: ").split()))
x=len(array)-1
print("Given array is: ",array)
reverseArr(array, 0, x)
print("The reversed array is ",array)
#Time Complexity : O(n)

#2)recursive approach
def recursiveRev(arr, start, end):
    if start<end:
        arr[start],arr[end]=arr[end],arr[start]
        recursiveRev(arr, start+1, end-1)
        return arr
    
    
array= list(map(int,input("Enter array: ").split()))
x=len(array)-1
print("Given array is: ",array)
recursiveRev(array, 0, x)
print("The reversed array is ",array)
#Time Complexity : O(n)

#3)Using list slicing:- array[::-1]
    