#print all even and odd no. seperately in nth term
n=int(input("enter the nth terms :"))
e=0
o=0
for i in range(n+1):
    if i%2==0:
        e+=i
    else:
        o+=i
print("sum of all even terms ",e)
print("sum of all odd terms ",o)