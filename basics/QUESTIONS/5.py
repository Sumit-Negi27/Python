#find the given year is Leap year or not

y=int(input("enter the year"))
if y%100==0 and y%400==0:
    print(f"{y}is a leap year")
elif y%100!=0 and y%4==0:
    print(f"{y}is a leap year")
else:
    print(f"{y} is normal year")

