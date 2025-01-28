for line in file: 
    print(file.readlines())

file.close()


print(file.read(4))
print(file.read())



file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()


file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()



msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()
#alternative
with open("filename.txt") as f:
   print(f.read());


list = file.readlines()
print(list[]);




"""Book Titles


You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book

Your program should output:
S9
A12
Recall the readlines() method, which returns a list containing the lines of the file.
Also, remember that all lines, except the last one, contain a \n at the end, which should not be included in the character count.
"""


file = open("/usercode/files/books.txt", "r")

#your code goes here
#list = file.readlines()
#print(list)


for line in file: 
    line = line.strip("\n")
    print(line[0] + str(len(line)))

file.close()

#################################
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

####################################

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

#######################################


nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

##########################################

filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)

#########################################

def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

##########################################

filename = input("Enter a filename: ")
with open(filename) as f:
  text = f.read()

print(count_char(text, "r"))

>>>
Enter a filename: test.txt
83
>>>

##########################################


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))


result:

a - 4.68%
b - 4.94%
c - 2.28%
d - 0.0%
e - 3.8%
f - 5.19%
g - 8.99%
h - 2.53%
i - 0.63%
j - 0.51%
k - 0.51%
l - 1.9%
m - 0.0%
n - 6.2%
o - 2.28%
p - 1.9%
q - 2.03%
r - 10.51%
s - 1.27%
t - 1.39%
u - 3.54%
v - 6.08%
w - 0.0%
x - 0.25%
y - 3.92%
z - 1.65%


##########################################

Word Counter


Given text as input, output the number of words it contains.

Sample Input
hello world

Sample Output
2

txt = input()

#by Colla
def count_words(text):
    count = 1
    for c in text:
        #print(text)
        if c == " ":
            count += 1
    return count

print(count_words(txt))

##########################################

"""
Longest Word

Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
"""

txt = input()

#fin = open("txt","r")
#txt = txt.read()

words = txt.split()
max_len = len(max(words, key=len))
for word in words:
    if len(word)==max_len:
        longest_word =word
         
print(longest_word)
 

##########################################

"""
Lambdas

Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression 
- usually equivalent to a single line of code.
Example:
"""

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#Lambda functions can be assigned to variables, and used like normal functions.
#Example:

double = lambda x: x * 2
print(double(7))
#14

##########################################

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#[16, 27, 38, 49, 60]

We could have achieved the same result more easily by using lambda syntax.
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = map(lambda x: x+5, nums)
print(result)


##########################################

#The function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean).
#Example:

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

##########################################

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

##########################################
#print even numbers in a list:

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

##########################################

#decorator:

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

or

print_text = decor(print_text)
print_text()

result:

============
Hello world!
============

##Python provides support to wrap a function in a decorator by pre-pending the function definition with a decorator name and the @ symbol.
##If we are defining a function we can "decorate" it with the @ symbol like:
@decor
def print_text():
    print("Hello world!")

print_text();

#This will have the same result as the above code.

##########################################

Decorators


You are given code that takes input and prints it as a simple row of text.

Add the uppercase_decorator to make the text uppercase.

text = input()

def uppercase_decorator(func):
    def wrapper(text):
        #your code goes here
        return func(text.upper())
    return wrapper
    
@uppercase_decorator    
def display_text(text):
    return(text)
    
print(display_text(text))

##########################################
#Recursion
#Factorial


def factorial(x):
    if x == 1:    #base case
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))


another simple:

Recursion
What is the result of this code?
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))
#5


##########################################
##Sets are data structures, similar to lists or dictionaries. 
##They are created using curly braces, or the set function


num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)             #true
print("spam" not in word_set)   #false

#To create an empty set, you must use set(), as {} creates an empty dictionary

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums) #{1, 2, 3, 4, 5, 6}
nums.add(-7)
nums.remove(3)
print(nums) #{1, 2, 4, 5, 6, -7}


#Basic uses of sets include membership testing and the elimination of duplicate entries.



first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) #{4, 5, 6}
print(first - second) #{1, 2, 3}
print(second - first) #{8, 9, 7}
print(first ^ second) #{1, 2, 3, 7, 8, 9}

##########################################
DATA structures:

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. 
Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot change.


##########################################
itertools
The module itertools is a standard library that contains several functions that are useful in
functional programming.
One type of function it produces is infinite iterators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable (for instance a list or string).
The function repeat repeats an object, either infinitely or a specific number of times.
Example:
 

from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break
3
4
5
6
7
8
9
10
11        



