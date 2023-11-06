##### Weekly Assignment of Ai with Python - Module 1. 04-11-2023
Last date of submission: 06-11-2023
______________________________________________________________________________

##### 1. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list  with those numbers



# ask user to enter comma seperated numbers

usernumbers = input("Enter numbers seperated by a comma: ")

print("user entered list:", usernumbers)
print(type(usernumbers))

#generate a list with above numbers
numlist = usernumbers.split(',')
print("List:", numlist)
print(type(numlist))
print(numlist[0])


##### 2. Write a Python program to accept a filename from the user and print the extension of that

filename = input("Enter a filename: ")

filetype = filename.split('.')

print(filetype)
print("Entered file name has the extension:", filetype[1])

##### 3. Write a Python program to display the first and last colors from the following list color_list = ["yellow","Green","grey" ,"orange"]



# code
color_list = ["yellow","Green","grey" ,"orange"]
print("First colour in the list is",color_list[0])

print("The last colour in the list is",color_list[-1])

##### 4. Write a program that checks if a given string is a palindrome.

# Explain
# 1. take a string
# 2. check if the string an its reverse are equal

# Code

txt = input("Enter a string: ")
revtxt = txt[::-1]

print(txt)
print(revtxt)

if txt == revtxt:
    print(txt, "ia a palindrome")

else :
    print(txt, "is not a palindrome")


##### 5. Return the count of sub-string “Shubhangi” appears in the given string - "Shubhangi is good developer. Shubhangi is a Data Scientist"

# Code

teststring = "Shubhangi is good developer. Shubhangi is a Data Scientist"

c = teststring.count('Shubhangi')

print("Number of times substring 'Shubhangi' appears in main string is:", c)

##### 6. Write a function to calculate area and perimeter of a rectangle.

# Take the length and breadth of the rectangle in cm

length = float(input("Enter the length of the Rectangle in cm:"))
breadth = float(input("Enter the breadth of the Rectangle in cm:"))

#calculate Area
area = (length*breadth)
print("Area of a rectangle with length",length,"cm and breadth",breadth,"cm is", area,"square cm.")

#calculate perimeter
perimeter = (length+breadth)*2
print("Perimeter of a rectangle with length",length,"cm and breadth",breadth,"cm is", perimeter,"cm.")

##### 7. Write a function to tell user if he/she is able to vote or not.

# Ask for user yob; find current age
# if age <18 not elligible to vote

yob = input("Enter your Year of Birth:")

currentage = 2023 - int(yob)

print("Your birth year is", yob, "and your current age is",currentage)

if currentage < 18:
    
    print ("Sorry, you are less than 18 years and not elligible to vote.")
    
else :
    print ("Congrats, you are more than 18 years and elligible to vote.")

## Alternate way : by getting the year from the system date

from datetime import date
today1 = date.today()

yob1 = input("Enter your Year of Birth:")

currentage1 = today1.year - int(yob1)

print("Your birth year is", yob1, "and your current age is",currentage1)

if currentage1 < 18:
    
    print ("Sorry, you are less than 18 years and not elligible to vote.")
    
else :
    print ("Congrats, you are more than 18 years and elligible to vote.")

##### 8. Write a program to check if each word in a string begins with a capital letter?

# code

ipstring = input("Enter a sentence or two where each word begins with a capita letter:")

if ipstring.istitle():
    print("The input string has all the words beginning with capital letter.")
else:
    print("The input string does not have all the words beginning with capital letter.")


##### 9. Write a program to Check if a string contains a specific substring.

# code

#readystring = "Write a program to Check if a string contains a specific substring."
#"program to Check" in readystring

fullstring = input("Enter a sentence or two:")

substring = input("Enter the string to be checked:")

if (substring in fullstring):
    print("Substring part of main string")
    
else:
    print ("Substring not a part of main string")

##### 10. Capitalize the first character of a string

# code

capstring = input("Enter a string:")
f = capstring[0]
print(f)
c = f.upper()
print(c)
newstring = c + capstring [1:] 

print(newstring)

##### 11. Reverse the string “hello world”

# code
hw = "hello world"

revhw = hw[::-1]

print(revhw)

##### 12. Write a program to display the last digit of a number. (hint : any number % 10 will return the last digit)

# code

num = input("Enter a number:")

lastdig = num[-1]

print(lastdig)

##### 13. Write a program to check whether an years is leap year or not.

# code

year = int(input("Enter a Year:"))

if (year % 400 ==0) and (year % 100 == 0):
    print(year,"is a leap year.")
    
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"is a leap year.")
    
