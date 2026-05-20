#input two no. and print the greatest one

a=int(input("enter first no"))

b=int(input("enter second no"))

if a>b:
    print(a,"is greater")

elif a==b:
    print(a,"and",b,"are equal")
else:
    print(b,"is greater")