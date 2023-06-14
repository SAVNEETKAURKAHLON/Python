# using pow() and sqrt() functions
#math module import all the math functions 
#to use it we should use m.function
import math as m #using m instead of math to short the word
result1 = m.pow(2,5) #2 raised to power 5
print(result1)
result2 = m.sqrt(36) # square root of 36
print(result2)

radius = 12
circumference = m.pi * radius * 2
area = m.pi * m.pow(radius,2)
area = m.pi * radius**2
print("the circumference of the circle is ",round(circumference,3))
print("the area of the circle is ",round(area,3)) 

#ceil is greatest integer number while floor is smallest integer number
res1 = m.floor(12.35)
res2 = m.ceil(12.35)
res3 = m.ceil(-3.35)
res4 = m.floor(-3.35)
print(res1,res2,res3,res4,sep="|")

