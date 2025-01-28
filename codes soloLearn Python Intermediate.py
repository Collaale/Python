Dictionaries


Python provides a number of built-in collection types, to store multiple values.

Lists are one of these collection types, and they allow you to store indexed values:

x = ['hi', 'hello', 'welcome']
print(x[2])
#welcome

Each item of a list has an index, which is automatically set.

Dictionaries are another collection type and allow you to map arbitrary keys to values.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

Example:

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"]) #24
print(ages["Mary"]) #42

Each element in a dictionary is represented by a key:value pair.

Dictionaries


Only immutable objects can be used as keys to dictionaries. Immutable objects are
those that can't be changed. So far, the only mutable objects you've come across 
are lists and dictionaries.

bad_dict = {
    [1, 2, 3]: "one two three", 
}

"""
Traceback (most recent call last):
  File "file0.py", line 1, in <module>
    bad_dict = {
TypeError: unhashable type: 'list'
"""

Since lists are mutable, the code above throws an error.
This means that you can use strings, integers, booleans, and any other immutable type as 
dictionary keys.


Problem
Dictionaries


You are working at a car dealership and store the car data in a dictionary:
car = {
    'brand': 'BMW',
    'year': 2018,
    'color': 'red'
} 
PY
Your program needs to take the key as input and output the corresponding value.

Sample Input
year

Sample Output
2018
The data is already defined in the code.



SOLUTION:

car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

ent = input()

print(car[ent])


Test Case 1

Input
brand

Your Output
BMW

Expected Output
BMW


####################################################################################

Dictionaries


To determine whether a key is in a dictionary, you can use in and not in, 
just as you can for a list.


Example:
Run the code and see how it works!

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

True
False
True


Dictionaries


A useful dictionary function is get. It does the same thing as indexing,
but if the key is not found in the dictionary it returns another specified value instead.

Example:

pairs = {    1: "apple",
	  "orange": [2, 3, 4], 
	      True: False, 
	        12: "True",
}

print(pairs.get("orange"))				#[2, 3, 4]
print(pairs.get(7, 42))				    #42
print(pairs.get(12345, "not found"))	#not found


To determine how many items a dictionary has, use the len() function.

Dictionaries
What is the result of this code?

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
#8 (sum of 3 + 5)


Problem

Dictionary Functions


You are working on data that represents the economic freedom rank by country.
Each country name and rank are stored in a dictionary, with the key being the country name.

Complete the program to take the country name as input and output its corresponding economic
freedom rank. In case the provided country name is not present in the data, output "Not found".

Recall the get() method of a dictionary, that allows you to specify a default value.


############ first way
data = {
    'Singapore'     : 1,
    'Ireland'       : 6,
    'United Kingdom': 7,
    'Germany'       : 27,
    'Armenia'       : 34,
    'United States' : 17,
    'Canada'        : 9,
    'Italy'         : 74
}


c = input()

print(data.get(c,"Not found"))




############ second way
 data = {
    'Singapore'     : 1,
    'Ireland'       : 6,
    'United Kingdom': 7,
    'Germany'       : 27,
    'Armenia'       : 34,
    'United States' : 17,
    'Canada'        : 9,
    'Italy'         : 74
}


c = input()

try:
    print(data[c])
except:  
    print("Not found")

####################################################################################


Tuples


Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.

Example:
words = ("spam", "eggs", "sausages")


You can access the values in the tuple with their index, just as you did with lists:

words = ("spam", "eggs", "sausages",)
print(words[0])
#spam

Trying to reassign a value in a tuple causes an error.

words = ("spam", "eggs", "sausages",)
words[1] = "cheese"

"""
Traceback (most recent call last):
  File "file0.py", line 2, in <module>
    words[1] = "cheese"
TypeError: 'tuple' object does not support item assignment
"""

Like lists and dictionaries, tuples can be nested within each other.


Tuples

Fill in the blanks to create a list, dictionary, and tuple:

# list
list = ["one", "two"]

# dictionary 
dict = {1:"one", 2:"two"}

# tuple 
tp = ("one", "two")


Tuples


Tuples can be created without the parentheses by just separating the values with commas.

Example:
my_tuple = "one", "two", "three"
print(my_tuple[0]) ##one

*****Tuples are faster than lists, but they cannot be changed.



Problem
Tuples