Some examples:
takewhile - takes items from an iterable while a predicate function remains true;
chain - combines several iterables into one long one;
accumulate - returns a running total of values in an iterable.

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)                                     #[0, 1, 3, 6, 10, 15, 21, 28]
print(list(takewhile(lambda x: x<= 6, nums)))   #[0, 1, 3, 6]


There are also several combinatoric functions in itertool,
such as product and permutation.
These are used when you want to accomplish a task with all 
possible combinations of some items.
Example:
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2)))) #[('A', 0), ('A', 1), ('B', 0), ('B', 1)]
print(list(permutations(letters)))      #[('A', 'B'), ('B', 'A')]

##########################################

Fibonacci


The Fibonacci sequence is one of the most famous formulas in mathematics.
Each number in the sequence is the sum of the two numbers that precede it.
For example, here is the Fibonacci sequence for 10 numbers, starting from 0: 0,1,1,2,3,5,8,13,21,34.

Write a program to take N (variable num in code template) positive numbers as input, and recursively calculate and output the first N numbers of the Fibonacci sequence (starting from 0).

Sample Input
6

Sample Output
0
1
1
2
3
5


my program:
num = int(input())


def fibonacci(n):
    #complete the recursive function
    if n == 0 or n == 1:
        return n
    else: 
        return (fibonacci(n-1) + fibonacci(n-2))
        

for i in range(num):
    print(fibonacci(i))

##########################################


class samples:

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)


class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

#Fido
#Woof!


Classes can also have class attributes, created by assigning variables 
within the body of the class. These can be accessed either from instances 
of the class, or the class itself.
Example:

class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)

#4
#4

##########################################

Inheritance

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
In the example above, Wolf is the superclass, Dog is the subclass.



Inheritance can also be indirect. One class can inherit from another, 
and that class can inherit from a third class.

Example:
class A:
    def method(self):
        print("A method")
    
class B(A):
    def another_method(self):
        print("B method")
    
class C(B):
    def third_method(self):
        print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()

However, circular inheritance is not possible.


The function super is a useful inheritance-related function that refers to the parent class.
It can be used to find the method with a certain name in an object's superclass.
Example:

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

2
1

##########################################

One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such
as + and * to be used on them.
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
print(result.x)  #8
print(result.y)  #16

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

##########################################
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

spam
============
Hello world!



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

>spam>eggs
e>spam>ggs
eg>spam>gs
egg>spam>s
eggs>spam>

##########################################

There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.
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

4
10
B
B

##########################################
a = 42  # Create object <42>
b = a  # Increase ref. count  of <42> 
c = [a]  # Increase ref. count  of <42> 

del a  # Decrease ref. count  of <42>
b = 100  # Decrease ref. count  of <42> 
c[0] = -1  # Decrease ref. count  of <42>

Lower level languages like C don't have this kind of automatic memory management


Data Hiding


A key part of object-oriented programming is encapsulation, which involves packaging
of related variables and functions into a single easy-to-use object - an instance of a class.
A related concept is data hiding, which states that implementation details of a class should
be hidden, and a clean standard interface be presented for those who want to use the class.
In other programming languages, this is usually done with private methods and attributes, 
which block external access to certain methods and attributes in a class.

The Python philosophy is slightly different. It is often stated as "we are all consenting adults here",
meaning that you shouldn't put arbitrary restrictions on accessing parts of a class. Hence there are no
ways of enforcing a method or attribute be strictly private.
However, there are ways to discourage people from accessing parts of a class, such as by denoting 
that it is an implementation detail, and should be used at their own risk.

Data Hiding


Weakly private methods and attributes have a single underscore at the beginning.
This signals that they are private, and shouldn't be used by external code. However, 
it is mostly only a convention, and does not stop external code from accessing them.
Its only actual effect is that from module_name import * won't import variables that
start with a single underscore.
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
print(queue)             ##Queue([1, 2, 3])
queue.push(0)
print(queue)             ##Queue([0, 1, 2, 3])
queue.pop()
print(queue)             ##Queue([0, 1, 2])
print(queue._hiddenlist) ##[0, 1, 2]

In the code above, the attribute _hiddenlist is marked as private, but it can
still be accessed in the outside code. The __repr__ magic method is used for
string representation of the instance.

Strongly private methods and attributes have a double underscore at the beginning
 of their names. This causes their names to be mangled, which means that they 
 can't be accessed from outside the class.
The purpose of this isn't to ensure that they are kept private, but to avoid bugs
 if there are subclasses that have methods or attributes with the same names.
