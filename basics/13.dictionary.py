#soo basically key value pair {}
a={1:"sumit",2:"karan",3:"rohan"} 
#mutable hote h means key value pair ko change or modify kr skte h 
#(srif values change kr skte h)
#key must be unique but value can be duplicate 
#insertion oder follow krte h 
#hetrogenous means koi bhi datatype rakh sktee h
print(a[1])#ismai jo key h uski value print hogi (DICTIONARY MAI INDEX NI HOTAA KEYS SE HE VALUE IDENTIFY KRTE H)
a[1]="sumit ji"#updating the value
a[4]="mohit"#creating a new key value pair
print(a)
del a[4]#deleting a key and its value
print(a)
for i in a:
    print(i) #key print karega
    print(a[i]) #key ki value print kregaa

#DEEP COPY AND SALLOW COPY CONCEPT ISMAI HAM .COPY() FN USE KRTE H 
