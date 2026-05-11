# n=123456
# while n>0:
#     print(n%10)
#     n=n//10
#accept a no. and print it reverse 
num=int(input("enter the no."))
rev=0
while num>0:
    rev= rev*10+ num%10
    num=num//10
print(rev)