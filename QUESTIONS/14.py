s="sfgjlh8754323@#$%^&*()"
d=0
a=0
sc=0
for i in s:
    if i.isdigit():
        d+=1
    elif i.isalpha():
        a+=1
    else:
        sc+=1
print(f"DIGIT = {d} \n CHARACTER = {a} \n SPECIAL SYMBOL = {sc}")

