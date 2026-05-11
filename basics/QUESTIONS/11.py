#perfect no.
num=int(input("enter the no. :"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
print(sum)
if sum==num:
    print(f"{num} is perfect no.")
else:
    print("not perfect no.")