else:
    print(year,"is not a leap year.")



##### 14. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

# code

weekdays = {1:"Sunday",
            2: "Monday",
            3: "Tuesday",
            4: "Wednesday",
            5: "Thursday",
            6: "Friday",
            7: "Saturday"
           }

wkday = int(input("Enter a number between 1 to 7 to indicate the day of the week:"))

print ("Today is ", weekdays[wkday])

##### 15. Write a program to check whether a number (accepted from user) is positive or negative.

# code

testnum = input("Enter a number:")

if float(testnum) < 0 :
    print(testnum, ":Its a Negative number")
else:
    print(testnum, ":Its a positive number")

##### 16. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

# code
divnum = int(input("Enter a whole number:"))

if (divnum % 2 == 0) and (divnum % 3 == 0):
    print (divnum," is divisible by both 2 and 3.")
else:
    print (divnum," is not divisible by both 2 and 3.")

# List
Basic List Operations:

Create an empty list.
Add an element to the end of the list.
Insert an element at a specific position in the list.
Remove an element from the list.
Check if an element is present in the list.
List Slicing and Indexing:

Print the first element of the list.
Print the last element of the list.
Print elements from index 2 to 5 (exclusive) using slicing.
Print every alternate element of the list.
List Functions:

Find the length of the list.
Sort the list in ascending order.
Reverse the list.
Remove the last element from the list.
Clear all elements from the list.
List Comprehension:

Create a new list containing squares of elements from the original list.
Create a new list containing only even numbers from the original list.
Nested Lists:

Create a nested list containing two lists: [1, 2, 3] and ['a', 'b', 'c'].
Access the second element of the first list inside the nested list.
Modify the third element of the second list inside the nested list.
List Methods:

Use the append() method to add an element to the end of the list.
Use the count() method to count the number of occurrences of a specific element.
Use the index() method to find the index of a specific element.
Use the remove() method to remove the first occurrence of a specific element.
Use the extend() method to add elements from another list to the current list.

##### 17. Write a program that takes a list of numbers as input and calculates their sum.


# code
list = [10,2,3,34,45]
n = len(list)
print(n)
sum = 0

for n in range (0,(n)):
    sum = sum + list[n]
    
    
print("Sum of all the numbers is:", sum)
    
    

##### 18. List Modification Initialize a list with elements [2, 4, 6, 8, 10]Append the number 12 to the end of the list. Remove the element 6 from the list. Print the modified list.

# code
initlist = [2, 4, 6, 8, 10]

initlist.append(12)
print(initlist)

initlist.pop(2)
print(initlist)

##### 19. List Operations Initialize two lists: [1, 2, 3] and [4, 5, 6]. Concatenate these lists without using the + operator. Print the concatenated list.

# code
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)
#list2.extend(list1) 
print(list1)

### Tuple 
Python tuples are a type of data structure that is very similar to lists. The main difference between the two is that tuples are immutable, meaning they cannot be changed once they are created. This makes them ideal for storing data that should not be modified, such as database records.

https://pynative.com/wp-content/uploads/2021/02/python-tuple.jpg

##### 20. Create and explain the working of tuple.

#code


##### 21. Initialize and Access Tuple Elements

Initialize a tuple with elements (3, 6, 9, 12, 15).
Print the second element of the tuple.
Attempt to change the value of the second element (this will show that tuples are immutable).

#code
tup21 = (3, 6, 9, 12, 15)

print(tup21[1])
print(type(tup21))

tup21[1] = 101


22. Initialize a tuple with elements (7, 2, 9, 5, 1).
Find the length of the tuple.
Find the index of the element 9.
Count the number of occurrences of 2 in the tuple.

mytup = (7,2,9,5,1)
print(type(mytup))

#print(len(mytup))

print(mytup.index(9))

print("number of occurences of digit 2:", mytup.count(2))

23. Set Initialization and Operations

Initialize two sets: {1, 2, 3, 4, 5} and {3, 4, 5, 6, 7}.
Find the union of the two sets.
Find the intersection of the two sets.
Find the difference between the first set and the second set.

#code
set1 = {1, 2, 3, 4, 5} 
set2 = {3, 4, 5, 6, 7}

#union
print(set1.union(set2))
print(set2.union(set1))

#intersection
print("Intersection of set1 and set2:", set1.intersection(set2))
print("Intersection of set2 and set1:", set2.intersection(set1))

#difference
print("Difference of set2 from set1:", set2.difference(set1))
print("Difference of set1 from set2:", set1.difference(set2))