Name mangled methods can still be accessed externally, but by a different name.
The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod.
Example:

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg) #7

s = Spam()
s.print_egg()
print(s._Spam__egg) # 7 
print(s.__egg)      # AttributeError: 'Spam' object has no attribute '__egg'

Basically, Python protects those members by internally changing the name to include the class name.

##########################################

Class Methods

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
print(square.calculate_area())    ##25

Technically, the parameters self and cls are just conventions; they could be changed to
anything else.
 However, they are universally followed, so it is wise to stick to using them.


Static methods

are similar to class methods, except they don't receive any 
additional arguments; they are identical to normal functions that belong to a class.
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


Static Methods
PROBLEM

Complete the given code to define a static add() method for the Calculator class, which returns the sum of its parameters.

The code takes two numbers as input, and should return their sum using the Calculator class's add() method.
Static methods can be called without creating an object of the class.

Solution:

class Calculator:
    #your code goes here
    def __init__ (self, sum):
        self.sum = sum
        
    @staticmethod
    def add (sumA, sumB): 
        sum = sumA + sumB
        return sum
        
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))


Properties


Properties provide a way of customizing access to instance attributes.
They are created by putting the property decorator above a method,
 which means when the instance attribute with the same name as the method is accessed,
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

"""
False


Traceback (most recent call last):
  File "file0.py", line 11, in <module>
    pizza.pineapple_allowed = True
AttributeError: can't set attribute

"""

Properties can also be set by defining setter/getter functions.
The setter function sets the corresponding property's value.
The getter gets the value.
To define a setter, you need to use a decorator of the same name as the property,
 followed by a dot and the setter keyword.
The same applies to defining getter functions.

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

"""if typed wrong:

False
Enter the password: 

Traceback (most recent call last):
  File "file0.py", line 21, in <module>
    pizza.pineapple_allowed = True
  File "file0.py", line 17, in pineapple_allowed
    raise ValueError("Alert! Intruder!")
ValueError: Alert! Intruder!


if typed right:
False
Enter the password: True

"""


A Simple Game


Object-orientation is very useful when managing different objects and their relations.
 That is especially useful when you are developing games with different characters and
  features.

Let's look at an example project that shows how classes are used in game development.
The game to be developed is an old fashioned text-based adventure game.
Below is the function handling input and simple parsing.


def get_input():
  command = input(": ").split()
  verb_word = command[0]
  if verb_word in verb_dict:
    verb = verb_dict[verb_word]
  else:
    print("Unknown verb {}". format(verb_word))
    return

  if len(command) >= 2:
    noun_word = command[1]
    print (verb(noun_word))
  else:
    print(verb("nothing"))

def say(noun):
  return 'You said "{}"'.format(noun)

verb_dict = {
  "say": say,
}

while True:
  get_input()


#The code above takes input from the user, and tries to match the first word with a
#command in verb_dict. If a match is found, the corresponding function is called.


The next step is to use classes to represent game objects.
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)


verb_dict = {
  "say": say,
  "examine": examine,
}    

>>>
: say Hello!
You said "Hello!"

: examine goblin
goblin
A foul creature

: examine elf
There is no elf here.
:

This code adds more detail to the Goblin class and allows you to fight goblins.
class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg


This was just a simple sample.
You could create different classes (e.g., elves, orcs, humans),
fight them, make them fight each other, and so on.


#########################################################


Fill in the blanks to make the egg attribute strongly private and 
access it from outside of the class.


class Test:

  
class Test:

    __egg = 7


t = Test()

print(t._Test__egg)


##############################################################

Fill in the blanks to make a setter for the property name.


class Person:

  def __init__(self, name):

    self._name = name



  @property

  def name(self):

    return self._name

  
    @name.setter      #x


  def name(self, value):

    self._name = value  #x


##############################################################



class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self):
        self.name += name
        self.capacity += capacity


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = Juice__add__(a, b)
print(result)

##############################################################

ProblemR
Juice Maker


You are given a Juice class, which has name and capacity properties.
You need to complete the code to enable and adding of two Juice objects,
resulting in a new Juice object with the combined capacity and names of the two
 juices being added.

For example, if you add an Orange juice with 1.0 capacity and an 
Apple juice with 2.5 capacity, the resulting juice should have:
name: Orange&Apple
capacity: 3.5

The names have been combined using an & symbol.


Use the __add__ method to define a custom behavior for the + operator
 and return the resulting object.


 Solution:
 class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' ('+str(self.capacity)+'L)')

    def __add__(self, other):
        return Juice(self.name +"&"+ other.name, self.capacity + other.capacity)

