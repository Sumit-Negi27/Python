#find the frequency of the elements occur in a list
l=[1,1,1,2,2,3,4,3,3,4,4,2,1]
d={}
for i in l:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)