24. Create a list with duplicate elements [1, 2, 2, 3, 4, 4, 5, 5].
Convert the list into a set to remove duplicates.
Print the resulting set.

#code
dupset = {1, 2, 2, 3, 4, 4, 5, 5}

#While printing and finding length removes the duplicates
#print("length:", len(dupset))
print("Set:", dupset)

set2 = dupset
print(set2)


# Sets
The Python sets are highly useful to efficiently remove duplicate values from a collection like a list and to perform common math operations like unions and intersections. Some of the challenges people often encounter are when to use the various data types.

25. Initialize two sets: {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}.
Check if the first set is a subset of the second set.
Check if the sets have any common elements.

#code
s1 = {1, 2, 3, 4, 5} 
s2 = {4, 5, 6, 7, 8}

#is s1 a subset of s2?
if (s1.issubset(s2)):
    print("s1 is subset of s2")    
else:
    print("s1 is not a subset of s2")

#check for common elements
print("Common elements between s1 and s2 are:", s1.intersection(s2))

26. Create a list with elements [10, 20, 30, 40, 50].
Convert the list into a tuple.
Print the tuple.

#code
testlist =  [10, 20, 30, 40, 50]
print(type(testlist))
print("List:", testlist)

#convert list to tuple
testtup = ()

testtup = tuple(testlist)
print(type(testtup))
print("Tuple:", testtup)

# Dictionary 
Python dictionaries allow us to associate a value to a unique key, and then to quickly access this value. It's a good idea to use them whenever we want to find (lookup for) a certain Python object. We can also use lists for this scope, but they are much slower than dictionaries.


https://pynative.com/wp-content/uploads/2021/02/dictionaries-in-python.jpg

##### 27. Create an empty dictionary.
Add the key-value pairs: 'apple': 3, 'banana': 5, 'cherry': 2.
Modify the value of 'banana' to 8.
Remove the key 'cherry' from the dictionary.

#code
testdict = dict()

# add key -value pairs
testdict = {'apple': 3, 'banana': 5, 'cherry': 2}
print(testdict)

#modify banana to 8
testdict['banana'] = 8
print(testdict)

# remove the key cherry
testdict.pop('cherry')
print(testdict)


##### 28. Create a dictionary representing the number of fruits: {'apple': 3, 'banana': 8, 'orange': 6}.
Check if 'orange' is a key in the dictionary.
Print all keys and values in separate lines.

#code
fruitdict = {}
# create the number of fruits
fruitdict['apple'] = 3
fruitdict['banana'] = 8
fruitdict['orange'] = 6
print(fruitdict)

#check if orange is a key
if 'orange' in fruitdict.keys():
    print ("Orange is a key")

#print all keys and values
print("The keys:", fruitdict.keys())
print("The values:", fruitdict.values())

##### 29. Create a dictionary where the keys are names of countries and the values are dictionaries containing information about the capital city and population.
Add at least three countries to the main dictionary.
Print the details (capital and population) of a specific country.

#code
countrydict = {}

#Add details of 3 countries
countrydict ['India'] = ['New Delhi', 140]
countrydict ['Japan'] = ['Tokyo', 12.3]
countrydict ['France'] = ['Paris', 6.5]
print(countrydict)

#print the details

print("The national capital of India is", countrydict['India'][0], "and its poulation is", countrydict['India'][1], "crores.")
print("The national capital of Japan is", countrydict['Japan'][0], "and its poulation is", countrydict['Japan'][1], "crores.")
print("The national capital of France is", countrydict['France'][0], "and its poulation is", countrydict['France'][1], "crores.")


##### 30. Create a dictionary where keys are items (strings) and values are prices (floats).
Ask the user to enter items and quantities they want to purchase.
Calculate the total cost of items in the shopping cart.

# code

#define the items
shoppinglist = { "buckets" : 50,
                 "soaps" : 15,
                 "spoons" : 12,
                 "toys" : 22,
                 "magazine" : 5
                }

# get the list of items from user
b = int(input("How many buckets do you want? "))
s = int(input("How many soaps do you want? "))
sp = int(input("How many spoons do you want? "))
t = int(input("How many toys do you want? "))
m = int(input("How many magazines do you want? "))

#calculate cost of the shopping cart
cart = (b*shoppinglist["buckets"]) + (s*shoppinglist["soaps"]) + (sp*shoppinglist["spoons"]) + (t*shoppinglist["toys"]) + (m*shoppinglist["magazine"])

print("The total cart amount payable is:", cart)