You are given a list of contacts, where each contact is represented by a tuple,
with the name and age of the contact.
Complete the program to get a string as input, search for the name in the list
 of contacts and output the age of the contact in the format presented below:

Sample Input
John

Sample Output
John is 31
If the contact is not found, the program should output "Not Found".

SOLUTION:


contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

c= str(input())

for i in contacts:
    if c in i:
        print(str(i[0]) +" is "+ str(i[1]))
        break
else:
    print("Not Found")


######################################################################################


Tuple Unpacking


Tuple unpacking allows you to assign each item in a collection to a variable.

Example:

numbers = (1, 2, 3)
a, b, c = numbers

print(a)
print(b)
print(c)

#1
#2
#3

This can be also used to swap variables by doing a, b = b, a , since b, a on the
right hand side forms the tuple (b, a) which is then unpacked.

Tuple Unpacking
What is the value of y after this code runs?

x, y = [1, 2]
x, y = y, x
#1

Tuple Unpacking


A variable that is prefaced with an asterisk (*) takes all values from the collection 
that are left over from the other variables.

Example:
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

#1
#2
#[3, 4, 5, 6, 7, 8]
#9
c will get assigned the values 3 to 8.

######################################################################################


Sets


Sets are similar to lists or dictionaries.
They are created using curly braces, and are unordered, which means that they 
can't be indexed.

Due to the way they're stored, it's faster to check whether an item is part of
 a set using the in operator, rather than part of a list.
Sets cannot contain duplicate elements.

num_set = {1, 2, 3, 4, 5}

print(3 in num_set)
#True

Sets cannot contain duplicate elements.


You can use the add() function to add new items to the set, and remove() 
to delete a specific element:

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#{1, 2, 3, 4, 5, 6}
#{1, 2, 4, 5, 6, -7}

Duplicate elements will automatically get removed from the set.

The len() function can be used to return the number of elements of a set.

Fill in the blanks to create a set, add the letter "z" to it, and print its length.

nums = {"a", "b", "c", "d"}
nums.add("z")
print(len(nums))


Sets

Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

#{1, 2, 3, 4, 5, 6, 7, 8, 9}
#{4, 5, 6}
#{1, 2, 3}
#{8, 9, 7}
#{1, 2, 3, 7, 8, 9}


Problem
Sets


You are working on a recruitment platform, which should match the available 
jobs and the candidates based on their skills.

The skills required for the job, and the candidate's skills are stored in sets.
Complete the program to output the matched skill.

You can use the intersect operator to get the values present in both sets.

skills = {'Python', 'HTML', 'SQL', 'C++', 'Java', 'Scala'}
job_skills = {'HTML', 'CSS', 'JS', 'C#', 'NodeJS'}


print(list(job_skills & skills)[0])

#########################################################################


List Comprehensions


List comprehensions are a useful way of quickly creating lists whose contents 
obey a rule.

For example, we can do the following:

# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

#[0, 1, 8, 27, 64]


List comprehensions are inspired by set-builder notation in mathematics.


What does this list comprehension create?

nums = [i*2 for i in range(10)]
#A list of even numbers between 0 and 18


List Comprehensions


A list comprehension can also contain an if statement to enforce a condition on

values in the list.

Example:
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)
#[0, 4, 16, 36, 64]


#############################################################################


Problem

List Comprehensions


Given a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u.

Sample Input
awesome

Sample Output
['w', 's', 'm']
Use a list comprehension to create the required list of letters and output it.



SOLUTION:

word = input()

vowels = {"a","e","i","o","u",}

wa= [i for i in word if i not in vowels ]


print(wa)


############################################################################


List Comprehensions
Create a list of multiples of 3 from 0 to 20.
a = [i for i in range(20) if i%3==0]


###########################################################################

Data Structures


As we have seen in the previous lessons, Python supports the following 
collection types: ***Lists,
				  ***Dictionaries,
				  ***Tuples,
				  ***Sets.

When to use a dictionary:
-*** When you need a logical association between a key:value pair.
-*** When you need fast lookup for your data, based on a custom key.
-*** When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
---- Use lists if you have a collection of data that does not need random access.
 Try to choose lists when you need a simple, iterable collection that is modified frequently.

---- Use a set if you need uniqueness for the elements.

---- Use tuples when your data cannot/should not change.


Many times, a tuple is used in combination with a dictionary, for example, a tuple 
might represent a key, because it's immutable.


Data Structures

Which of the following data types does not allow duplicate values?
#Set


