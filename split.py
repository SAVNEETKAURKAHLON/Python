#using split for separating two numbers
a, b = input("please enter the two numbers to be added ").split() #split(";") to split using semi colon
a, b = (float(a),float(b))
print ("the sum of thwe two numbers is ",(a+b))
#split works only for string
#must take input as string and  then CHANGE THE DATA TYPE otherwise it will show error
date = "11/2/3"
#split at / ,so it will split date into three parts
date = date.split("/")
print(date)  #it will be printed in the form of list
month = int(date[0])
day = int(date[1]) #[0] are index numbers
year = int(date[2])
print(month, day, year)