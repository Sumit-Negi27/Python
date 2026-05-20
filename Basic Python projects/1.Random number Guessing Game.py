import random #python library h that generate random no.
num = random.randint(1,10)


trial=0
while True:
    guess=int(input("please guess the no between 1 to 10(can include 1 and 10 als0): "))
    if guess>10:
        print("no. is out of bound")
    if guess!=num:
        print("sorry try again")
        trial+=1
        print(f"No. of attempts : {trial}")
        if num>guess:
            print("go little higher")
        elif num<guess:
            print("go little lower")
    else:
        print("Yeahh u guessed it right in ",trial, " attempts")
        break