What is the result of this code?

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
#44


Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.
a = [x*10 for x in range (5, 9)]




##############################################################################


Problem
Letter Counter


Given a string as input, you need to output how many times each letter appears 
in the string.

You decide to store the data in a dictionary, with the letters as the keys,
and the corresponding counts as the values.
Create a program to take a string as input and output a dictionary, which
represents the letter count.

Sample Input
hello

Sample Output
{'h': 1, 'e': 1, 'l': 2, 'o': 1}

You need to output the dictionary object.
Note, that the letters are in the order of appearance in the string.


SOLUTION

text = input()
dict = {}
#your code goes here

for x in text:
  #count += 1
  dict[x] = text.count(x)

print(dict)


##############################################################################


Functional Programming


Functional programming is a style of programming that (as the name suggests)
is based around functions.

A key part of functional programming is higher-order functions. Higher-order 
functions take other functions as arguments, or return them as results.

Example:

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

#20

The function apply_twice takes another function as its argument, and calls it 
twice inside its body.



What is the output of this code?

def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))
#16

Pure Functions


Functional programming seeks to use pure functions. Pure functions have no side effects,
and return a value that depends only on their arguments.
This is how functions in math work: for example, the cos(x) will, for the same value of x, 
always return the same result.
Below are examples of pure and impure functions.

*******************Pure function:
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)


*******************Impure function:
some_list = []

def impure(arg):
  some_list.append(arg)


The function above is not pure, because it changed the state of some_list.


Pure Functions

Using pure functions has both advantages and disadvantages.

Pure functions are:

------------ easier to reason about and test.
------------ more efficient. Once the function has been evaluated for 
an input, the result can be stored and referred to the next time
the function of that input is needed, reducing the number of times
the function is called. This is called memoization.
------------ easier to run in parallel.

***Pure functions are more difficult to write in some situations.


##################################################################################



110 Comments
Lambdas


Creating a function normally (using def) assigns it to a variable with its name
automatically.
Python allows us to create functions on-the-fly, provided that they are created 
using lambda syntax.

This approach is most commonly used when passing a simple function as an argument
to another function. The syntax is shown in the next example and consists of the 
lambda keyword followed by a list of arguments, a colon, and the expression to
evaluate and return.

def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)


Functions created using the lambda syntax are known as anonymous.


##################################################################################

Lambdas


Creating a function normally (using def) assigns it to a variable with its name 
automatically.
Python allows us to create functions on-the-fly, provided that they are created using
 lambda syntax.

This approach is most commonly used when passing a simple function as an argument to
 another function. The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, a colon, and the expression to evaluate and return.


def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)


Functions created using the lambda syntax are known as anonymous.


Lambdas


Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression -- 
usually equivalent to a single line of code.


Example:
In the code above, we created an anonymous function on the
 fly and called it with an argument.


 #named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))				   #0

#lambda
print((lambda x: x**2 + 5*x + 4) (-4)) #0


Lambdas
Fill in the blanks to create a lambda function that returns the square of its argument,
 and call it for the number 8.

a = (lambda x: x*x) (8)


**********************map


The built-in functions map and filter are very useful higher-order functions that operate
on lists (or similar objects called iterables).

*****The function map takes a function and an iterable as arguments, and returns a 
new iterable with the function applied to each argument.

Example:

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#[16, 27, 38, 49, 60]


We could have achieved the same result more easily by using lambda syntax.

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

#[16, 27, 38, 49, 60]


To convert the result into a list, we used list explicitly.


**************************map

Fill in the blanks to multiply each item in the list by 2 using lambda syntax.

nums = [11, 22, 33]
a = list(map(lambda x: x*2 , nums))


filter


The function filter filters an iterable by leaving only the items that match a 
condition (also called a predicate).

Example:

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
#[22, 44]

****Like map, the result has to be explicitly converted to a list if you want to print it.


****************filter

Fill in the blanks to extract all items that are less than 5 from the list.


nums = [1, 2, 5, 8, 3, 0, 7]

res = list(filter(lambda x: x<5, nums))

print(res)



**************Generators


Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, 
but they can still be iterated through with for loops.
They can be created using functions and the *******yield statement.

Example:

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

5
4
3
2
1


The yield statement is used to define a generator, replacing the 
return of a function to provide a result to its caller without destroying local variables.

What statement is used in functions to turn them into generators?
*******yield


