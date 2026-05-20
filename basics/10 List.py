#IN PYTHON WE HAVE 4 TYPE OF DATA STRUCTURE
#LIST,TUPLE,DICTIONARY,SETS

#LIST
#allow duplicates values
a=[1,23,3,4,3,4]
#mutable hoti h (change kr skte h)

#hetrogenous means ek mai he different data structure add kr skte h
l=[1,"sum",1.22,True]
#ordered mai rahegaa and in sequence mai
#ismai indexing and slicing bhi kr skte h same like string

#LIST TRAVERSING
# for i in range(len(a)):
#     print(a[i])

#method and functions soo basically methods mai a.append() and in function add(a) kuch aesa hotaaa
#METHODS IN LIST
#append
a.append(100)
print(a)
#insert 2.5 at index 2
a.insert(2,2.5)
print(a)
#remove first occurence of that no. will remove
a.remove(3)
print(a)
a.index(1)#index no. find krke de detaa h 