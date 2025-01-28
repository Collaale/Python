Python Data Structures


Almost every program uses data.
Organizing, managing and storing data is important as it enables easier access and efficient modifications.

Data Structures allow you to store and manage your data.

Python has a number of built-in data structures:
- Strings
- Lists
- Dictionaries
- Tuples
- Sets

During this course, we will learn about these data structures, use them to store data and see their real-life applications.
If you are not familiar with the basics of Python, please complete our Python for Beginners course first.

Python Data Structures


In addition to the built-in data structures, Python allows you to create your own data structures, enabling you to have full control over their functionality.

The most prominent data structures are:
- Stacks
- Queues
- Trees
- Linked Lists
These data structures have many uses in popular algorithms. We will learn about them in the coming modules.



Strings


Strings are used to store text, and are one of the simplest and most used data structures.

Any text between two single or double quotation marks is a string.

For example:
x = "Hello world"
print(x)
#Hello world

The variable x now represents a string.


Special Characters


There are a number of special characters that can be used in strings.
\n  represents a new line:

print('One\nTwo\nThree')
One
Two
Three



Similarly, \t represents a tab.
If you want to include a single quote in a single-quoted string (or a double quote in a double-quoted string), you need to escape it using a backslash:

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')
#Brian's mother: He's not an angel. He's a very naughty boy!

The backslash is also called the escape character.


Accessing Strings


Strings can be thought of as a sequence of characters. Each character in the string has its unique position (or index).

You can access a character of a string using its index:

x = "Hello"
print(x[2])
#l

The index starts from 0, meaning that the first character has the index 0.


Accessing Strings


You can also use negative indices, which access the characters of the string counting from the end.
For example:

x = "Hello"
print(x[-1])  
#o

The code above accesses the last character of the string.


22 Comments
Accessing Strings
What is the output of this code?

x = "awesome"
print(x[-2])
#m


Accessing Strings


You can loop through the characters in a string using a for loop:


x = "Hello"
for c in x:
    print(c)

H
e
l
l
o


Problem
Accessing Strings


You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4
There are 4 vowels in the given text.

SOLUTION:

#your code goes here

phrase = input()
count = 0
for c in phrase:
    if (c == "a" or
        c == "e" or
        c == "i" or
        c == "o" or
        c == "u" ):
      
        count += 1

print(count)

#############################################################################


String Operations


The in operator can be used to check if a string is part of another string.


For example:

x = "I love Python"
if "love" in x:
   print("Yes")
 
#Yes

The not in operator can be used to check if a string is not part of another string.


Strings can be added together (also called concatenation):
print("Spam" + 'eggs')

#Spameggs


Strings can also be multiplied by integers. This produces a repeated version of the original string.

print("spam" * 3)

print(4 * '2')
#spamspamspam
#2222

Strings can't be multiplied by other strings. Strings also can't be multiplied by floats, even if the floats are whole numbers.


#############################################################################


Problem
String Operations


Let's test your coding skills! 
Take a string as input and output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string.

Sample Input:
data

Sample Output:
d
aa
ttt
aaaa
Hint: Use a loop to iterate over the string, keeping the position number of the current iteration in a variable. Then use multiplication to repeat the letters.


SOLUTION:

#your code goes here

inp = input()
print()
i = 0
while (i < len(inp)):
    print(inp[i] * (i+1))
    i += 1


String Operations
Guess the output:

a = "abra"
b = "cad"
x = a+b+a
print(x)
#abracadabra


String Functions


String have many useful functions:
count(str) returns how many times the str substring appears in the given string.
upper() converts the string to uppercase.
lower() converts the string to lowercase.
replace(old, new) replaces all occurrences of old with new.
len(str) returns the length of the string (number of characters).

Take a look at this code for examples:

x = "This is some text"

print(x.count("s"))
print(x.upper())
print(x.lower())
print(x.replace("some text", "awesome"))
print(len(x)) 

3
THIS IS SOME TEXT
this is some text
This is awesome
17


Note, that these functions return a new string with the corresponding manipulation.

#################################################################################################

Problem

Manipulating Strings


You are making a text editor and need to implement find/replace functionality.
The code declares a text string. You need to take two string inputs, which represent the substring to find and what to replace it with in the text.
Your program needs to output the number of replacements made, along with the new text.