a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b

print(result)


##############################################################


Regular Expressions


Regular expressions are a powerful tool for various kinds of string manipulation.
They are a domain specific language (DSL) that is present as a library in most
modern programming languages, not just Python.
They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format
 of an email address), - performing substitutions in a string (such as changing all 
 American spellings to British ones).
Domain specific languages are highly specialized mini programming languages.
Regular expressions are a popular example, and SQL (for database manipulation) is another.
Private domain-specific languages are often used for specific industrial purposes.

Regular expressions in Python can be accessed using the re module, which is part of the 
standard library. After you've defined a regular expression, the re.match function can 
be used to determine whether it matches at the beginning of a string.
If it does, match returns an object representing the match, if not, it returns None.
To avoid any confusion while working with regular expressions, we would use raw strings
 as r"expression".Raw strings don't escape anything, which makes use of regular expressions
 easier.

Example:

import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
    print("Match")
else:
    print("No match")

Here the pattern is a simple word, but there are various characters, which would have
 special meaning when they are used in a regular expression.

 Other functions to match patterns are re.search and re.findall.
The function re.search finds a match of a pattern anywhere in the string.
The function re.findall returns a list of all substrings that match a pattern.

Example:
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")        <-

if re.search(pattern, "eggspamsausagespam"):
    print("Match")           <- 
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))  #['spam', 'spam']


print(re.finditer(pattern, "eggspamsausagespam")) # <callable_iterator object at 0x7efff5956610>

The function re.finditer does the same thing as re.findall,
 except it returns an iterator, rather than a list.


The regex search returns an object with several methods that give details about it.
These methods include 
->group which returns the string matched,
-> start and end which return the start and ending positions of the first match,
-> and span which returns the start and end positions of the first match as a tuple.

Example:

import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group()) #pam
    print(match.start()) #4 because not count the position "0"
    print(match.end())   #7   
    print(match.span())  #(4,7)



Search & Replace


One of the most important re methods that use regular expressions is sub.
Syntax:
re.sub(pattern, repl, string, count=0)

This method replaces all occurrences of the pattern in string with repl,
substituting all occurrences, unless count provided. 
This method returns the modified string.

Example:

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)                           # My name is Amy. Hi Amy.

#############################################################################

Metacharacters


Metacharacters are what make regular expressions more powerful than normal string methods.
They allow you to create regular expressions to represent concepts like 
"one or more repetitions of a vowel".

The existence of metacharacters poses a problem if you want to create a regular expression
 (or regex) that matches a literal metacharacter, such as "$". You can do this by escaping
 the metacharacters by putting a backslash in front of them.
However, this can cause problems, since backslashes also have an escaping function in normal
Python strings. This can mean putting three or four backslashes in a row to do all the
escaping.To avoid this, you can use a raw string, which is a normal string with an "r" in
front of it. We saw usage of raw strings in the previous lesson.


The first metacharacter we will look at is . (dot).
This matches any character, other than a new line.


import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")            <-print

if re.match(pattern, "gray"):
    print("Match 2")            <-print

if re.match(pattern, "blue"):
    print("Match 3")            # No found, no print



The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.
Example:

import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")          <-print

if re.match(pattern, "gray"):
    print("Match 2")          <-print  

if re.match(pattern, "stingray"):
    print("Match 3")          # No found, no print


The pattern "^gr.y$" means that the string should start with gr,
then follow with any character, except a newline, and end with y.




#############################################################################


Character Classes


Character classes provide a way to match only one of a specific set of characters.
A character class is created by putting the characters it matches inside square brackets.
Example:

import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")                <-print

if re.search(pattern, "qwertyuiop"):
    print("Match 2")                <-print

if re.search(pattern, "rhythm myths"):
    print("Match 3")                # No found, no print


The pattern [aeiou] in the search function matches all strings that
contain any one of the characters defined.


Character Classes


Character classes can also match ranges of characters.
Some examples:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. 

For example, [A-Za-z] matches a letter of any case

Example:

import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
    print("Match 1")        <--- JUST PRINT THIS

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")

The pattern in the example above matches strings 
that contain two alphabetic uppercase letters followed by a digit.


Place a ^ at the start of a character class to invert it.
This causes it to match any character other than the ones included.
Other metacharacters such as $ and ., have no meaning within character classes.
The metacharacter ^ has no meaning unless it is the first character in a class.

Example:

import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
    print("Match 1")                        <-print

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")                        <-print

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")