Generators


Due to the fact that they yield one item at a time, generators don't have the memory 
restrictions of lists. In fact, they can be infinite!


def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)

Result:
>>>
7
7
7
7
7
7
7
...

In short, generators allow you to declare a function that behaves like an iterator,
i.e. it can be used in a for loop.

Generators

Fill in the blanks to create a prime number generator that yields all prime numbers
in a loop. (Consider having an is_prime function already defined):

def
 get_primes():

  num = 2

  while True:
    if is_prime(num):
		yield num
    num += 1


Generators


Finite generators can be converted into lists by passing them as arguments to the 
list function.

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

[0, 2, 4, 6, 8, 10]


Using generators results in improved performance, which is the result of the lazy
(on demand) generation of values, which translates to lower memory usage. 
Furthermore, we do not need to wait until all the elements have been generated
before we start to use them.

Generators

What is the result of this code?

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))
#['s', 'sp', 'spa', 'spam']



Decorators


Decorators provide a way to modify functions using other functions.
This is ideal when you need to extend the functionality of functions
 that you don't want to modify.

Example:


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()
============
Hello world!
============

We defined a function named decor that has a single parameter func. Inside decor,
 we defined a nested function named wrap. The wrap function will print a string,
  then call func(), and print another string. The decor function returns the wrap
   function as its result.
We could say that the variable decorated is a decorated version of print_text
 -- it's print_text plus something.
In fact, if we wrote a useful decorator we might want to replace print_text 
with the decorated version altogether so we always got our "plus something"
 version of print_text.
This is done by re-assigning the variable that contains our function:

print_text = decor(print_text)
print_text()

============
Hello world!
============
Now print_text corresponds to our decorated version.


This pattern can be used at any time, to wrap any function.
Python provides support to wrap a function in a decorator by
 pre-pending the function definition with a decorator name and the @ symbol.
If we are defining a function we can "decorate" it with the @ symbol like:
This will have the same result as the above code.
A single function can have multiple decorators.

###################################################################################

Recursion


Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference -- functions calling themselves.
It is used to solve problems that can be broken up into easier sub-problems of the
same type.

A classic example of a function that is implemented recursively is the factorial function,
which finds the product of all positive integers below a specified number.
For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!.
Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials.
Below is a recursive implementation of the factorial function.

def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))

The base case acts as the exit condition of the recursion.
Not adding a base case results in infinite function calls, crashing the program.

Recursion


Recursion can also be indirect. One function can call a second, which calls the first, 
which calls the second, and so on. This can occur with any number of functions.

Example:

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))
True
False

Recursion
What is the result of this code?

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

*args


Python allows you to have functions with varying numbers of arguments.
Using *args as a function parameter enables you to pass an arbitrary 
number of arguments to that function. The arguments are then accessible 
as the tuple args in the body of the function.

Example:

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(The parameter *args must come after the named parameters to 
a function., 2, 3, 4, 5)

The name args is just a convention; you can choose to use another.

**kwargs


**kwargs (standing for keyword arguments) allows you to handle named arguments
that you have not defined in advance.
The keyword arguments return a dictionary in which the keys are the argument names,
and the values are the argument values.

Example:
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

###{'a': 7, 'b': 8}

a and b are the names of the arguments that we passed to the function call.
The arguments returned by **kwargs are not included in *args.


#######################################################################


What is the output of this code?

def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)
8


#######################################################################

Spelling Backwards


Given a string as input, use recursion to output each letter of the strings
in reverse order, on a new line.

Sample Input
HELLO

Sample Output

O
L
L
E
H

Complete the recursive spell() function to produce the expected result.

SOLUTION:

def spell(txt):
    #your code goes here
    #i = len(txt)
    if txt=="": 
        return txt
    else:
        print(txt[len(txt)-1])
        return spell(txt[0:len(txt)-1])
    

txt = input()
spell(txt)



#######################################################################

Classes


The focal point of Object Oriented Programming (OOP) are objects, which are
 created using classes.
The class describes what the object will be, but is separate from the object
itself. In other words, a class can be described as an object's blueprint,
description, or definition.
You can use the same class as a blueprint for creating multiple different objects.

Classes are created using the keyword class and an indented block, which contains
class methods (which are functions).
Below is an example of a simple class and its objects.

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


#######################################################################

__init__


The __init__ method is the most important method in a class.
This is called when an instance (object) of the class is created, using the
class name as a function.