For example, for the given text "I weigh 80 kilograms. He weighs 65 kilograms.":

Sample Input
kilograms
kg

Sample Output
2
I weigh 80 kg. He weighs 65 kg.

The program replaced 2 occurrences of the word kilograms with kg.
Note, that you need to output the number of replacements, before the replaced text.


SOLUTION?

text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."

f = input()
r = input()

co = text.count(f)
re = text.replace(f,r)

print(co)
print(re)


###################################################################################################################


Problem
Letter Frequency


You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

Explanation : The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
Division result is a float. Use the int() function to convert the result to an integer.

#your code goes here

t = input()
l = input()


le = len(t)
co = t.count(l)

pe = ((co / le) * 100)

print(int(pe))


#####################################################################################################################


Lists


Lists are used to store multiple elements, each corresponding to an index.

They are created using square brackets.
For example:

names = ["James", "Tom", "Amy"] 


The names list contains three strings. Each element of the list can be accessed using its index:

This will output the 2nd element of the list.

names = ["James", "Tom", "Amy"]
print(names[1])
#Tom


The first list item's index is 0.



Lists


Lists can be used to represent a collection of data, for example ages of people, monthly growth rates of stocks, etc.

Lists can also be nested to represent 2D grids, such as matrices:


m = [
    [1,2,3],
    [4,5,6]
    ]
    
print(m[1][2]) 

#6


The code above outputs the 3rd item of the 2nd row.


A matrix-like structure can be used in cases where you need to store data in row-column format.



List Operations


Similar to strings, we can use the in and not in operators to check if an element is part of the list:

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#True
#True
#False

The len() function can be used to return the number of elements in a list.


Loops


Similar to strings, we can loop through the elements of a list using a loop:

x = [2, 4, 6, 8]

for n in x:
   print(n)

2
4
6
8


n will represent the current list item during each iteration.



################################################################################################

List Functions


Lists support the following functions:
append(item) adds an item to the end of the list.
insert(index, item) adds an item at the given index in the list.
remove(item) removes an item from the list.
pop(index) removes the item at the given index.
count(item) returns a count of how many times an item occurs in the list.

Some examples:
Elements that are after the inserted item are shifted to the right.

x = [2, 4, 6]
x.append(8)
x.remove(4)
x.insert(0, 8)

print(x)

print(x.count(8)) 

[8, 2, 6, 8]
2

Elements that are after the inserted item are shifted to the right.


List Functions


reverse() reverses items in the list.
sort() sorts the list. By default, the list is sorted ascending. You can specify reverse=True as the parameter, to sort descending.
max(list) returns the maximum value.
min(list) returns the minimum value.

Some examples:

x = [2, 4, 6, 8]
x.reverse()
print(x)

x.sort()
print(x)

print(min(x))
print(max(x))

[8, 6, 4, 2]
[2, 4, 6, 8]
2
8


Note, that the reverse() and sort() functions change the list they are called on.


List Functions
What is the output of this code?

x = [8, 5, 42, 11, 20, 4]
x.sort()
print(max(x)-min(x)+x[2])
#46

#################################################################################################

List Comprehensions


List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
For example, we can do the following:


# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)

#[0, 1, 8, 27, 64]


List comprehensions are inspired by set-builder notation in mathematics.


List Comprehensions


A list comprehension can also contain an if statement to enforce a condition on values in the list.
Example:


evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

[0, 4, 16, 36, 64]


List Comprehensions
Create a list of multiples of 3 from 0 to 20.
a = [i for i in range(20) if i%3==0]


########################################################################################################

PROBLEM

Average Word Length


Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5
Strings have a split() method, which returns the string split into a list, with the given separator. By default, the separator is a space, so calling 
split() will return a list containing the words of the string as items.


SOLUTION:

text = input()

sumLW = 0
word = 1

for sw in text:
    if sw != " ":
        sumLW += len(sw) 
    elif sw == " ":
        word += 1
print(sumLW/word)

########################################################################################################


Dictionaries


We saw how lists allow us to store elements with their corresponding indices.
The indices in a list are automatically set. But what if we need to set our own index?

