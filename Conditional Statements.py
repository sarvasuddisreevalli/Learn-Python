# if-else statement
age = int(input("Enter your age:\n"))
if age >= 18 and age <65:
  print("You're an adult")
elif age >= 65:
    print("You're a senior citizen")
elif age < 0:
    print("Invalid age")
elif age == 0:
    print("You're just born")
else:
  print("You're a child")
  
# if-else boolean example
is_student = True
if is_student:
    print("You're a student")
else:
    print("You're not a student")

# arithmetic operators
# (=,+,-,*,/,//,%)
friends = 5
# friends++ doesn't work 
friends += 1
friends -= 3
friends *= 2
friends /= 2 #(float division)
friends //= 3 #(interger division)
remaining_friends = friends % 2
friends %= 2

# Type casting
# User input is always a string so type conversion needed
name = 'siri'
subjects = 19
gpa = 8.99
is_prime = True
# type(gpa) --> to check datatype
gpa = int(gpa)
subjects = float(subjects)
subjects = str(subjects)
name = bool(name)
print(type(name))
