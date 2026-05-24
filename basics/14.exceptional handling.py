#Error vo mistake hoti h jishe aapke code mai dikkat hoti h like run ni hotaa
#SYNTAX AND LOGICAL ERROR
 #INDENDATION ERROR
#ERROR KI WAJH SE PROGRAM KA FLOW BREAK HO JAATA H
#TRY ; EXCEPT ; ELSE ; FINALLY ; RAISE
a=int(input("enter the no. to divide"))
try:
    print(10/a)
except Exception as e:
    print(f"you found a error as {e}")#agr ye run hua toh else ni hogaa 
else:
    print('there is no error')# if else run hua Means except run ni hogaa
finally:
    print("mai run hungaa he")#iska mtlb ki kuch bhi ho ye block of code chalegaa hee

print("division done")