The pattern [^A-Z] excludes uppercase strings.
Note, that the ^ should be inside the brackets to invert the character class.


#############################################################################

Problem
Character Classes


All the products in online shop have their own ID. Every ID consists of 4 symbols:
The first symbol: an uppercase character
The second symbol: an uppercase character
The third symbol: a digit
The forth symbol: a digit

Write a program for a search tool, that will take the ID as input and 
output "Searching" if the format is correct, and "Wrong format", if it's not.

Sample Input
LG17

Sample Output
Searching


SOLUTION:

import re
Id = input()

#your code goes here

pattern = r"[A-Z][A-Z][0-9][0-9]$"

if re.search(pattern, Id):
    print("Searching")
else:
    print("Wrong format")


#############################################################################


Metacharacters


Some more metacharacters are * + ? { and }.
These specify numbers of repetitions.
The metacharacter * means "zero or more repetitions of the previous thing".
It tries to match as many repetitions as possible. The "previous thing" 
can be a single character, a class, or a group of characters in parentheses.

Example:

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")                <--print

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")                <--print

if re.match(pattern, "spam"):
    print("Match 3")                #NO PRINT

The example above matches strings 
that start with "egg" and follow with zero or more "spam"s.



Metacharacters


The metacharacter + is very similar to *, except it means "one or more repetitions", 
as opposed to "zero or more repetitions".

Example:

import re

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match 1")                    <--print

if re.match(pattern, "gggggggggggggg"):
    print("Match 2")                    <--print

if re.match(pattern, "abc"):
    print("Match 3")                #NO PRINT


To summarize:
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.


Metacharacters


The metacharacter ? means "zero or one repetitions".
Example:

import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match 1")                <--print

if re.match(pattern, "icecream"):
    print("Match 2")                <--print

if re.match(pattern, "sausages"):
    print("Match 3")                #NO PRINT

if re.match(pattern, "ice--ice"):
    print("Match 4")                #NO PRINT


Fill in the blanks to match both 'color' and 'colour'.

pattern = r"colo(u)?r"



Curly Braces


Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something".
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero.
If the second number is missing, it is taken to be infinity.

Example:

import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
    print("Match 1")            <--print

if re.match(pattern, "999"):
    print("Match 2")            <--print

if re.match(pattern, "9999"):
    print("Match 3")            #NO PRINT

"9{1,3}$" matches string that have 1 to 3 nines.


#############################################################################

Groups


A group can be created by surrounding part of a regular expression with parentheses.
This means that a group can be given as an argument to metacharacters such as * and ?.
Example:

import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")            <--print

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")            <--print

if re.match(pattern, "spam"):
    print("Match 3")            #NO PRINT

(spam) represents a group in the example pattern shown above.



Groups
What would '([^aeiou][aeiou][^aeiou])+' match?
#One or more repetitions of a non-vowel, a vowel and a non-vowel

The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.
Example:

import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

print:

abcdefghi
abcdefghi
bc
de
('bc', 'de', 'fgh', 'g')

########################################################

What would group(3) be of a match of 1(23)(4(56)78)9(0)?
#A call of group(n), where n is greater than 0, returns the nth group from the left.
#56

There are several kinds of special groups.
Two useful ones are named groups and non-capturing groups.

***Named groups have the format (?P<name>...), where name is the name of the group,
 and ... is the content. They behave exactly the same as normal groups, except they
  can be accessed by group(name) in addition to its number.

***Non-capturing groups have the format (?:...). They are not accessible by the group
method, so they can be added to an existing regular expression without breaking the numbering.

Example:

import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
    print(match.group("first"))
    print(match.groups())

#abc
#('abc', 'ghi')

What would be the result of len(match.groups()) of a match of (a)(b(?:c)(d)(?:e))?
#3

Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue".
Example:

import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print ("Match 1")

match = re.match(pattern, "grey")
if match:
    print ("Match 2")    

match = re.match(pattern, "griy")
if match:
     print ("Match 3")

Match 1
Match 2

########################################################

Special Sequences

There are various special sequences you can use in regular expressions.
They are written as a backslash followed by another character.
One useful special sequence is a backslash and a number between 1 and 99,
e.g., \1 or \17. This matches the expression of the group of that number.

Example:

import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
    print ("Match 3")

#Match 1
#Match 2

Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the first group's
 subexpression, which is the matched expression itself, and not the regex pattern.

 What would (abc|xyz)\1 match?
#"abc" or "xyz", followed by the same thing