All methods must have self as their first parameter, although it isn't explicitly
 passed, Python adds the self argument to the list for you; you do not need to
  include it when you call the methods. Within a method definition, self refers
   to the instance calling the method.

Instances of a class have attributes, which are pieces of data associated with them.
In this example, Cat instances have attributes color and legs. These can be accessed
 by putting a dot, and the attribute name after an instance.
In an __init__ method, self.attribute can therefore be used to set the initial value
 of an instance's attributes.

Example:
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)

##ginger

In the example above, the __init__ method takes two arguments and assigns them to the
object's attributes. The __init__ method is called the class constructor.


################################################################################

Methods


Classes can have other methods defined to add functionality to them.
Remember, that all methods must have self as their first parameter.
These methods are accessed using the same dot syntax as attributes.

Example:

class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

##Fido
##Woof!

Class attributes are shared by all instances of the class.


Problem

Classes


You are making a video game! The given code declares a Player class,
with its attributes and an intro() method.
Complete the code to take the name and level from user input, create
a Player object with the corresponding values and call the intro()
method of that object.

Sample Input
Tony
12

Sample Output
Tony (Level 12)
Use the dot syntax to call the intro() method for the declared object.

SOLUTION:

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

#your code goes here
a= input()
b= input()

play = Player(a,b)
play.intro()


TESTE

Input
Player1
4
Your Output
Player1 (Level 4)
Expected Output
Player1 (Level 4)

############################################################################


Inheritance


Inheritance provides a way to share functionality between classes.
Imagine several classes, Cat, Dog, Rabbit and so on. Although they may differ
in some ways (only Dog might have the method bark), they are likely to be similar
in others (all having the attributes color and name).
This similarity can be expressed by making them all inherit from a superclass Animal,
 which contains the shared functionality.
To inherit a class from another class, put the superclass name in parentheses after 
the class name.

Example:

class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

##brown
##Woof!



Inheritance


A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods,
it overrides them.

class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

##Woof

In the example above, Wolf is the superclass, Dog is the subclass.


Inheritance


The function super is a useful inheritance-related function that refers
 to the parent class. It can be used to find the method with a certain name in
  an object's superclass.

Example:

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

#2
#1

super().spam() calls the spam method of the superclass.


############################################################################


Magic Methods


Magic methods are special methods which have double underscores at the beginning 
and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__, but there are several others.
They are used to create functionality that can't be represented as a normal method.


One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and *
to be used on them.
An example magic method is __add__ for +.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

8
16

The __add__ method allows for the definition of a custom behavior for the + operator 
in our class.
As you can see, it adds the corresponding attributes of the objects and returns a new
object, containing the result.
Once it's defined, we can add two objects of the class together.


Magic Methods


More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

The expression x + y is translated into x.__add__(y).
However, if x hasn't implemented __add__, and x and y are of different types,
 then y.__radd__(x) is called.
There are equivalent r methods for all magic methods just mentioned.

Example:

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

##spam
##============
##Hello world!

In the example above, we defined the division operation for our class SpecialString.


Magic Methods
What is A() ^ B() evaluated as, if A doesn't implement any magic methods?

##B().__rxor__(A())

Magic Methods


Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.

Example:


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs


#>spam>eggs
#e>spam>ggs
#eg>spam>gs
#egg>spam>s
#eggs>spam>

As you can see, you can define any custom behavior for the overloaded operators.


Magic Methods


There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, 
such as __call__ for calling objects as functions, and __int__, __str__,
 and the like, for converting objects to built-in types.

Example:

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

#6
#3
#B
#B

We have overridden the len() function for the class VagueList
 to return a random number.
The indexing function also returns a random item in a range from
the list, based on the expression.


Magic Methods
Which magic method call is made by x[y] = z?

#x.__setitem__(y, z)


############################################################################

Data Hiding


A key part of object-oriented programming is encapsulation, which involves packaging 
of related variables and functions into a single easy-to-use object -- an instance of
a class.
A related concept is data hiding, which states that implementation details of a class 
should be hidden, and a clean standard interface be presented for those who want to use
 the class.
In other programming languages, this is usually done with private methods and attributes, 
which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all 
consenting adults here", meaning that you shouldn't put arbitrary restrictions on
accessing parts of a class. Hence there are no ways of enforcing that a method or
attribute be strictly private.

