#reverse the string without any pre build fn
a="SUMIT"
for i in range(len(a)-1,-1,-1):
    print(a[i])
    
#Check string is palindrome or not
s = input("Enter a string: ")
rev = ""

for i in s:
    rev = i + rev
    print(rev)
if s == rev:
    print("Palindrome String")
else:
    print("Not a Palindrome String")