Dictionaries are another collection type and allow us to map arbitrary keys to values.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

Example:
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

#24
#42

Each element in a dictionary is represented by a key:value pair.


Dictionaries


You can use strings, integers, booleans, and any other immutable type as dictionary keys.
This means that you cannot use lists or dictionaries as keys:

bad_dict = {
    [1, 2, 3]: "one two three", 
}


Traceback (most recent call last):
  File "file0.py", line 1, in <module>
    bad_dict = {
TypeError: unhashable type: 'list'


Dictionaries


To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

Example:

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

#True
#False
#True


Dictionaries


A useful dictionary function is get(). It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead.

Example:

pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True    : False, 
  12      : "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))

#[2, 3, 4]
#42
#not found

To determine how many items a dictionary has, use the len() function.



###################################################################################

Tuples


Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.

Example:
words = ("spam", "eggs", "sausages")

You can access the values in the tuple with their index, just as you did with lists:

words = ("spam", "eggs", "sausages",)
print(words[0])
#spam

Like lists and dictionaries, tuples can be nested within each other.

Fill in the blanks to create a list, dictionary, and tuple:

# list
list = ["one", "two"]


# dictionary 
dict = {1:"one", 2:"two"}


# tuple 
tp = ("one", "two")


Tuples


An advantage of tuples over lists is that they can be used as keys for dictionaries (because they are immutable):

dict = {
    ("David", 42): "red",
    ("Bob", 24): "green"
}

print(dict[("Bob", 24)]) 
green


Tuples are faster than lists, but they cannot be changed.


What is the result of this code?

tuple = (1, (1, 2, 3))
print(tuple[1])
#(1, 2, 3)

Tuple Unpacking


Tuple unpacking allows you to assign each item in a collection to a variable.

Example:

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

1
2
3

This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) which is then unpacked.


Tuple Unpacking


A variable that is prefaced with an asterisk (*) takes all values from the collection that are left over from the other variables.

Example:

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

1
2
[3, 4, 5, 6, 7, 8]
9

c will get assigned the values 3 to 8.


###########################################################################################


Sets


Sets are collections of unordered items that are unique.

They are created using curly braces, and, due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, rather than part of a list.
Sets cannot contain duplicate elements.


num_set = {1, 2, 3, 4, 5}

print(3 in num_set)

#True


Sets cannot contain duplicate elements.


Sets


You can use the add() function to add new items to the set, and remove() to delete a specific element:


nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

{1, 2, 3, 4, 5, 6}
{1, 2, 4, 5, 6, -7}

Duplicate elements will automatically get removed from the set.


Sets


Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
Tap Try It Yourself to play around with the code!


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(first & second) #{4, 5, 6}
print(first - second) #{1, 2, 3}
print(second - first) #{8, 9, 7}
print(first ^ second) #{1, 2, 3, 7, 8, 9}


{1, 2, 3, 4, 5, 6, 7, 8, 9}
{4, 5, 6}
{1, 2, 3}
{8, 9, 7}
{1, 2, 3, 7, 8, 9}

#############################################################################

Data Structures


As we have seen in the previous lessons, Python supports the following collection types: Lists, Dictionaries, Tuples, Sets.

Here are some general guidelines for choosing the correct data structure:


***********- Use a dictionary, when you need a logical association between a key:value

***********- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.

***********- Use a set if you need uniqueness for the elements.

***********- Use tuples when your data cannot/should not change.


Many times, a tuple is used in combination with a dictionary, for example, a tuple can represent a key, because it's immutable



#############################################################################


Problem
Ticket Office


You are analyzing sales data from a ticket office.
The ticket for an adult is $20, while the ticket for a child under 18 is $5.
The data you are given is in a dictionary format, where the keys are the sold ticket numbers, and the values are the customer ages.
For example, "123-08": 24 means that the ticket was bought a 24 year old.
Your goal is to calculate how much more money the office would make if it would change the ticket discount age to the given input.
So, your program needs to take an integer as input and output the percentage of revenue growth, if the discount was given to people under that age.

For example, if the office made $15000 with the original discount age, and would make $18000 with 14 as the discount age, then the growth would be ((18000-15000)/15000)*100 = 20%

