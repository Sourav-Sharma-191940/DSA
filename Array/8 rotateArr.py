def rotate(arr, n):
    temp=arr[n-1]
    for i in range(n-1, 0,-1):
        arr[i]=arr[i-1]
    arr[0]=temp
    print(arr)
# Time Complexity: O(n) 
# Auxiliary Space: O(1)

#using two pointer 
def pointerRotate(arr, n):
    i=0
    j=n-1
    while i!=j:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
    
       
arr=[23, 55, 75, 37, 1, 488]
n=6
rotate(arr, n)