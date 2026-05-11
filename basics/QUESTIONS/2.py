name=(input("enter your name: "))
gender=(input("enter your gender M/F:"))

if gender=="M":
    print("hello Good morning Mr.",name)
elif gender=="F":
    print("hello Good morning Mrs.",name)
else:
    print("give correct values in gender ", name)