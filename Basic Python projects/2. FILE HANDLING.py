#CRUD
from pathlib import Path








def createfile():
    name=input("enter the name of your file u want to create :- ")
    p=Path(name)
    o=open(p,"w")
    w=input("Write the stuff u want to write in your created file")
    o.write(w)
    print(" FILE CREATED")


def readfile():
    name=input("enter which file u want to read")
    p=Path(name)
    o=open(p,"r")
    stuff=o.read()
    print(stuff)

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

a=int(input("give your response here :- "))

if a==1:
    createfile()
if a==2:
    readfile()