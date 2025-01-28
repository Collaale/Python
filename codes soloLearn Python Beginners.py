
Want to build a slick website? Develop a video game? Or maybe create an artificial intelligence?
 Python’s got you covered, and then some. Python is a high-level programming language, with a ton 
 of applications.

It’s seriously flexible and accessible, which makes it popular with some of the world's biggest 
(and coolest) organizations–think Google, NASA, Disney...*whispers* even the CIA.

In this course, we’ll cover the basic concepts of Python, as well as build real-life projects and
 solve different coding challenges!

We will be learning Python version 3, which is the most recent major version of Python.


Data Types


Before we go any further, it’s a good idea to introduce the main types of data that we use in Python.
 Each value in Python has a type.

Text, like "Hello world", is called a string.
Whole numbers are called integers.
And numbers with a decimal point are called floats.

Now, we’ve already encountered strings and integers, so you know what that means...Time to float!

Some examples of numbers that are represented as floats are 0.5 and -7.8237591.


So we know what floats are, they’re numbers with a decimal, but how do we produce them?

Well, we can produce a float by dividing any two integers.
Or we can also run an operation on two floats, or on a float and an integer.

Like this:
A float can be added to an integer, because Python automatically converts the integer to a float.
Clever Python!


Exponentiation


Alright, that covers the very basic operations, addition, subtraction, multiplication, and division. 
You’re doing great!

It’s time to kick it up a notch and introduce exponentiation–which is what we call it when we raise 
one number to the power of another.

The exponentiation operation is performed using two asterisks. Like this:
You can chain exponentiations together. In other words, you can rise a number to multiple powers.

For example, 2**3**2.


print( 2**5 )
#32

print( 2**5**2 )
#33554432


Too easy? Yeah, thought so. How about exponentiation with floats! Because we can totally 
use floats in exponentiation.

Check it out. The following code will result in the square root of 9:


print( 9 ** (1/2) )
#3.0


########################################################################################################

Exponentiation


Did you know that there are more bacteria cells in your body than cells that make up your body? Weird!

A bacteria culture starts with 500 bacteria and doubles in size every hour.
Which means, after 1 hour the number of bacteria is 1000, after 2 hours - 2000, and so on.

Let’s calculate and output the number of bacteria that will be in the culture after 24 hours.
The formula to calculate the bacteria after N hours will be: 500*2ᴺ



SOLUTION:

#your code goes here
print(500*2**24)


########################################################################################################


Quotient


Floor division is done using two forward slashes and is used to determine the quotient of a division.
Wait! What?! "Floor Division"? "Quotient"?

Quotient just means the quantity produced by the division of two numbers.

And Floor division is just like a normal division operation except that it returns the largest 
possible integer. This integer is either less than or equal to the normal division result.

For example:
The code above will output 3, because 6 goes into 20 three times, and is the largest possible integer.
You can also use floor division on floats, and the result will always be a float.

