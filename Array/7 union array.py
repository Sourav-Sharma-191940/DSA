# By using sets as set automatically removes duplicate values
# def setUnion(a, m, b, n):
#     s=set(a)
#     for ele in b:
#         s.add(ele)
#         return len(s)
# Time Complexity: O(m * log(m) + n * log(n))
#O(m + n) in case of Python because in python the set built-in method is quite different than that of C++ once, Python uses an hash map internally.

#By using dictionary
# def dictUnion(a, b):
#     d = {}
#     count = 0
#     for ele in a:
#         if ele in d:
#             continue
#         d[ele] = 1
#         count += 1
#     for ele in b:
#         if ele in d:
#             continue
#         d[ele] = 1
#         count += 1
#     return count

#By using map
def mapUnion(a,m,b,n):
    mp={}
    for i in range(m):
        mp[a[i]]=i
    for i in range(n):
        mp[b[i]]=i
    for key in mp.keys():
        print(key,end=" ")
 
# time complexity= O(m+n)

a=[23,4,34,22,1,4]
m=6
b=[23,4,22,2345,55]
n=5
mapUnion(a, m, b, n)
