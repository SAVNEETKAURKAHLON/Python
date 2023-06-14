first_name = "Bob"
last_name = "Smith"
#using curly brackets to concatinate strings
# using , to separate we can use anything 
#using f-string we don't have to convert data type to concatinate
full_name = f"{last_name},{first_name}"
print(full_name)
print()
age = 38
info = f"{last_name} is {age} years old"
print("User info: ",info)
print()
info = last_name+ " is "+ str(age) + " years old"
print("User info ",info)