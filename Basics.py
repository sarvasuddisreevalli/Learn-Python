# output :
# print(value,...,sep='',end='\n',flush=False)
print('Hello World')
print(7)
print(True)
print('Hello',1,2.5,True)

# data types :
print(7) # integer
print(1e309) # python can't handle and gives inf
print(1.7e308)
print(8.55) # floating numbers
print(True) # boolean
print('This is a string') # string
print(5+6j) # complex number
print([1,2,3,4,5]) # list
print((1,2,3,4,5)) # tuple
print({1,2,3,4,5}) # set
print({'Name':'Siri','Age':19,'Course':'BTech'}) # dictionary
type({2}) # func that detects data type

# variables :
name = 'sreevalli'
print(f"I'm {name}")
a = 10
b = 9
print(name,a+b)
# dynamic typing
a = 5
# static typing
# int c = 5
# dynamic binding - in python
x = 5
print(x)
x = 'siri'
print(x) # no fixed datatype 
# static binding - in c,cpp,java
int y = 5
y = 'siri'
print(y)
a,b,c = 1,2,3
a=b=c = 5

# comments :
# written for developer comfort & not executable part
# No multiple line commands in python
# first comment
a = 1 # integer

# keywords :
# False
# None
# True
# and
# as
# assert
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield

# identifiers :
# identifiers can not be keyword
# you can't start with a digit
# 1a = 1 --> wrong
# a1 = 1 --> works
# you can't use special characters
# first-name = 'siri' --> wrong using -,@,#
# first_name = 'siri' --> works
# _ = 'sreevalli' --> works

# user input :
input ('Enter name:') # takes everything as string
int (input('Enter a val')) # takes input stores as integer
# type conversion :
int('4')
# int(2+3i) -->not possible in python
str(5)
float(4)

# Literals
a = 0b1010 # binary literal
b = 100 # decimal literal
c = 0o310 # octal literal
d = 0x12c # hexadecimal literal
# float literals
float_1 = 1.5
float_2 = 1.5e2
float_3 = 1.5e-3
#complex literal 
g = 3.14j
print(g.real,g.imag)

string1 = 'This is a valid string'
string2 = "This is a valid string"
char = "C"
multiline_str = """This is a multiline string with more than one line of code""" # allows multiple lines as single string
unicode = u"\U0001f600\U0001F606\U0001F923" # output : 3 emoji's with that unicode
raw_str = r"raw \n string" # output : raw \n string instead of raw string

a = True+4
b = False+10
print(a,b)
# true,false doesn't work only True,False works

# Null literal
a = None
print(a)
# used only for variable declaration like in c we use like (int a;)
# In python we can declare a variable with a value or None