So, for the input 14, your program should output 20. The output should be an integer (use int() to convert the result).
To iterate over the values of a dictionary, you can use the .values() function:
for value in data.values()


SOLUTION:

data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, 
    "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27,
    "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9,
    "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14,
    "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10,
    "87-456": 8, "87-430": 40
}
age = int(input())
#your code goes here

aU    = 0
aD    = 0
count = 0
adlt  = 0
cild  = 0
vlrDef= 0
vlrPer= 0
perc  = 0

for value in data.values():
    count += 1 
    if (value >= age):
        aU += 1
    else:
        aD += 1 

    if (value > 17):
        adlt += 1
    else:
        cild += 1

vlrDef = (adlt*20) + (cild*5)
vlrPer = (aU*20) + (aD*5)

perc = ((vlrPer-vlrDef)/vlrDef)*100
print(int(perc))
#print(int(aU))
#print(int(aD))
#print(int(count))
#print("++++++++++++++++")
#print(int(adlt))
#print(int(cild))
#print(int(vlrDef))
#print(int(vlrPer))


##################################################################################################


User-Defined Data Structures


In the previous modules we have seen the built-in data structures in Python, which include Lists, Dictionaries, Tuples and Sets.

Some applications require additional functionality when working with data, for example, word processors have an undo-redo function,
task schedulers need queuing mechanisms, maps need to find the shortest path, etc.
In these cases we need to define our own data structures that provide the required functionality.

Some of the most popular data structures are:
- Stacks
- Queues
- Linked Lists
- Graphs
We will implement the above data structures and use them to solve popular problems.


Stack


A stack is a simple data structure that adds and removes elements in a particular order.
Every time an element is added, it goes on the "top" of the stack. Only an element at the top of the stack can be removed,
 just like a stack of plates. This behavior is called LIFO (Last In, First Out).contentImageTerminology
Adding a new element onto the stack is called push.
Removing an element from the stack is called pop.

Applications
Stacks can be used to create undo-redo functionalities, parsing expressions (infix to postfix/prefix conversion), and much more.
A stack can be implemented using a list in Python.


Stack in Python


Let's define and implement the Stack class with its corresponding push, pop, is_empty and print_stack methods.

We will use a list to store the data.

class Stack:
    def __init__(self):
        self.items = []  
  
    def is_empty(self):
        return self.items == []
  
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)
    
    def print_stack(self):
        print(self.items)
    
s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.print_stack()

s.pop()
s.print_stack()

['c', 'b', 'a']
['b', 'a']

As you can see, it's easy to create a stack using a list.
We use a list called items to store our elements.
The push method adds an element at the beginning of the list, while the pop method removes the first element of the list.
Play around with the code and see the Stack working in action!

#################################################################################################

Queue


A queue is similar to a stack, but defines a different way to add and remover elements.
The elements are inserted from one end, called the rear, and deleted from the other end, called the front.
This behavior is called FIFO (First in First Out).contentImage

Terminology
The process of adding new elements into the queue is called enqueue.
The process of removal of an element from the queue is called dequeue.

Applications
Queues are used whenever we need to manage objects in order starting with the first one in.
Scenarios include printing documents on a printer, call center systems answering people on hold, and so on.


Python lists are the easiest way to implement a queue functionality.


Queue in Python


Let's implement the Queue class with it's corresponding enqueue, dequeue, is_empty and print methods.

We will use a list to store the elements.


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()


['42', 'b', 'a']
['42', 'b']



The enqueue method adds an element at the beginning of the list, while the dequeue method removes the last element.
Play around with the code and see the Queue working in action!


#######################################################################################

Linked List


A linked list is a sequence of nodes where each node stores its own data and a link to the next node.
One node links to another forming what can be thought of as a linked chain:contentImageThe first node is called the head, and it's used as the starting point for any iteration through the list. The last node must have its link pointing to None to determine the end of the list.

Unlike stacks and queues, you can insert and remove nodes in any position of the linked list (similar to a standard list).

Applications
Linked lists are useful when your data is linked. For example when you need undo/redo functionality, 
the nodes can represent the state with links to the previous and next states.
 Another example would be a playlist of music, where each clip is linked with the next one.
Linked lists can also be used to create other data structures, such as stack, queues and graphs.


