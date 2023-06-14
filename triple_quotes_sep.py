print("it's",'"monday"',"today")
# using three double quotes to avoid concatination in the statements which contain multiple single quotes or double quoteM
print("""It's "Monday" today""")
print("""Today's day is not Friday""")
print("""It's "sunny" weather outside""")
print("""Luke's address is: 123: Terminal's Lake""")
# same data type 
num1,num2,num3=1,2,3
print(num1,num2,num3)
# diff data type
data1,data2,data3=1,"sav",1.2
print(data1,data2,data3)
# using sep to add underscore instead of spaces 
# sep should always be added at the end
print("python","course","code","Prog123",sep="_")
# using end to finish a line with specific character and to join next line
print("python","course","code","Prog123",sep="_",end=" ")
print("first sem")
# using \t\n to print in the next line
print("python","course","code","Prog123",sep="_",end="--\t\n")
print("first sem")
# this will break the end also in two lines
print("python","course","code","Prog123",sep="_",end="-----\n---\t\n")
type1=123.3
type2="hello"
print(type(type1)) #using TYPE to find out the data type of the variable used
print(type(type2))