However, there are ways to discourage people from accessing parts of a class, such
as by denoting that it is an implementation detail, and should be used at their own risk.

Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, 
it is mostly only a convention, and does not stop external code from accessing them.

Example:
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

Queue([1, 2, 3])
Queue([0, 1, 2, 3])
Queue([0, 1, 2])
[0, 1, 2]


In the code above, the attribute _hiddenlist is marked as private, but it can still be
 accessed in the outside code.
The __repr__ magic method is used for string representation of the instance.

Data Hiding


Strongly private methods and attributes have a double underscore at the beginning of 
their names. This causes their names to be mangled, which means that they can't be 
accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid bugs if 
there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name. 
The method __privatemethod of class Spam could be accessed externally with
 _Spam__privatemethod.


Example:
class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)

7
7

Traceback (most recent call last):
  File "file0.py", line 9, in <module>
    print(s.__egg)
AttributeError: 'Spam' object has no attribute '__egg'

Basically, Python protects those members by internally changing the name to
include the class name.




How would the attribute __a of the class b be accessed from outside the class?
##_b__a



############################################################################


Class Methods


Methods of objects we've looked at so far are called by an instance of a class,
 which is then passed to the self parameter of the method.
Class methods are different -- they are called by a class, which is passed to the
 cls parameter of the method.
A common use of these are factory methods, which instantiate an instance of a class,
 using different parameters than those usually passed to the class constructor.
Class methods are marked with a classmethod decorator.

Example:


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

#25

New_square is a class method and is called on the class, rather than on an instance
of the class. It returns a new object of the class cls.

Technically, the parameters self and cls are just conventions; they could be changed
to anything else. However, they are universally followed, so it is wise to stick to
using them.


19 Comments

Class Methods
Fill in the blanks to make sayHi() a class method.
class Person:

  def __init__(self, name):

    self.name = name


@classmethod
  
def
 sayHi(cls):

    print("Hi")


Static Methods


Static methods are similar to class methods, except they don't receive any additional
arguments; they are identical to normal functions that belong to a class.
They are marked with the staticmethod decorator.

Example:

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


##No output

Static methods behave like plain functions, except for the fact that you can call 
them from an instance of the class.

Which of these is most likely to be a static method?
def spam(x, y):


##################################################################################

Properties


Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method, which
means when the instance attribute with the same name as the method is accessed,
the method will be called instead.
One common use of a property is to make an attribute read-only.

Example:

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

False


Traceback (most recent call last):
  File "file0.py", line 11, in <module>
    pizza.pineapple_allowed = True
AttributeError: can't set attribute

Properties
Fill in the blanks to create an "isAdult" property.
class Person:

  def __init__(self, age):

    self.age = int(age)

  
@property


  def isAdult(self):

    if self.age > 18
:


      return True

    else:

return
False


Properties


Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as
the property, followed by a dot and the setter keyword.
The same applies to defining getter functions.

Example:

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

#if digit Sw0rdf1sh!
False
Enter the password: True


#if digit anything
False
Enter the password: 

Traceback (most recent call last):
  File "file0.py", line 21, in <module>
    pizza.pineapple_allowed = True
  File "file0.py", line 17, in pineapple_allowed
    raise ValueError("Alert! Intruder!")
ValueError: Alert! Intruder!

Define a decorator that would be used to add a setter to the property egg.
@egg.setter


Fill in the blanks to make the egg attribute strongly private and access it
 from outside of the class.

class Test:
__egg = 7

t = Test()

print(t._Test__egg)


Fill in the blanks to make a setter for the property name.
class Person:

  def __init__(self, name):

    self._name = name

  @property

  def name(self):

    return self._name
  
##@name.setter


  def name(self, value):

##    self._name = value


######################################################################################

Problem
Shooting Game


You are creating a shooting game!
The game has two types of enemies, aliens and monsters. You shoot the aliens using your 
laser, and monsters using your gun.
Each hit decreases the lives of the enemies by 1.
The given code declares a generic Enemy class, as well as the Alien and Monster classes,
with their corresponding lives count.
It also defines the hit() method for the Enemy class.

You need to do the following to complete the program:
1. Inherit the Alien and Monster classes from the Enemy class.
2. Complete the while loop that continuously takes the weapon of choice from user input 
and call the corresponding object's hit() method.

Sample Input
laser
laser
gun
exit