More useful special sequences are \d, \s, and \w.
These match digits(\d), whitespace(\s), and word(\w) characters respectively.

In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w
matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - 
mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.

Example:

import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")
if match:
    print("Match 1")     <-- print

match = re.match(pattern, "1, 23, 456!")
if match:
    print("Match 2")    #no print

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")    #no print

#(\D+\d) matches one or more non-digits followed by a digit.

Which pattern would NOT match "123!456!"?
#(\D+\s?)+


Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively.
The sequence \b matches the empty string between \w and \W characters, 
or \w characters and the beginning or end of the string. Informally, 
it represents the boundary between words.
The sequence \B matches the empty string anywhere else.

Example:

import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
    print ("Match 1")           <-- print

match = re.search(pattern, "We s>cat<tered?")
if match:
    print ("Match 2")           <-- print

match = re.search(pattern, "We scattered.")
if match:
    print ("Match 3")           #no print


#\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.

Which pattern would match 'SPAM!' in a search?
# \AS...\b.\Z


####################################################################

Email Extraction


To demonstrate a sample usage of regular expressions, lets create a program 
to extract email addresses from a string.
Suppose we have a text that contains an email address:

str = "Please contact info@sololearn.com for assistance"

PY
Our goal is to extract the substring "info@sololearn.com".
A basic email address consists of a word and may include dots or dashes.
This is followed by the @ sign and the domain name (the name, a dot, and
 the domain name suffix).
This is the basis for building our regular expression.

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"

PY
[\w\.-]+ matches one or more word character, dot or dash.
The regex above says that the string should contain a word (with dots and
dashes allowed), followed by the @ sign, then another similar word, then a dot and another word.

Our regex contains three groups:

1 - first part of the email address.
2 - domain name without the suffix.
3 - the domain suffix.

Putting it all together:

import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())

#info@sololearn.com

In case the string contains multiple email addresses, we could use the 
re.findall method instead of re.search, to extract all email addresses.
The regex in this example is for demonstration purposes only.
A much more complex regex is required to fully validate an email address.

###################################################################


Problem
Phone Number Validator


You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid
You can use a regular expression to check if the input matches the given pattern.

SOLUTION:

import re
#your code goes here

num = input()

pattern = r"[1|8|9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"

if re.search(pattern, num):
    print("Valid")
else:
    print("Invalid")


###################################################################

The Zen of Python


Writing programs that actually do what they are supposed to do is 
just one component of being a good Python programmer.
It's also important to write clean code that is easily understood,
even weeks after you've written it.

One way of doing this is to follow the Zen of Python, a somewhat
tongue-in-cheek set of principles that serves as a guide to programming
the Pythoneer way. Use the following code to access the Zen of Python.
Result:
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Run the code and see how it works!

Some lines in the Zen of Python may need more explanation.
Explicit is better than implicit: It is best to spell out exactly
 what your code is doing. This is why adding a numeric string to
  an integer requires explicit conversion, rather than having it 
  happen behind the scenes, as it does in other languages.
Flat is better than nested: Heavily nested structures (lists of lists, 
    of lists, and on and on…) should be avoided.
Errors should never pass silently: In general, when an error occurs,
you should output some sort of error message, rather than ignoring it.

There are 20 principles in the Zen of Python, but only 19 lines of text.
The 20th principle is a matter of opinion, but our interpretation is 
that the blank line means "Use whitespace".
The line "There should be one - and preferably only one - obvious way to do it"
 references and contradicts the Perl language philosophy that there should be
  more than one way to do it.

  PEP


Python Enhancement Proposals (PEP) are suggestions for improvements
 to the language, made by experienced Python developers.
PEP 8 is a style guide on the subject of writing readable code.
 It contains a number of guidelines in reference to variable names,
  which are summarized here:

- modules should have short, all-lowercase names;
- class names should be in the CapWords style;
- most variables and function names should be lowercase_with_underscores;
- constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
- names that would clash with Python keywords (such as 
    'class' or 'if') should have a trailing underscore.

PEP 8 also recommends using spaces around operators and
 after commas to increase readability.
However, whitespace should not be overused. For instance, 
avoid having any space directly inside any type of brackets.

However, whitespace should not be overused.
For instance, avoid having any space directly inside any type of brackets.

PEP 8

Other PEP 8 suggestions include the following:
- lines shouldn't be longer than 80 characters;
- 'from module import *' should be avoided;
- there should only be one statement per line.

It also suggests that you use spaces, rather than tabs, to indent.
 However, to some extent, this is a matter of personal preference. 
 If you use spaces, only use 4 per line. 
 It's more important to choose one and stick to it.

