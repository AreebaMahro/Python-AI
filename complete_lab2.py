# ========================if, if-else, else-if statements=================

print("\n-----> if, if-else, else-if statements:")
x = 10
if x>10:
    print("X is greater than 10.")
elif x<10:
    print("X is less than 10.")
else:
    print("X is equal to  10.")

# ===============================while loop==========================

print("\n-----> While Loop:")
print("Even values from 10 to 20:\n")
while x<=20:
    if x%2==0:
        print(x)
    x=x+1
else:            # else of while loop
    print("While loop of even values ends.")
#-------------------------------------------------------
print("Sum of values b/w 0 t0 100:\n")
x=0
sum=0
while x<=100:
    sum=sum+x
    x=x+1
else:           
    print("Sum is:",sum)
    print("While loop of Sum values ends.")
# -----------------------------------------------------
print("Star Half Triangle by while loop:\n")
x=1
while x<=5:
    y=1
    while y<=x:
        print("*" , end =' ')
        y=y+1
    print()
    x=x+1
else:            
    print("While loop of Star Half Triangle ends.")
#----------------------------------------------------------
print("Another Star Half Triangle by another method:")
x=1
while x<=5:
    print("*" * x )
    x=x+1
else:            
    print("While loop of Star Half Triangle ends.")
#----------------------------------------------------------------

# ======================================for loop=================================

#---------------------------using iterative variable-------------------
print("\n-----> List Iteration:")
l = ["Areeba", "Nadia", "Aqsa"]
for x in l:
    print(x)

print("\n-----> Tuple Iteration:")
t = ("Areeba", "Nadia", "Aqsa")
for x in t:
    print(x)

print("\n-----> String Iteration:")
s = "Areeba Mahro"
for x in s:
    print(x)
#-------------------------------------examples-------------------------------------
print("Star Half Triangle by for loop:\n")
for x in range(1,6):   # last value is not included in range
    for y in range(1,x+1):
        print("*", end=' ')
    print()

#-------------------------------------------------------------
print("Sum of values b/w 0 t0 100 using for loop:\n")
sum=0
for x in range(1,101):
    sum+=x 
else:           
    print("Sum is:",sum)

#--------------------------------using index-----------------------------
print("\n-----> List Iteration:")
l = list(("Areeba", "Nadia", "Aqsa"))   # list is made using list constructor function
for index in range(len(l)):
    print(l[index])

print("\n-----> Tuple Iteration:")
t = ("Areeba", "Nadia", "Aqsa")
for index in range(len(t)):
    print(t[index])

print("\n-----> String Iteration:")
s = "Areeba Mahro"
for index in range(len(s)):
    print(s[index])

# ===============================loop control statements=========================

for i in range(1,6):
    if i==3:
        i=i+1
        continue   # continue ststement transfers the control to loop
    print(i)
    i=i+1
else:
    print("3 is skipped using continue statement.")

#------------------------------------------------------------------
for i in range(1,6):
    if i==4:
        break   # break ststement transfers the control out of the loop
    print(i)
    i=i+1
else:
    print("loop is terminated at 3 using break statement.") # this will not be printed due to brak statement
print("loop is terminated at 3 using break statement.")

#=============================Functions=======================================

def my_first_fun():       # definition of a function
    print("\nAreeba Mahro!")
my_first_fun()            # calling a function

#-------------------------------------------------------------------------
# function with parameter
def my_first_fun(s):      
    print("\nMy name is " + s + ".")
my_first_fun('Areeba Mahro') 

# function with default parameter
def my_first_fun(s = 'Mahro'):      
    print("\nMy name is " + s + ".")
my_first_fun()
my_first_fun('Areeba')

# function with list as a parameter
def my_first_fun(l):      
    print("\n",l)
food=['fruits', 'vegitables', 'chicken']
my_first_fun(food)

#-----------------------------------------------------------------------

# function with returning value
def my_first_fun(x,y):      
    sum=x+y
    return sum
total = my_first_fun(10,20)
print("\n Sum is:",total)

#-----------------------------------------------------------------------

# function with arbitrary arguments
def my_first_fun(x,y,*arguments):      
    print(x,",",y,",",arguments)
my_first_fun(10,20,30,40,50,60)

# function with arbitrary key arguments
def my_first_fun(x,y,**key_arguments):      
    print(x,",",y,",",key_arguments)
    print(key_arguments['name'])
my_first_fun(x=10,y=20,c=30,d=40,name='Areeba Mahro')

# function with key arguments
def my_function(child3, child2, child1): 
    print("The youngest child is " + child3) 
my_function(child1 = "Silah", child2 = "Areeba", child3 = "Mehar")

# =============================Classes===================================

class student:
    name = "Areeba Mahro"
    father = "Anser Farooq"
    rollno = "BCS21011"
    cgpa = 3.55
    def __init__(self,namee,fatherr,rollnoo,cgpaa):
        self.name = namee
        self.father = fatherr
        self.rollno = rollnoo
        self.cgpa = cgpaa
    def show(self):
        print(f" Name is {self.name}. \n Father name is {self.father}. \n Roll no. is {self.rollno}. \n CGPA is {self.cgpa}. \n")
p1 = student("Silah","Nagra","BSE21022",3.99)
p1.show()

         