Sample Output
Alien has 4 lives
Alien has 3 lives
Monster has 2 lives
The while loop stops when the user enters 'exit'.

class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)


m = Monster()
a = Alien()

while True:
    x = input()
    if x == 'laser':
      a.hit()
    elif x == 'gun':
      m.hit()  
    elif x == 'exit':
        break

########################################################################################

Exceptions


You have already seen exceptions in previous code. They occur when something goes wrong,
due to incorrect code or input. When an exception occurs, the program immediately stops.
The following code produces the ZeroDivisionError exception by trying to divide 7 by 0:

num1 = 7
num2 = 0
print(num1/num2)

Traceback (most recent call last):
  File "file0.py", line 3, in <module>
    print(num1/num2)
ZeroDivisionError: division by zero


An exception is an event, which occurs during the execution of a program that disrupts
the normal flow of the program.


Exceptions


Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an
inappropriate value.
Python has several other built-in exceptions, such as ZeroDivisionError and OSError.
 Third-party libraries also often define their own exceptions.


 Exception Handling


When an exception occurs, the program stops executing.
To handle exceptions, and to call code when an exception occurs,
you can use a try/except statement.
The try block contains code that might throw an exception. If that exception occurs,
the code in the try block stops being executed, and the code in the except block is run. 
If no error occurs, the code in the except block doesn't run.

For example:

try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

## An error occurred
## due to zero division


Exception Handling

A try statement can have multiple different except blocks to handle different exceptions.
Multiple exceptions can also be put into a single except block using parentheses, to have 
the except block handle all of them.

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

#Error occurred

You can handle as many exceptions in the except statement as you need.


Exception Handling


An except statement without any exception specified will catch all errors.

These should be used sparingly, as they can catch unexpected errors and hide programming
mistakes.

For example:

try:
    word = "spam"
    print(word / 0)
except:
    print("An error occurred")

Exception handling is particularly useful when dealing with user input.


###############################################################################

finally


After a try/except statement, a finally block can follow. It will execute after the
try/except block, no matter if an exception occurred or not.

try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")

Hello
Divided by zero
This code will run no matter what

The finally block is useful, for example, when working with files and resources:
 it can be used to make sure files or resources are closed or released regardless 
 of whether an exception occurs.


###############################################################################

else


The else statement can also be used with try/except statements.
In this case, the code within it is only executed if no error occurs in the try statement.

Example:

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

#1
#3


try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

#4

else
What is the sum of the numbers printed by this code?

try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)
#4


Raising Exceptions


You can throw (or raise) exceptions when some condition occurs.
For example, when you take user input that needs to be in a specific format, you can throw
an exception when it does not meet the requirements.
This is done using the raise statement.


num = 102
if num > 100:
  raise ValueError

Traceback (most recent call last):
  File "file0.py", line 3, in <module>
    raise ValueError
ValueError


You need to specify the type of the exception raised. In the code above, we raise a ValueError.


How many exceptions will the following code result in?

try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError

#2

Exceptions can be raised with arguments that give detail about them.

For example:


name = "123"
raise NameError("Invalid name!")

Traceback (most recent call last):
  File "file0.py", line 2, in <module>
    raise NameError("Invalid name!")
NameError: Invalid name!


Raising Exceptions
Fill in the blanks to raise a ValueError exception, if the input is negative.

Raising Exceptions
Fill in the blanks to raise a ValueError exception, if the input is negative.
num = input(":")

if float(num) < 0:
  raise ValueError("Negative!")        

##########################################################################################

Problem
Registration System


You are making a registration form for a website.
The form has a name field, which should be more than 3 characters long.
Any name that has less than 4 characters is invalid.
Complete the code to take the name as input, and raise an exception if the name is invalid,
outputting "Invalid Name". Output "Account Created" if the name is valid.

Sample Input
abc

Sample Output
Invalid Name
Use try/raise/except statements.


try:
    name = input()
    #your code goes here
    if len(name) < 4:
        raise 
    
except:
    print("Invalid Name")

else:
    print("Account Created")


###########################################################################################

Opening Files


You can use Python to read and write the contents of files.
This is particularly useful when you need to work with a lot of data that is 
saved in a file. For example, in data science and analytics, the data is commonly in CSV 
(comma-separated values) files.

Let's start by working with text files, as they are the easiest to manipulate.
Before a file can be edited, it must be opened, using the open function.


myfile = open("filename.txt")


