#CRUD
from pathlib import Path
import os


def createfile():
    try:
        name=input("enter the name of your file u want to create :- ")
        p=Path(name)
        o=open(p,"w")
        w=input("Write the stuff u want to write in your created file :- ")
        o.write(w)
        print(" FILE CREATED")
    except Exception as e:
         print(f"you found a error as {e}")


def readfile():
    try:
        name=input("enter which file u want to read :-")
        p=Path(name)
        o=open(p,"r")
        stuff=o.read()
        print(stuff)
    except Exception as e:
        print(f"error aa giyaa bhai {e}")

def updatefile():
    try:
        name=input("enter the name of the file u want to update :-")
        p=Path(name)
        print("press 1 if u want to rename the file")
        print("press 2 if u want to update but remove the previous data")
        print("press 3 if u want to append the new data")
        choice=int(input("enter your choice = "))
        if choice==1:
            name2=input("enter your new file name :-")
            p2=Path(name2)
            p.rename(p2)
        if choice==2:
            with open(p,"w") as o:
                w=input("enter what u want to write over it :-")
                o.write(w)
        if choice==3:
            with open(p,"a") as o:
                w=input("enter u want to append :-")
                o.write(" "+w)
    except Exception as e:
        print(f"error aa giyaa re jiska name h {e}")

def removefile():
    try:
        name=input("enter the file name u want to remove :-")
        p=Path(name)
        os.remove(p)
        print("file removed")
    except Exception as e:
        print(f"exception aa giya whose name is: {e}")
while True:
    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 0 to end the task")

    a=int(input("give your response here :- "))

    if a==1:
        createfile()
    if a==2:
        readfile()
    if a==3:
        updatefile()
    if a==4:
        removefile()
    if a==0:
        break