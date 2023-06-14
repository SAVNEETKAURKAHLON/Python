temp = int(input("enter the temperature today "))
if( temp > 40):
    print("today is nice weather")
else:
    print("today is little cold")

score = int(input("enter the marks "))
if( score >=0 and score <= 100):
    
    if( score<60):
     print("grade is F")
    elif(score < 70):
     print("grade is D")
    elif(score < 80):
        print("grade is C")
    elif(score < 90):
     print("grade is B")
    else:
     print("grade is A")
else:
   print("enter valid score")