The argument of the open function is the path to the file. If the file is in the current
working directory of the program, you can specify only its name.

Opening Files


You can specify the mode used to open a file by applying a second argument to the
 open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files
 (such as image and sound files).

For example:

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")


You can combine modes, for example, wb from the code above opens the file
 in binarywrite mode.

 Opening Files


Once a file has been opened and used, you should close it.
This is done with the close method of the file object.
file = open("filename.txt", "w")
# do stuff to the file

file.close()


We will read/write content to files in the upcoming lessons.

###########################################################################################

Reading Files


The contents of a file that has been opened in text mode can be read 
using the read method.

We have created a books.txt file on the server which includes titles of books.
 Let's read the file and output the content:


file = open("/usercode/files/books.txt")
cont = file.read()
print(cont)
file.close()

#This will print all of the contents of the file.

Harry Potter
The Hunger Games
Pride and Prejudice
Gone with the Wind

Reading Files


To read only a certain amount of a file, you can provide the number of bytes to read as an
 argument to the read function.
Each ASCII character is 1 byte:


file = open("/usercode/files/books.txt")
print(file.read(5))
print(file.read(7))
print(file.read())
file.close()

Harry
 Potter

The Hunger Games
Pride and Prejudice
Gone with the Wind


Calling the read() method without an argument will return the rest of the file content.


Reading Files


To retrieve each line in a file, you can use the readlines() method to return a list 
in which each element is a line in the file.

For example:

file = open("/usercode/files/books.txt")

for line in file.readlines():
    print(line)
    
file.close()


Harry Potter

The Hunger Games

Pride and Prejudice

Gone with the Wind


If you do not need the list for each line, you can simply iterate over the file variable:


Harry Potter

The Hunger Games

Pride and Prejudice

Gone with the Wind


In the output, the lines are separated by blank lines, as the print function automatically
adds a new line at the end of its output.

##########################################################################################


Problem
Reading Files


You need to make a program to read the given number of characters of a file.
Take a number N as input and output the first N characters of the books.txt file.


The given code opens the books.txt file. Use the file object to read the content of the file


file = open("/usercode/files/books.txt")
#your code goes here

n = input()

print(file.read(int(n)))

file.close()


########################################################################################


Reading Files
Fill in the blanks to open a file, read its content and print its 2nd line.

file = open("filename.txt", "r")

cont = file. readlines()

print(cont[1])

file.close()


########################################################################################


Writing Files


To write to files you use the write method.

For example:


file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

#This has been written to a file

This will create a new file called "newfile.txt" and write the content to it.
In case the file already exists, its entire content will be replaced when you
open it in write mode using "w".


Writing Files APPEND


If you want to add content to an existing file, you can open it using the "a" mode,
which stand for "append":

file = open("/usercode/files/books.txt", "a")

file.write("\nThe Da Vinci Code")
file.close()

file = open("/usercode/files/books.txt", "r")
print(file.read())
file.close()

This will add a new line with a new book title to the file.
Remember, \n stands for a new line.


Writing Files


The write method returns the number of bytes written to a file, if successful.


msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

##12

The code above will write to the file and print the number of bytes written.

To write something other than a string, it needs to be converted to a string first.


#####################################################################################


Working with Files


It is good practice to avoid wasting resources by making sure that files are always
 closed after they have been used. One way of doing this is to use try and finally


try:
  f = open("/usercode/files/books.txt")
  cont = f.read()
  print(cont)
finally:
 f.close()

Harry Potter
The Hunger Games
Pride and Prejudice
Gone with the Wind

This ensures that the file is always closed, even if an error occurs.


Working with Files


An alternative way of doing this is by using with statements.This creates a temporary 
variable (often called f), which is only accessible in the indented block of the with 
statement.

with open("/usercode/files/books.txt") as f:
  print(f.read())

Harry Potter
The Hunger Games
Pride and Prejudice
Gone with the Wind


 The file is automatically closed at the end of the with statement, even if
exceptions occur within it.


##########################################################################################

Problem


Title Encoder


You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the
title and combine them.

For example, for the book title "Game of Thrones" the encoded version should be "GoT".

Complete the program to read the book title from the file and output the encoded versions,
each on a new line.

You can use the .split() method to get a list of words in a string.



file = open("/usercode/files/books.txt", "r")


#your code goes here

for title in file:
    for word in title.split():
        print(word[0], end="")
    print()


file.close()


