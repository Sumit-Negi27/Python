#Check whether the no. is prime  or not
num=int(input("enter the no. :"))
a=0
if num==0:
    print("not prime no.")
elif num==1:
    print("prime no")
else:
    for i in range(1,num):
        if num%i==0:
            a+=i
    if a==1:
        print("prime")
    else:
        print("not prime")