The most important advice in the PEP is to ignore it when it makes
 sense to do so. Don't bother with following PEP suggestions when 
 it would cause your code to be less readable;
  inconsistent with the surrounding code; or not backwards compatible.
However, by and large, following PEP 8 will greatly enhance the quality
 of your code.
Some other notable PEPs that cover code style:
PEP 20: The Zen of Python
PEP 257: Style Conventions for Docstrings

###################################################################


Function Arguments


Python allows to have function with varying number of arguments.
Using *args as a function parameter enables you to pass an arbitrary 
number of arguments to that function. The arguments are then accessible
 as the tuple args in the body of the function.

Example:

The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)
#1
#(2, 3, 4, 5)

The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.



###################################################################


Default Values


Named parameters to a function can be made optional by giving them 
a default value. These must come after named parameters without a 
default value.

Example:
def function(x, y, food="spam"):
    print(food)

function(1, 2)
function(3, 4, "egg")

#spam
#egg

#In case the argument is passed in, the default value is ignored.
#If the argument is not passed in, the default value is used.


###################################################################


Function Arguments


**kwargs (standing for keyword arguments) allows you to handle named
 arguments that you have not defined in advance.
The keyword arguments return a dictionary in which the keys are the
 argument names, and the values are the argument values.

Example:
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

#{'a': 7, 'b': 8}

a and b are the names of the arguments that we passed to the function call.
The arguments returned by **kwargs are not included in *args.

###################################################################


Tuple Unpacking


Tuple unpacking allows you to assign each item in an iterable (often a tuple) to a variable.
Example:
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
#1
#2
#3

This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side
 forms the tuple (b, a) which is then unpacked.


A variable that is prefaced with an asterisk (*) takes all values from the iterable that are 
left over from the other variables.
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

What is the output of this code?
a, b, c, d, *e, f, g = range(20)
print(len(e))
#14


###################################################################

Ternary Operator


Conditional expressions provide the functionality of if statements 
while using less code. They shouldn't be overused, as they can easily 
reduce readability, but they are often useful when assigning variables.
Conditional expressions are also known as applications of the ternary operator.
Example:

a = 7
b = 1 if a >= 5 else 42
print(b)
#1

a = 7
b = 1 if a >= 8 else 42
print(b)
#42

The ternary operator checks the condition and returns the corresponding value.
In the example above, as the condition is true, b is assigned 1. If a was less than 5,
 it would have been assigned 42.
Another example:

status  = 1
msg = "Logout" if status == 1 else "Login"

print(msg)
#Logout

The ternary operator is so called because, unlike most operators, it takes three arguments.

###################################################################

Problem

Ternary Operator


You are given a program for a bank card withdrawal system: 
it takes the account and the amount that the user wants to withdraw, 
then outputs the remaining money. If the requested cash is greater 
than the balance, the program outputs "Error".
The bank wants to set a minimal value of $500 for withdrawal.
 Modernize the program so that it will output the same "Error" 
 if the requested money is less than $500.

Sample Input
4500
300

Sample Output
Error
As with other operators, you can chain multiple conditions with the ternary operator.

SOLUTION:


balance = int(input())
to_cash = int(input())

#change the code
money_left = balance-to_cash if (to_cash>=500 and to_cash <=balance) else "Error"

print(money_left)


###################################################################

else


The else statement is most commonly used along with the if statement,
but it can also follow a for or while loop, which gives it a different meaning.
With the for or while loop, the code within it is called if the loop finishes
normally (when a break statement does not cause an exit from the loop).

Example:

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1") <-- Print

for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2") <-- No print

#Unbroken 1

The first for loop executes normally, resulting in the printing of "Unbroken 1".
The second loop exits due to a break, which is why it's else statement is not executed.

The else statement can also be used with try/except statements.
In this case, the code within it is only executed if no error occurs in the try statement.
Example:

try:
    print(1)   <-- Print
except ZeroDivisionError:
    print(2)
else:
    print(3)   <-- Print

try:
    print(1/0)
except ZeroDivisionError:
    print(4)   <-- Print
else:
    print(5) 

#1
#3
#4


###################################################################

__main__


Most Python code is either a module to be imported, or a script that does something.
However, sometimes it is useful to make a file that can be both imported as a module 
and run as a script.
To do this, place script code inside if __name__ == "__main__".
This ensures that it won't be run if the file is imported.

Example:

def function():
    print("This is a module function")

if __name__=="__main__":
    print("This is a script")


