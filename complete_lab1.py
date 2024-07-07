# Programming In Python...... (single line comment)
print("\n------------------------------------FIRST PROGRAM------------------------------------\n")
print("HELLO WORLD!!! -_-")

# input / output
print("\n------------------------------------INPUT/OUTPUT-------------------------------------\n")

# input
print("-----> Input:")
a = input("Enter value:")
print("Value is:",a," Data type of this value is: ",type(a))
print("# By default data type of input value is string. To get other types of data function like int(), float() is used.")
a = int(input("Enter value:"))
print("Value is:",a,". Data type of this value is: ",type(a))

# output
print("\n-----> Output:")
print("\n-----> Output At Same Line with Default Separater i.e space:")
print("Hello1","Hello2","Hello3")
print("\n-----> Output At Same Line with Separater =' *** ':")
print("Hello1","Hello2","Hello3",sep=' *** ')
print("\n-----> Output with Default End i.e New Line:")
print("Hello1")
print("Hello2")
print("\n-----> Output with End =' *** ':")
print("Hello1",end=' *** ')
print("Hello2")
print("\n-----> Formating the Output using 'f' :")
name = 'Areeba Mahro'
place = 'Gujranwala'
age = 22
print(f"My name is {name} and I live in {place} and my age is {age}.")
"""
Programming
In 
Python.. 
(multiple line comment)
"""
# or
'''
Programming
In 
Python.. 
(multiple line comment)
'''

# indendation is important in python as it indicates the block of body
print("\n------------------------------------INDENTATION-------------------------------------\n")
if True:
 print("This ststement has single space indentation")
if True:
    print("This ststement has single tab indentation")
if True:
     print("This ststement has single space + single tab indentation")
     

# assigning different values to differet variables at the same line
print("\n--------------INITIALIZATION OF MULTIPLE VARIABLES IN A SINGLE LINE-------------\n")
x,y,z = 10,20,30
print(x,y,z)

# function to find the data type of a variable
print("\n-----------------------FUNCTION TO FIND DATA TYPES-----------------------\n")
x = 11
y = 11.000
e = 2.12e-10 ; E = 5E220  # exponential value
z = "BCS21011" 
c = 1+2j ; C = 1+2J  # complex type values uses j/J instead of i(iota)
b = True ; B = False # blean type values
print(type(x))
print(type(y))
print(type(e))
print(type(E))
print(type(z))
print(type(c))
print(type(C))
print(type(b))
print(type(B))


# functions for casting i.e data type changing
print("\n--------------------FUNCION FOR CASTING-----------------------\n")
x = 11
y = 11.000
z = "BCS21011"
print(float(x))
print(str(x))
print(int(y))
print(str(y))
print(bool(x))
print(bool(''))
print("Any value convered into bool type show 'True' except of '0/None/empty string' as these values show 'False'")
print("String and Boolen data type can not be convered into othr types")
'''
print(int(z)) string cannot be changed into  int or float
'''
# to delete a variable using del button
print("\n-----------------------DELETING VARIABLE------------------------\n")
a = 33
print("A=",a)
del a
print("'A' has been deleted successfully! using 'del' command")

# writting two or more statements at the same line using semicolon
print("\n-------------TWO OR MORE STSTEMENTS AT THE SAME LINE USING SEMICOLON---------------\n")
print(x) ; print(y) ; print(z)

# special characters in the strings i.e \n , \t , \\ , \' , \" i.e Newline ,Horizontal Tab ,Backslash ,Single Quote ,Double Quote respectively
print("\n------------------SPECIAL CHARCTERS(ESCAPE SEQUENCES)----------------------\n")
print("Mahro is shifted to new line \n Mahro")
print("Mahro is shifted to single tab space \t Mahro")
print("The respective symbol is blackslash: \\ ")
print("These are \' single quotes \'")
print("These are \" double quotes \"")

# string indices and accessing string elements *** Indices start with 0 from left side and -1 when starting from right side. 
print("\n-----------------------------STRINGS-------------------------------------\n")
z = "BCS21011" # one method to declare string value
u = 'BCS21012' # another method to declare string value
s = "BCS'21013" ; S = 'BCS"21014' # can use one type of quote within another type
# Wrong string declarations are: s = "BCS21011' / s = 'BCS21011" / s = "BCS"21011" / s = 'BCS'21011'
print("Single line strings:\n",z,"   ",u,"   ",s,"   ",S)
# Muliple line string syntaxusing triple single or double quotes
Para = """wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg """
print("Multiple line string:\n",Para)
# string indices
print("\n-----> String Indices:")
G = "Areeba Mahro "
print("String = Areeba Mahro")
print("Printing Areeba index wise")
print(G[0])
print(G[1])
print(G[2])
print(G[3])
print(G[4])
print(G[5])
print("Printing Mahro Reversely index wise")
print(G[-2]) ; print(G[-3]) ; print(G[-4]) ; print(G[-5]) ; print(G[-6])

# string slicing means to cut a part of the string by giving string_name(starting_index:ending_index) where ending_index is not included
print("\n-----> String Slice:")
print("String before slice is:",G)
print("String after slice is: ",G[7:12])

