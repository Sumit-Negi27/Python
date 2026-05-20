#list mai -ve and +ve no h tumko best hh and u have to print seperately
# l=[1,-2,3,4,-5,6,-7,-8]
# l1=[]
# l2=[]
# for i in range(len(l)):
#     if l[i]>0:
#         l1.append(l[i])
#     else:
#         l2.append(l[i])
# print(l1)
# print(l2)

#mean of list element
# a=[1,2,3,4,5,6]
# sum=0
# for i in range(len(a)):
#     sum+=a[i]
# mean=sum/len(a)
# print(mean)

#FIND GRATEST ELEMENT AND PRINT THE INDEX TOO
a=[100,2,300,4,450,55,6,350]
# max=0
# for i in range(1):
#     for j in range(1,len(A)):
#         if A[i]>A[j] and A[i]>max:
#            max=A[i]
#         elif A[j]>A[i] and A[j]>max:
#            max=A[j]
#     print(f"the greatest no. is :{max}")
#     print("index of the no. is :", A.index(max))
# greatest=a[0]
# s=0
# index=0
# for i in range(len(a)):
#     if a[i]>greatest:
#         s=greatest
#         greatest=a[i]
#         index=i
#     elif a[i]>s:
#         s=a[i]
# print(f"Greatest no. is {greatest} and it's index value is {index}")
# print(f"second largest no. is {s} and it's index is {a.index(s)}")
 
#check list is sorted or not
a=[1,2,3,4,5,6,8]
for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        print("list is not sorted")
        break
else:
    print("list is sorted")