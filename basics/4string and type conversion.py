#String thoda extra space leti h 
#kyuki haar string ka ek unicode hota h and vo usko save krti h 
#like
a="A"
print(ord(a))#unicode find krtaa h character ka 
print(chr(65))# unicode ko character mai covert krta h 

#indexing = 0 to n left to right and -1 to -n right to left
name="Sumit"
print(name[0])
print(name)
print(name[-1])

#STRING SLICING 
name="sumit negi"

#name[start:stop+1:steps]

print(name[0:5:1])
print(name[6::])

#type conversion 
# int () float() str() bool() 
#boolean mai falsy wale 0 , 0.0 , FALSE , () , [] , {} , " "
x=""
x=bool(x)
print(x)
num=123
b=str(num)
print(b)

#type conversion 2 type 
# implicit python khudse data conversion krta h and explicit ismai hamko krna padhta h

