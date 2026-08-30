# if-else statement
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
age = 19
gpa = 8.99
is_prime = True
# type(gpa) --> to check datatype
gpa = int(gpa)
age = float(age)
age = str(age)
name = bool(name)
print(type(name))
