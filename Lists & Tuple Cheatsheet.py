# List is the type of datatype where U can store multiple value
# It is inserted in [] brackets For eg.
# List is imutable -- Means It can not change

Items_grocery = ["choclate","candy","toffee","shirt","cell",]
print(Items_grocery[0]) #U can print them using print(Listname[Item_order])


#It can Store Intergers also For eg.


My_marks = [20,24,76,45,79,68,47]
My_marks.sort()      #It is Used to arrange the list in accending order
My_marks.reverse()   #It is Used to reverse the List
print(My_marks)


# while printing We can Use : for printing from specific number to specific number for 2nd time
# : is used for jumping numbers

print(My_marks[1:5])
print(My_marks[::2])

#Append Is used for add in the end of the list

My_marks.append(10)
print(My_marks)

#Insert Is Used To Insert in certain Index

My_marks.insert(3,5)
print(My_marks)

# Everything is same in tuple The only diffrence is tuple is Immutable
# Tuple Use () brackets