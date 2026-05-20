#FACTORIAL
n=int(input("enter the nth terms :"))
fact=1
for i in range(n,0,-1):
    fact*=i
print(fact)