print(20 // 6) 
#3

The code above will output 3, because 6 goes into 20 three times, and is the largest possible integer.
You can also use floor division on floats, and the result will always be a float.


Remainder


Ahh those pesky remainders. But, they’re not so pesky in Python. 
We can use the modulo operator–which is carried out with a percent symbol (%)
–to get the remainder of a given division.

For example:
All numerical operators can also be used with floats.

print(20 % 6)
#2

print(1.25 % 0.5) 
#0.25

########################################################################################################

Problem

Quotient & Remainder


Random task! You need to calculate the number of hours in 888 minutes.

Your program needs to output the number of hours and then the number of remaining minutes, on separate lines.

For example, 72 minutes are equal to 1 hour and 12 minutes, so your program would output:
1
12

You can use floor division to find the number of hours, and the modulo operator to find the remaining minutes.
Use separate print() statements for each output.

SOLUTION:


#your code goes here
print(888//60)
#14

print(888%60)
#48

########################################################################################################

Problem
Flight Time


You need to calculate the flight time of an upcoming trip. You are flying from LA to Sydney, covering a

distance of 7425 miles, the plane flies at an average speed of 550 miles an hour.

Calculate and output the total flight time in hours.

Hint
The result should be a float.
Use the print statement to output the result.

SOLUTION

#your code goes here

print(7425/550)

#13.5


########################################################################################################

STRINGS

print("Python is fun!")

print('Always look on the bright side of life')


BACKSLASH

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')


Newlines


Ok, so we can generate text, but it’d be pretty hard to read 
if everything was on one single line, right?

To create a new line we use \n.

print('One\nTwo \nThree') 
#One
#Two 
#Three


Based on what we just learned, can you guess how we represent tab?

--> That’s right, it’s \t.


\n is useful, but it can be a bit of a pain if we’re trying to format lots of multiline text.

There’s another way though! Newlines are automatically added for strings created using three
quotes.

For example:

print("""this
is a
multiline
text""") 

#this
#is a
#multiline
#text


In Python math works with words as well as numbers.

So not only can we add integers and floats, but also strings, using something called 
concatenation, which can be done on any two strings. Like this:

print("Spam" + 'eggs')
#Spameggs

And it even works with numbers! Strings containing numbers are still added as strings
rather than integers. Like this:

print("2" + "2")
#22

But don’t try to add a string to a number! Even though they might look similar,
they are two different entities, so doing this will break the code and produce an error.



String Operations


You may not be able to add strings to integers, but you can multiply by them!

Multiplying a string by an integer, produces a repeated version of the original string.
 Like this:


print("spam" * 3)
#spamspamspam

print(4 * '2')
#2222

But don’t try to multiply a string by another string. This will just generate an error.
The same will happen if you try to multiply a string by a float, even if the float is a number.


What’s the output of this code?

print("42" + '5')
#425


########################################################################################################

Problem
Strings


You need to make a program for a leaderboard.
The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
1.
2.
3.
...
You can use the \n newline character to create line breaks, or, alternatively, create the
 desired output using three double quotes \"""\.



SOLUTION:

#your code goes here
for i in range(10):
    if i > 0:
        print(str(i)+".")


1.
2.
3.
4.
5.
6.
7.
8.
9.

 ########################################################################################################

 Variable Names


Naming your variables is pretty flexible. You can use letters, numbers, and underscores 
in variable names. But you can’t use special symbols, or start the name with a number.

Don’t forget, Python is a case sensitive language. Which means,
Lastname and lastname are two different variable names.

########################################################################################################


Input


What function would we use to get input from the user in Python? Drumroll please! That’s right,
 the input function! Python likes to keep things simple and intuitive.

So a game can ask for the user's name and age as input and then use them in the game.

The input function prompts the user for input, and returns what they enter as a string.

 Like this:

 x = input()
print(x)

Even if the user enters a number as input, it’s processed as a string.



name = input("Enter your name: ")

print("Hello, " + name) 

The prompt message tells the user what input the program is asking for – 
so it’s important that it’s clear.


SAMPLE
age = int(input())
print(age)  

SAMPLE
age = 42
print("His age is " + str(age))  

You can convert to float using the float() function.

When the input() function executes the program flow stops until a user
enters some value. Ball’s in your court user!



In-Place Operators


Ok moving on from input. Let’s talk in-place operators.

In-place operators let you write code like 'x = x + 3' more concisely, 
as 'x += 3'. And who doesn’t love to save time!

Check it out:
x = 2
print(x)

x += 3
print(x)


We can do the same thing possible with other operators like -, *, / and % as well.


In-Place Operators


These operators aren’t just useful for numbers, oh no, no, no. Got some Strings you
 want to simplify? Simplify away!

 x = "spam"
print(x)
#spam


x += "eggs"
print(x)
#spameggs


In-place operators can be used for any numerical operation
 (+, -, *, /, %, **, //). So many symbols, so many possibilities!




ProblemResults
Tip Calculator


When you go out to eat, you always tip 20% of the bill amount. But who’s 
got the time to calculate the right tip amount every time? Not you that’s
 for sure! You’re making a program to calculate tips and save some time.

Your program needs to take the bill amount as input and output the tip as
 a float.

Sample Input
50

Sample Output
10.0
Explanation: 20% of 50 is 10.
To calculate 20% of a given amount, you can multiply the number by 20 and 
divide it by 100: 50*20/100 = 10.0


SOLUTION:

bill = int(input())
#your code goes here
print(float(bill*.2))


###################################################################


Booleans


You’re making great progress! Well done! You’re definitely ready to meet another type in Python.

So we’ve met strings, integers and floats. Let’s add Booleans into the mix shall we?

Booleans can have two values: True and False.

We can create them by comparing values, for instance by using the equal operator ==. Like this:


my_boolean = True
print(my_boolean)
True

print(2 == 3)
False

print("hello" == "hello")
True

True
False
True


Be careful not to confuse assignment (one equals sign) with comparison (two equals signs).

But don’t worry, we’ll be talking more about this later.

x = 7

print(x != 8)
print(x > 5)
print(x < 2)
print(x >= 7)
print(x <= 7)

#True
#True
#False
#True
#True

Comparison operators are also called Relational operators.


############################################################################################


if Statements


Ok so our Boolean comparison has figured out if our statement is true or false, now what?

Well one thing you can do is use if statements to run code based on a certain condition, 
say, if the Boolean evaluates to True.

With If statements, if the condition evaluates to True, the statements are carried out.
Otherwise, they aren't carried out.

An if statement looks like this:

if condition:
   statements

Python uses indentation (that empty space at the beginning of a line) to delimit blocks of code.
 Depending on the program's logic, indentation can be mandatory. As you can see,
 the statements in the if should be indented.

if Statements


Still with us? Great!
Here’s an example if statement in action:

x = 42
if x > 5:
   print("x is greater than 5") 
#x is greater than 5

Since the condition of the if statement is True, the program outputs "x is greater than 5".
The colon at the end of the expression in the if statement is important, don’t leave it out.

num = 12
if num > 5:
   print("Bigger than 5")
   if num <= 47:
      print("Between 5 and 47")

#Bigger than 5
#Between 5 and 47

Indentation is used to define the level of nesting.


#######################################################################

else Statements


And we can totally do the same thing with statements that evaluate to false.
We just need a different statement. This is where the else statement comes in!

The else statement can be used to run some statements when the condition of the
 if statement is False.

As with if statements, the code inside the block needs to be indented.

x = 4
if x == 5:
   print("Yes")
else:
   print("No")

#No

The colon at the end else keyword is important, don’t leave it out.


But wait! Before you go trying to do the same fancy stuff with else statements as you can 
with if statements, be aware: every if condition block can have only one else statement.

So for us to make multiple checks, we need to chain if and else statements.

For example, the following program checks and outputs the num variable's value as text:


num = 3
if num == 1:
  print("One")
else: 
  if num == 2:
    print("Two")
  else: 
    if num == 3: 
      print("Three")
    else: 
      print("Something else")


#Three

elif Statements


Great! So now we can pack our code with lots of lovely if/else statements, right?
Well, maybe that’s not the best idea. Too many if/else statements make your code 
long and hard to read. Two things we definitely don’t want code to be.

The best way to solve this is the elif (short for else if) statement.
It’s a shortcut to use when chaining if and else statements, making the code shorter
and easier to read.

The same example from the previous part can be rewritten using elif statements:

num = 3
if num == 1:
  print("One")
elif num == 2:
  print("Two")
elif num == 3: 
  print("Three")
else: 
  print("Something else")


#Three

Much shorter and cleaner! And as you can see in that example, a series of if elif 
statements can have a final else block, which is called if none of the if or elif 
expressions is True.

The elif statement is equivalent to an else/if statement. It’s used to make the
 code shorter, more readable, and avoid indentation increase.


#####################################################################################

Problem
else Statement


You need to make a program to take a year as input and output "Leap year" 
if it’s a leap year, and "Not a leap year", if it’s not.

To check whether a year is a leap year or not, you need to check the following:
1) If the year is evenly divisible by 4, go to step 2. Otherwise, the year is NOT leap year.
2) If the year is evenly divisible by 100, go to step 3. Otherwise, the year is a leap year.
3) If the year is evenly divisible by 400, the year is a leap year. Otherwise, it is not a
leap year.

Sample Input
2000

Sample Output
Leap year

Use the modulo operator % to check if the year is evenly divisible by a number.


A year is called a leap year if it contains an additional day which makes the 
number of the days in that year is 366. This additional day is added in
February which makes it 29 days long.


SOLUTION:

year = int(input())
#your code goes here

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not a leap year")  
  else:
    print("Leap year")  
else:
  print("Not a leap year")

#########################################################################################

Boolean Logic


Now it’s time to level up our Booleans with some operators!

The Boolean and, or, not operators allow to check for multiple conditions in an if statement.

Let’s start with the and operator. It is True, if both conditions evaluate to True:
Boolean operators can be used in expression as many times as needed.

print( 1 == 1 and 2 == 2 )
True
print( 1 == 1 and 2 == 3 )
False
print( 1 != 1 and 2 == 2 )
False
print( 2 < 1 and 3 >  6 )
False

#True
#False
#False
#False

Boolean operators can be used in expression as many times as needed.

Boolean Or


Now onto the or operator.

The or operator is True if either (or both) of its conditions are True, and False 
if both conditions are False
Making sense? Great!
Besides values, you can also compare variables.

print( 1 == 1 or 2 == 2 )

print( 1 == 1 or 2 == 3 )

print( 1 != 1 or 2 == 2 )

print( 2 < 1 or 3 >  6 )

#True
#True
#True
#False

Making sense? Great!
Besides values, you can also compare variables.

Boolean Not


Finally, the not operator works a little differently. not takes just one argument,
 and inverts it.

The result of not True is False, and not False goes to True.
Like this:

You can chain multiple conditional statements in an if statement using the Boolean operators.

print(not 1 == 1)
#False

print(not 1 > 7)
#True

You can chain multiple conditional statements in an if statement using the Boolean operators.


#########################################################################################

while Loops


Here’s another time saver!

We can use the while loop to repeat a block of code multiple times.

For example, let's say we need to process multiple user inputs, so that each time the user
 inputs something, the same block of code needs to execute.

Here’s a while loop containing a variable that counts up from 1 to 5, at which point the loop
 terminates.

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

#1
#2
#3
#4
#5
#Finished!

During each loop iteration, the i variable gets incremented by one, until it reaches 5.

So, the loop will execute the print statement 5 times.
The code in the body of a while loop is executed repeatedly. This is called iteration.


while Loops


And even better, you can use multiple statements in a while loop!

Say you need to use an if statement to make decisions. Which is especially useful in things
 like games, where you might need to loop through a number of player actions and add or
  remove points to the player’s score.

Check out this code, which uses an if/else statement inside a while loop to separate the 
even and odd numbers in the range of 1 to 10:


x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1

#1 is odd
#2 is even
#3 is odd
#4 is even
#5 is odd
#6 is even
#7 is odd
#8 is even
#9 is odd



str(x) is used to convert the number x to a string, so that it can be used for concatenation.

Fill in the blanks to create a loop that increments the value of x by 2 and prints the even values.
x = 0

while  x <=20:
    print(x)
x += 2

#########################################################################################


break


Infinite loops may sound cool, but they’re not always useful.

To end a while loop prematurely, we can use a break statement.

For example, we can break an infinite loop if some condition is met:

i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")


#0
#1
#2
#3
#4
#Breaking
#Finished


while True is a short and easy way to make an infinite loop.

An example use case of break:
An infinite while loop can be used to continuously take user input. 
For example, you are making a calculator and need to take numbers from 
the user to add and stop, when the user enters "stop".

In this case, the break statement can be used to end the infinite loop when
the user input equals "stop".

Using the break statement outside of a loop causes an error.


continue


Another statement that can be used within loops is continue.
Unlike break, continue jumps back to the top of the loop, rather 
than stopping it. Basically, the continue statement stops the current 
iteration and continues with the next one.

For example:

i = 0
while i<5:
  i += 1
  if i==3:
    print("Skipping 3")
    continue
  print(i)

#1
#2
#Skipping 3
#4
#5

An example use case of continue:
An airline ticketing system needs to calculate the total cost for all tickets purchased.
The tickets for children under the age of 3 are free. We can use a while loop to iterate
through the list of passengers and calculate the total cost of their tickets.

Here, the continue statement can be used to skip the children.
Using the continue statement outside of a loop causes an error.


#########################################################################################


Problem


BMI Calculator


Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
 It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's
weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal
Weight is in kg, height is in meters.
Note, that height is a float.

SOLUTION:

#your code goes here


w = input()

h = input()

bmi = float(w) / (float(h)**2)


if bmi < 18.5:
    print("Underweight") 
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi > 30:
    print("Obesity")


#########################################################################################


LISTS:


We can create a list by using square brackets with commas separating items. Like this:

words = ["Hello", "world", "!"]  

In that example the words list contains three string items: hello, world and !

If you want to access a certain item in the list, you can do this by using its
index in square brackets. In our example, that would look like this:

For example:

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2]) 

#Hello
#world
#!

The first list item's index is 0, rather than 1, as you might expect.


But lists aren’t just for shopping!

We can do some pretty cool stuff with them in Python. For example,
we can use nested lists to represent 2D grids, such as matrices.

For example:

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    
print(m[1][2])  
#6

This is useful because a matrix-like structure can allow you to store data in
row-column format, like in ticketing programs, that need to store the seat numbers in 
a matrix, with their corresponding rows and numbers.

The code above outputs the 3rd item of the 2nd row.

Strings can be indexed like lists too!

Indexing a string is like creating a list containing each character in the string.

For example:

str = "Hello world!"
print(str[6])
#W

pace (" ") is also a symbol and has an index.
Trying to access a non-existing index will result in an error.



List Operations


The list of cool things we can do with lists just keeps growing!
Lists can also be added and multiplied in the same way as strings.

For example:

nums = [1, 2, 3]
print(nums + [4, 5, 6])    #[1, 2, 3, 4, 5, 6]
print(nums * 3)            #[1, 2, 3, 1, 2, 3, 1, 2, 3]

Lists and strings share a lot of similarities - 
you can basically think of strings as lists of characters that can't be changed.

List Operations
Figure out the output of this code:

x = [2, 4]
x += [6, 8]
print(x[2]//x[0])
#3

#########################################################################################


Problem
Strings as Lists


You need to take the first and last name of a person as input and output the initials
(first letters of the first and last name).

Sample Input
James
Smith

Sample Output
J.S.
In order to match the output, you need to place dots after each initial.


SOLUTION:

fname = input()
lname = input()
#your code goes here

print(fname[0]+"."+lname[0]+".")


#########################################################################################

List Operations


To check if an item is in a particular list, we can use the in operator.

It returns True if the item occurs one or more times in the list, and False if it doesn't. 
Like this:

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

#True
#True
#False

The in operator is also used to determine whether or not a string 
is a substring of another string.


List Operations
What's the result of this code?

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
  print(nums[3]) #7
else:
  print(nums[4])

List Operations


Similarly, to check if an item is not in a list, you can use the not operator in one of
the following ways:

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#True
#True
#False
#False

#########################################################################################

for Loop


There’s always more to say, but that was a pretty good intro to lists.
 Let’s move on and introduce a new loop.

The for loop is used to iterate over a given sequence, such as lists or strings.

The code below outputs each item in the list and adds an exclamation mark at the end:

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

hello!
world!
spam!
eggs!

In the code above, the word variable represents the corresponding item of the list 
in each iteration of the loop.

During the 1st iteration, word is equal to "hello", and during the 2nd iteration 
it's equal to "world", and so on.

for Loop
Fill in the blanks to create a valid for loop.
letters = ['a', 'b', 'c']

for l in letters:
  print(l)


for Loops

A for loop can be used to iterate over strings.

For example:

str = "testing for loops"
count = 0

for x in str:
  if(x == 't'):
    count += 1

print(count) #2

The code above defines a count variable, iterates over the string and 
calculates the count of 't' letters in it. During each iteration, the x
variable represents the current letter of the string.

The count variable is incremented each time the letter 't' is found, so,
at the end of the loop it represents the number of 't' letters in the string.

Similar to while loops, the break and continue statements can be used in for loops,
to stop the loop or jump to the next iteration.


for Loops
What's the output of this code?

list = [2, 3, 4, 5, 6, 7]

for x in list:
    if(x%2==1 and x>4):
        print(x)
        break
#5


###############################################################################

for vs while


So we’ve got the for and while loops, which can be used to execute a block
 of code multiple times. So which do we use and when?

*****Usually we’d use the for loop when the number of iterations is fixed.
 For example, iterating over a fixed list of items in a shopping list.

*****The while loop is useful in cases when the number of iterations isn’t known
 and depends on some calculations and conditions in the code block of the loop.
 For example, ending the loop when the user enters a specific input in a calculator program.

While both, for and while loops can be used to achieve the same results, however,
 the for loop has cleaner and shorter syntax, making it a better choice in most cases.


###############################################################################


Range


Python makes it super easy to create number sequences using the range() function.

By default, it starts from 0, increments by 1 and stops before the specified number.

The following code generates a list containing all of the integers, up to 10.


numbers = list(range(10))
print(numbers)
##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


In order to output the range as a list, we need to explicitly convert it to a list,
using the list() function.


###############################################################################

#youtube hour hate

print("Hours of video uploaded by hour in youtube",60*500,  
        "\n or:", (60*500)/24, "days" # 500 hour per minute
        "\n or:", round(((60*500)/24)/365), "years and",((60*500)/24)%365, "days")

Hours of video uploaded by hour in youtube 30000 
                                        or: 1250.0 days
                                        or: 3 years and 155.0 days

###############################################################################


Range


Right, time to take a deeper dive into ranges!

If range is called with one argument, it’ll produce an object with values from 0 
to that argument.

If it’s called with two arguments, it’ll produce values from the first to the second.

For example:

numbers = list(range(3, 8))
print(numbers)

#[3, 4, 5, 6, 7]


Remember, the second argument is not included in the range, so range(3, 8) won’t include the number 8.


print(range(20) == range(0, 20))
#True


Range


There’s also a third argument you can use with range(), and it’s really useful. It’s called Step 
and it determines the interval of the sequence produced. Take a look:


numbers = list(range(5, 20, 2))
print(numbers)
#[5, 7, 9, 11, 13, 15, 17, 19]


Want to go backward? No problem! We can also create a list of decreasing numbers, using a negative 
number as the third argument, for example list(range(20, 5, -2)).

numbers = list(range(5, 20, -2))
print(numbers)
#[] no print

What's the result of this code?

nums = list(range(3, 15, 3))
print(nums[2])
#9


for Loops


Let’s come back to the for loop for a moment, because it’s great friends with range.
It’s commonly used to repeat some code a certain number of times, which is done by combining for 
loops with range objects. Like this:

for i in range(5):
  print("hello!")

#hello!
#hello!
#hello!
#hello!
#hello!

Don’t worry about calling list on the range object when it is used in a for loop, because it
 isn't being indexed, so a list isn't needed.


###############################################################################

List Slices


Looking for a more advanced way to retrieve values from a list? Look no further 
than List slices!

The most basic list slicing involves indexing a list with two colon-separated integers.
This will return a new list containing all the values in the old list between the indices.

Example:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#[4, 9, 16, 25]
#[9, 16, 25, 36, 49]
#[0]

Just like the arguments to range, the first index provided in a slice is included in 
the result, but the second isn't.


List Slices

Save a little time, and keep your code as short and simple as possible by remembering this:
If the first number in a slice is omitted, it’s taken to be the start of the list.
If the second number is omitted, it’s taken to be the end.

Example:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

#[0, 1, 4, 9, 16, 25, 36]
#[49, 64, 81]

Slicing can also be done on tuples.



Fill in the blanks to take the first two elements of the list:
list = ["a", "b", "c", "d"]

a = list[0:2]
# a, b


List Slices


Just like with ranges, your list slices can include a third number,
representing the step, to include only alternate values in the slice. Like this:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])


Result:
>>>
[0, 4, 16, 36, 64]
[4, 25]
>>>

Just in case you need it, here’s another example: [2:8:3] will include elements 
starting from the 2nd index up to the 8th with a step of 3.


List Slices
What's the output of this code?

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

#[1, 25, 81]


List Slices


And yeah, you guessed it, Negative values can also be used in list slicing 
(as well as normal list indexing).

Which means that when negative values are used for the first and second 
values in a slice (or a normal index), 
*****they count from the end of the list. Like this:

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

Result:
>>>
[1, 4, 9, 16, 25, 36, 49, 64]
>>>

If a negative value is used for the step, the slice will be done backwards.
Using [::-1] as a slice is a common and idiomatic way to reverse a list.

What's the output of this code?

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])
#[49, 36]


###############################################################################


Problem
Sum of Consecutive Numbers


No one likes homework, but your math teacher has given you an assignment to find 
the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
You can iterate over a range and calculate the sum of all numbers in the range.
Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.


SOLUTION:

N = int(input())
#your code goes here

sum = 0

for i in range(N+1):
    sum += i

print(sum)

Sum of Consecutive Numbers
Run
ProblemResults
Test Case 1

Input
358
Your Output
64261
Expected Output
64261


###############################################################################


Functions


You made it all the way to module 6! Congrats!

Let’s start by talking about functions. You’ve already met and used plenty of
functions ( a group of related statements that performs a specific task) by now.

To jog your memory, here are some examples that you've already seen:
print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)

The words in front of the parentheses are function names, and the 
comma-separated values inside the parentheses are function arguments.

Functions help break our program into smaller, modular chunks. As our
program gets bigger and more complex, functions help to make it more organized and manageable.

List Functions


Python has a bunch of useful built-in functions. Like len!

len lets you get the number of items in a list. Like this:

nums = [1, 3, 5, 2, 4]
print(len(nums)
#5

You can also use len on strings to return their length (character count).

Unlike indexing items, len does not start with 0. The list above contains 
5 items, meaning len will return 5.



Useful Functions


Time for the lightning round! Let’s do a quick rundown of the functions supported by lists.
Note, that the function is called using the list name, followed by a dot.

nums = [1, 2, 3]
nums.append(4)
print(nums)
#[1, 2, 3, 4]

insert() - inserts a new item at any position in the list:

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words) 
#['Python', 'is', 'fun']




index() - finds the first occurrence of a list item and returns its index.

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q')) 
#2
#0
#1


***max(list): Returns the maximum value.
***min(list): Returns the minimum value.
***list.count(item): Returns a count of how many times an item occurs in a list.
***list.remove(item): Removes an item from a list.
***list.reverse(): Reverses items in a list.

For example, you can count how many 42s are there in the list using:
items.count(42) where items is the name of our list.

###############################################################################


String Formatting


Strings have a format() function, which enables values to be embedded in it,
 using placeholders.

Example:
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)

#Numbers: 4 5 6


Each argument of the format function is placed in the string at the corresponding position,
 which is determined using the curly braces { }.


String Formatting
What's the result of this code?

print("{0}{1}{0}".format("abra", "cad"))
#abracadabra


You can also name the placeholders, instead of the index numbers.
Example:
a = "{x}, {y}".format(x=5, y=12)
print(a)
#5, 12


What's the result of this code?

str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)
#7, 9, 5


String Functions


Another lightning round! Here are some of the other useful string functions:

***join - joins a list of strings with another string as a separator.

***replace - replaces one substring in a string with another.

***startswith and endswith - determine if there is a substring at the start and end of a string, respectively.

***lower and upper – changes the case of a string

***split -the opposite of join, turns a string with a certain separator into a list.

Here they are in action:


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


###############################################################################

Functions


But what if those pre-defined functions just don’t cut it? You need more flexibility
to create the program you’re working on. Well, you can create your own functions by
using the def statement.

Here’s an example of a function named my_func. It takes no arguments, and prints "spam"
three times. It’s defined, and then called. The statements in the function are executed
only when the function is called.

def my_func():
   print("spam")
   print("spam")
   print("spam")

my_func()

#spam
#spam
#spam


The code block within every function starts with a colon (:) and is indented.

So once you’ve defined a function, you can call them multiple times in your code.
Like this:

def hello():
   print("Hello world!")
 
hello()
hello()
hello()

###############################################################################


Arguments

Functions can take arguments, which can be used to generate the function output.
For example:

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

#spam!
#eggs!
#python!

As you can see from the example, the argument is defined inside the parentheses and is named word.


Arguments


Even better, you can define functions with more than one argument; separate them with commas. Like this:

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

#13
#13

Returning from Functions


Certain functions, such as int or str, return a value instead of outputting it.

The returned value can be used later in the code, for example, by getting assigned to a variable.

To do this for your defined functions, you can use the return statement. Like this:
For example:


def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))   #7
z = max(8, 5)
print(z)           #8

The return statement cannot be used outside of a function definition.


Returning from Functions


Once you return a value from a function, it immediately stops being executed.

Any code placed after the return statement won’t be executed.
For example:

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))
#9



Comments


We’re so close to the finish line! Well done for making it this far!

Comments are annotations to code used to make it easier to understand.
 They don't affect how code is run.

In Python, a comment is created by inserting an

*** octothorpe
 (otherwise known as a number sign or hash symbol: #). 

All text after it on that line is ignored.
For example:

x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment
print 1

Unlike programming languages such as C, Python doesn’t have 
general-purpose multiline comments.



Docstrings


Ok let’s wrap up module 6 with docstrings.

Docstrings (documentation strings) are similar to comments, 
in that they’re designed to explain code. But! they’re more 
specific and have a different syntax.

They’re created by putting a multiline string containing an explanation 
of the function below the function's first line. Like this:

def shout(word):
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + "!")

shout("spam")
#spam!

Unlike conventional comments, docstrings are retained throughout the 
runtime of the program. This allows the programmer to inspect these comments at run time.


###############################################################################

Problem
Search Engine


You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

Sample Input
"This is awesome"
"awesome"

Sample Output
Word found
Define the search() function, so that the given code works as expected.

SOLUTION:


import re

def search(t,w):
    pattern = r""+w+""
    if re.search(pattern,t):
        return "Word found" 
    else:
        return "Word not found"

text = str(input())
word = str(input())

print(search(text, word))