Linked List in Python


Each node will include data and the link to the next node.

Let's start by creating the Node class:
class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next


Now we can create the LinkedList class with the corresponding methods:

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)      

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())

9 => 5 => 8 => 
8

The add_at_front() method adds a new Node as the head of the list and links the previous head to it.
The add_at_end() method iterates to the end of the list using a while loop and adds the new node as the link of the last node.
Run the code and see how it works!

###################################################################################################################


Problem
Linked List


You are making a Music Player, which allows you to create a playlist of tracks.
The given code defines Player and Track classes, where the Player is a linked list, chaining together Track objects.
The code takes a number of tracks from user input and adds them to the playlist.

You need to iterate over the linked list and output all the tracks in the playlist in the order of playback.
Use a while loop to iterate over the linked list.


SOLUTION:

class Track:
    def __init__(self, title, next):
        self.title = title
        self.next = next

class Player:
    def __init__(self):
        self.head = None

    def add(self, title):
        if not self.head:
            self.head = Track(title, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Track(title, None)


p = Player()
while True:
    x = input()
    if x == 'end':
        break
    p.add(x)

#your code goes here

n = p.head

while n != None:
    print(n.title)
    n = n.next



#################################################################################



Linked List in Python

Fill in the blanks to iterate over the linked list named myList and output the data of each node.


x = myList.head
while x != None:
    print(x.data)
    x = x.next

#################################################################################



Graph


Graphs are used to represent many real-life applications like networks, transportation paths of a city, and social network connections.

A graph is a set of connected nodes where each node is called a Vertex and the connection between two of them is called an Edge.

Here is an example graph:

contentImageThis can represent, for example, connections on a social network, where each Vertex represents a person and the Edges represent connections.
Tap Continue to check out the implementation of the graph in Python!


Graph in Python


A graph can be represented using a square matrix, where each element represents the edges: 0 indicates no edge, while 1 indicates an edge. The rows and columns represent the vertices.

For example:
0 1 1
1 0 0
1 0 0
 
The matrix above represents a graph with 3 vertices (that's why it's a 3x3 matrix).
The 1s represent the edges. There are 2 edges: the 1st vertex is connected with the 2nd and 3rd.
There are four 1s in the matrix, because if A is connected with B, then B is connected to A.
This type of matrix is called an adjacency matrix, because it shows if the corresponding vertices are adjacent or not.

Graph in Python


Let's implement the Graph class:

class Graph(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 1 
            self.adj[dest-1][orig-1] = 1 
        
    def remove_edge(self, orig, dest): 
        if orig > self.size or dest > self.size or orig < 0 or dest < 0: 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][dest-1] = 0 
            self.adj[dest-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(4) 
G.add_edge(1, 3) 
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()



0   0   1   0
0   0   0   1
1   0   0   1
0   1   1   0

We store the matrix in a two-dimensional list, called adj.
The __init__ method creates the adj matrix with the given size (number of vertices) and initializes all values to zeros.
The add_edge() method is used to add an edge by setting the corresponding values to 1.
Similarly, the remove_edge() method sets the values to 0.
Run the code to see their implementation and the whole program in action!


#############################################################################################


Problem
Balanced Parentheses


Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.

Given an expression as input, we need to find out whether the parentheses are balanced or not.
For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.

The problem can be solved using a stack.
Push each opening parenthesis to the stack and pop the last inserted opening parenthesis whenever a closing parenthesis is encountered.
If the closing bracket does not correspond to the opening bracket, then stop and say that the brackets are not balanced.
Also, after checking all the parentheses, we need to check the stack to be empty -- if it's not empty, then the parentheses are not balanced.

Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not.

Sample Input:
(a( ) eee) )

Sample Output:
False
You can use a simple list for a stack. Use list.insert(0, item) to push on the stack, and list.pop(0) to pop the top item. You can access the top element of the stack using list[0].


SOLUTION:


def balanced(expression):
    #your code goes here
    bracket_stack = []
    for char in expression:
        if char == "(":
            bracket_stack.insert(0, char)
        elif char == ")":
            try:
                bracket_stack.pop(0)
            except IndexError:
                return False
    
    return bracket_stack == []


print(balanced(input()))




