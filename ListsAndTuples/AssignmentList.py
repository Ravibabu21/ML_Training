My_Fruits=['Apple','Banana','Grape','PineApple','Mango']
print(My_Fruits[2]) #printing the 3rd item in the list as indexing starts from 0,1,2,3,4 so the 3rd item will be grape.
My_Fruits.append("Berry") #adding the berr fruit to the list.
print(My_Fruits)
del My_Fruits[1]
print(My_Fruits) #removed 2nd item in the list.

My_tuple=(1,2,3,4,25)
print("My first number ", My_tuple[0]," My last Number ", My_tuple[-1]) #accesing first and last number in the tuple

found = False
for num in My_tuple:
    if num==25:
        found = True
        break
if found:
    print("The number is present in the tuple")
else:
    print("Sorry 25 is not in the tuple") #checking 25 is in the tuple or not

My_tuple_list=list(My_tuple)
My_tuple_list.append(55)
My_tuple=tuple(My_tuple_list)
print(My_tuple) #converted to list and added new number and again converted to tuple