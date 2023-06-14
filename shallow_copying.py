list_one=[1,2,3,4,5]
list_two= list_one
list_two[1]=9
print(list_two)
print(list_one)
ones_list = [1,2,5,4,3]
students = [["joel",85,95,70] , ["Anne",95,100,100] , ["Mike",77,70,85]]
print(students)
print(students[1][2])
print(students[0][1])

if((ones_list[0] > ones_list[1]) and (ones_list[0] > ones_list[2]) and (ones_list[0] > ones_list[3]) and (ones_list[0] > ones_list[4])):
    print("zero index is greater")
  
elif((ones_list[1] > ones_list[0]) and (ones_list[1] > ones_list[2]) and (ones_list[1] > ones_list[3]) and (ones_list[1] > ones_list[4])):
    print("first index is greater")

elif((ones_list[2] > ones_list[0]) and (ones_list[2] > ones_list[1]) and (ones_list[2] > ones_list[3]) and (ones_list[2] > ones_list[4])):
    print("second index is greater")

elif((ones_list[3] > ones_list[0]) and (ones_list[3] > ones_list[2]) and (ones_list[3] > ones_list[1]) and (ones_list[3] > ones_list[4])):
    print("third index is greater")

else:
    print("fourth index is greater")





l1 = [1,2]
l2 = [5,6]
l3 = l1+l2
print(l3)