# string concatination
s1 = "Areeba"
s2 = "Mahro"
s3 = s1 + " " + s2
print("\n-----> String Concatination:")
print("\n--> String before  Concatination is:")
print("String 01: ","My name is ",s3)
print("String 02: "," and I live in Pakistan")
print("\n--> String after Concatination using '+' is: ")
print("My name is " + s3 + " and I live in Pakistan")

# Printing a string 'n' times
print("\n-----> Printing a string 'n' times:")
print("String = " + G)
x = int(input("Enter how many times do u want to print the above string: "))
print(" Output:   ",G * x)

# string format using format() function
print("\n-----> String Format:")
s = "My name is {} and I live in {} and my age is {}." # one method
print(s.format(name,place,age))
S = "My name is {1} and I live in {2} and my age is {0}." # another method using indices which represent the same indices inside format() function like format(0,1,2,.....)
print(S.format(name,place,age))

# string lenght i.e number of characters in a string using len() function
print("\n-----> String Length:")
print("String = " + G)
print("Length of the String '" + G + "' is: ",len(G))

# string 'in' and 'not in' functions to find whether the value is in the string or not
print("\n-----> String 'in' and 'not in' functions to find whether the value is in the string or not:")
print("String = " + G)
# String 'in' function
print("\n-----> String 'in' function")
print("Is 'Mahro' in the String:",end=' ')
print("Mahro" in G)
print("Is 'Orham' in the String:",end=' ')
print("Orham" in G)
# String 'not in' function
print("\n-----> String 'not in' function")
print("Is 'Mahro' not in the String:",end=' ')
print("Mahro" not in G)
print("Is 'Orham' not in the String:",end=' ')
print("Orham" not in G)

# Converting the string into UPPER or lower case using 'upper()' and 'lower()' functions
print("\n-----> Converting the string into UPPER or lower case:")
print("String = " + G)
# upper case
print("-----> Into UPPER case")
print(G.upper())
# lower case
print("-----> Into lower case")
print(G.lower())
# lists
print("\n-------------------------------LISTS-------------------------------------\n")
list_1 = [1,2,3,4,5]
print("List's Integer Values are:",list_1)
list_2 = [11.1,22.1,33.1,44.1,55.1]
print("List's Float Values are:",list_2)
list_3 = ['Red','Green','Yellow','Blue','Black']
print("List's String Values are:",list_3)
list_4 = [1,'Red',22.1,'Purple',33]
print("List's Mixed Data Type Values are:",list_4)
list_5 = []
print("An Empty List:",list_5)

# list indices
print("\n-----> List Indices:")
list_4 = [1,'Red',22.1,'Purple',33]
print("List's Values are:",list_4)
print("Value at 4 index of list is: ",list_4[3])

# list slice
print("\n-----> List Slice:")
list_4 = [1,'Red',22.1,'Purple',33]
print("List before slice is:",list_4)
print("List after slice is: ",list_4[2:4])

# arithmethic operatore
print("\n-------------------------ARITHMETHIC OPERATORS---------------------------/n")
x = 100
y = 30
sum = x+y 
minus = x-y
product = x*y 
divided = x/y 
modulus = x%y
exponential = x**y 
integer_only = x//y 
print("Let X = ", x," and Y = ", y)
print("---> Then, Arithmethic Operators (+,-,*,/,%,**,//) are: where '**' gives 'Exponential value' , '//' gives 'Only fractional value without fraction part'\n")
print("X+Y=",sum," , X-Y=",minus," , X*Y=",product," , X/Y=",divided," , X%Y=",modulus," , X**Y=",exponential," , X//Y=",integer_only)

# conditional statements
print("\n-------------------------COMPARISON OPERATOR---------------------------/n")
print("Let X = ", x," and Y = ", y)
print("--->Then Comparison Operators (==,!=,>,>=,<,<=) are:\n")
print("X==Y:",x==y," , X!=Y:",x!=y," , X>Y:",x>y," , X>=Y:",x>=y," , X<Y:",x<y," , X<=Y:",x<=y)

# logical operators
print("\n-------------------------LOGICAL OPERATOR---------------------------/n")
z=60
print("Let X = ", x," and Y = ", y, " and Z = ", z)
print("--->Then Logical Operators (and,or,not) are:\n")
print("and OPERATOR: x<y and y<z: " , x<y and y<z)
print("or OPERATOR: x<y or y<z: " , x<y or y<z)
print("not OPERATOR: not(x<y and y<z): " , not(x<y and y<z))

# identity operators tells whether two variables point to same memory location or not
print("\n-------------------------IDENTITY OPERATOR---------------------------/n")
print("Let X = ", x," and Y = ", y)
print("--->Then Identity Operators (is,is not) are:\n")
print("is OPERATOR: x is y: " , x is y)
print("is not OPERATOR: x is not y: " , x is not y)

# membership operators 'in' and 'not in' to find that given data is  a specific part of string/list etc or not
print("\n-------------------------MEMBERSHIP OPERATOR---------------------------/n")
x = "University of the Punjab Gujranwala"
print("Let a string X = ", x)
print("--->Then Membership Operators (in,not in) are:\n")
print("in OPERATOR: Is 'Punjab' in X: " , "Punjab" in x)
print("not in OPERATOR: Is 'Punjab' not in X: " ,"Punjab" not in x )