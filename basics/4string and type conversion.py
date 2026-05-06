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