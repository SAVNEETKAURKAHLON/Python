name ="Savneet kaur kahlon"
name_length = len(name)
print(name[name_length-1])

print(name.isalpha())

string ="Hello World"
print(name.isalpha())

string = "helloworld"
print(name.islower())

string = "HelloWorld"
print(name.islower())

#strip function removes spaces from front 
#title converts first letter of every string into capital letter
#isdigit function checks if every letter is digit and gives true as a answer

message = " hello world "
print(message.title())
print(message.strip())
print(message.isdigit())

var1="hello "
var2="hello world"
print(var2 in var1) #is var2 string in var1 (false)
print(var1 in var2) # is vae1 in var2 (true)
print(var1 not in var2) #is var1 not in var2 (false)
print(var2 not in var1) # is var2 not in var1 (true)
split_using = var2.split() #split(@) where @ comes savneetkaur015 gmail.com result
print(split_using)
email = "savneetkaur@gmail.com"
print(email.split('@')[0])
name_split = name.split()
#join adds all words 
#should use any letter or space to join words with
print("@".join(name_split))
college = "sheridan"
college_split = " ".join(college)
print(college_split)