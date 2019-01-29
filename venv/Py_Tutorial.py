myfloat1 = 7.0 # Defining float without defining type of variable
print("myfloat1 = ", myfloat1)
myfloat2 = float(7) # defining float using type

print("myfloat2 = ", myfloat2)
mystring1 = 'hello' # defining string using ''
print("mystring1 = ", mystring1)
mystring2 = "hello" # Using "" we can include apostrophes
print("mystring2 = ", mystring2)
mystring3 = "Don't worry about apostrophes"
print("mystring3 = ", mystring3)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a, b)

# This will not work!
#
# one = 1
# two = 2
# hello = "hello"
# print(one + two+ hello)
#
# This will not work!

# LISTS
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1, 2, 3
for x in mylist:
    print(x)

# ARITHMETIC OPERATORS
number = 1 + 2 * 3 / 4.0
print (number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello " * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

# TASK
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#This prints out "Hello, Eugene!"

    name = "Eugene"
    print("Hello, %s!" % name)

#This prints out "Eugene is 21 years old."
    name = "Eugene"
    surname = "Oliferenko"
    age = 21
    print("%s %s is %d years old." % (name, surname, age))

#This pronts out: A list: [1, 2, 3]
    mylis = [1,2,3]
    print("A list: %s" % mylist) # The line that is printed out is STRING type

# %s - String (or any objects)
# %d - integers
# %f - floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot
# %x/%X - Integers in hex representation (lowercase/uppercase)

#TASK
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

#BASIC STRING OPERATIONS
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))

astring = "Hello world!"
print(astring.index("o"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print(astring[3:7:2])
# [start:stop:step]

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])

astring = "Hello world!"
print(astring[::-1])
# inversion

astring = "Hello world!"
print(astring.upper())
print(astring.lower())
#converting into the uppercase and lowercase

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdsdgdfhfsfh"))
#just cheacking

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)

#TASK
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurence of "a" should be at index 8
print("The first occurence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

#Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # start to five
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # just number 12
print("The characters with odd index are '%s'" % s[1:2]) # (0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th -from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lovercase
print("String in lovercase: %s" % s.lower())

# Check how a string starts
if s.startwith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endwith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings, each containing only a word
print("Split the words of a string: %s" % s.split(" "))