#factor of no.
num=int(input("enter the no. whose factor u want to find :"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
