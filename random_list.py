import random
stats = []
stats.insert(0,round(random.random(),2))
stats.insert(1,random.random())
print(stats)

var1 = 0
var2 = 0
list1 = []


flip1 = round(random.random(),1)
list1.append(flip1)

flip2 = round(random.random(),1)
list1.append(flip2)

flip3 = round(random.random(),1)
list1.append(flip3)

flip4 = round(random.random(),1)
list1.append(flip4)

flip5 = round(random.random(),1)
list1.append(flip5)

print(list1)
if( flip1 < 0.5):
     print("head")
     var1 +=1
else:
    print("tail")
    var2 +=1

if( flip2 < 0.5):
    print("head")
    var1 +=1
else:
    print("tail")
    var2 +=1


if( flip3 < 0.5):
    print("head")
    var1 +=1
else:
    print("tail")
    var2 +=1


if( flip4 < 0.5):
    print("head")
    var1 +=1
else:
    print("tail")
    var2 +=1


if( flip5 < 0.5):
    print("head")
    var1 +=1
else:
    print("tail")
    var2 +=1

print("heads",var1)
print("tails",var2)