#This is a script


When the Python interpreter reads a source file, it executes all
 of the code it finds in the file. Before executing the code,
  it defines a few special variables.
For example, if the Python interpreter is running that module (the source file)
 as the main program, it sets the special __name__ variable to have a value "__main__".
 If this file is being imported from another module, __name__ will 
 be set to the module's name.


__main__


If we save the code from our previous example as a file called sololearn.py, 
we can then import it to another script as a module, using the name sololearn.
sololearn.py

some_script.py
import sololearn

sololearn.function()
PY
Result:
>>>
This is a module function
>>>
Basically, we've created a custom module called sololearn, and then used it in another script.


###################################################################

Major 3rd-Party Libraries


The Python standard library alone contains extensive functionality.
However, some tasks require the use of third-party libraries.
 Some major third-party libraries:

***Django: The most frequently used web framework written in Python, 
Django powers websites that include Instagram and Disqus.
It has many useful features, and whatever
features it lacks are covered by extension packages.
***CherryPy and 
***Flask are also popular web frameworks.

For scraping data from websites, the library 

***BeautifulSoup is very useful, and leads to better results than building
your own scraper with regular  expressions.

While Python does offer modules for programmatically accessing websites,
 such as *urllib, they are quite cumbersome to use.
 Third-party library requests make it much easier to use HTTP requests.


Major 3rd-Party Libraries


A number of third-party modules are available that make it much easier to carry 
out scientific and mathematical computing with Python.
The module 
***matplotlib allows you to create graphs based on data in Python.
The module 
***NumPy allows for the use of multidimensional arrays that are much 
faster than the native Python solution of nested lists. It also contains functions to
 perform mathematical operations such as matrix transformations on the arrays.
The library 
***SciPy contains numerous extensions to the functionality of NumPy.

Python can also be used for game development.
Usually, it is used as a scripting language for games written in other languages,
 but it can be used to make games by itself.
For 3D games, the library 
***Panda3D can be used. For 2D games, you can use 
***pygame.


###################################################################


Packaging


In Python, the term packaging refers to putting modules you have written 
in a standard format, so that other programmers can install and use them with ease.

This involves use of the modules 
***setuptools and 
***distutils.

The first step in packaging is to organize existing files correctly.
 Place all of the files you want to put in a library in the same parent directory. 

 This directory should also contain a file called __init__.py,

 which can be blank but must be present in the directory.

This directory goes into another directory containing the readme and license, 
as well as an important file called setup.py.

Example directory structure:
SoloLearn/
   LICENSE.txt
   README.txt
   setup.py
   sololearn/
      __init__.py
      sololearn.py
      sololearn2.py

You can place as many script files in the directory as you need.

Packaging


The next step in packaging is to write the setup.py file.
This contains information necessary to assemble the package so it can be uploaded to
 PyPI and installed with pip (name, version, etc.).
Example of a setup.py file:
from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)
After creating the setup.py file, upload it to PyPI, or use the command line to create
 a binary distribution (an executable installer).
To build a source distribution, use the command line to navigate to the directory containing
setup.py, and run the command python setup.py sdist.
Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary
distribution.

Use python setup.py register, followed by python setup.py sdist upload to upload a package.

Finally, install a package with python setup.py install.


Packaging


The previous lesson covered packaging modules for use by other Python programmers. 
However, many computer users who are not programmers do not have Python installed. 
Therefore, it is useful to package scripts as executable files for the relevant platform,
such as the Windows or Mac operating systems. This is not necessary for Linux, as most Linux
 users do have Python installed, and are able to run scripts as they are.

For Windows, many tools are available for converting scripts to executables. 
For example, 
***py2exe, can be used to package a Python script, along with the libraries it requires, 
into a single executable.
***PyInstaller and 
***cx_Freeze serve the same purpose.

For Macs, use 
***py2app, PyInstaller or cx_Freeze.

#############################################################################################


What is the output of this code?
def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)
#8

What is sum of the numbers printed by this code?
for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)
#9

Fill in the blanks to swap the variable values with one single statement.
a = 7

b = 42

a , b = b,a

#############################################################################################



Problem

Adding Words


You need to write a function that takes multiple words as its argument and returns a 
concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

Sample Input
this
is
great

Sample Output
this-is-great
Recall, using *args as a function parameter enables you to pass an arbitrary number of 
arguments to that function.

SOLUTION:


def concatenate(*args):
    
    #return match

    return '-'.join(args)

print(concatenate("I", "love", "Python", "!"))

#############################################################################################