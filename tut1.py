print("hello world")
# // python is case sensitive 
# // DYNAMIC LANGUAGE
age= input("enter age") 
print("current age= "+ age) 
#//Input is string, need TYPE CONVERSION
print("wrong age after 3 years= " + (age)  )

print("age after 3 years= " + str(int(age)+3)  )
# //converted age to int, then added age, then re converted to string to concatenate with text to display.

name1 = "uditi"
name2= "uditi raymangia" 

print(name1.upper())
print(name1.find('u')) #gives index of u in name starting from 0
#gives -1 if not found
print(name2.find('raymangia')) #gives starting index of string raymangia
print('u'in name1) #returns if the char or string exists in name1 or not(bool)
print( name1.replace('u',"su")) # name1.replace('d', "dh") )
print(name2.replace('i','I'))

print(5//2) # =2 and not 2.5  #truncates decimal 

#operator precedence same as c++ 
print(range(7))
# there is no block system in python, you just indent properly to write right code
#string multiplication is possible in python
i=0
while(i<5):
    print(i*"*")  #automatically goes to new line in every iteration
    i+=1
for item in range(5):
    print(item) #prints items in range(5)

#list = mixed array
list1 = [0,1,2, "hello", True, 'last'] #true won't work as python is case sensitive
print(list1)
print(list1[3])
print(list1[-1]) #prints the last element in list
print(list1[1:3]) #prints elements from index 1 to 2 not 3
for item in list1:
    print(item)
#similar to range example, therefore range is a list of integers
# difference in directly printing list and using a loop is that while directly printing it prints in 1 line with brackets and inverted commas, with loop, it prints in new line(due to iteration) and without inverted commas
#can use while and iterator method also instead of for
list1.insert(5,"second last") #inserting at the mentioned index value
print(list1)
list1.append("added") #to add at end
print(list1)

print("hello" in list1) #searches if hello exists in list1; similar to example of string, therefore string just list of characters. 
print(len(list1))  
#break same as in c++
""" list2=[0,1,2,3]
list3=['hi','yo','ciao', 'hola'] """
print("---CONTINUE USECASE---")
for item in list1:
    if item == 'hello':   #don't forget to indent in if loop
        continue
    print(item) 
#this loop prints everthing except hello
print("---tuple---")
list1=(0,1,2,2,'no')#tuple= list without modification options available or a CONSTANT LIST
list2 = 0,1,2,'no'#this is also a tuple
print(list1) #list 1 assigned to tuple, no more a list
tuple1=list1
print(tuple1.count(2)) #gives how many times that element is present
print(tuple1.index('no')) #gives the index of that element
print(list1) #still it is tuple
print("---set---")
set1= list1={0,1,2,2}
print(list1) #list 1 gone to set
#in set, only once any element is printed even if it exists twice in actaul set
#there is no index system in set #cant use set1[2], therefore sets are unordered
print("---dictionary---")#when want to store values in pair 
dict1={"uditiParent":"pankaj", "uditiMarks":99}
print(dict1)
print(dict1["uditiMarks"]) #can individually access 2nd element of every pair
dict1['uditiMarks']=100 #can do alteration
print(dict1["uditiMarks"])
