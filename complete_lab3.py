# =======================================program 1====================================

print("_________________Numbers divisible by 7 and multiple of 5 b/w 1500 1nd 2700__________________")
for x in range(1500,2700):
    if x % 7 == 0:
        if x % 5 == 0:
            print(x)

# =======================================program 2====================================

print("\n________________________________Temperature converter________________________________")
def temp_converter():
    print("1.  From Celcius to Fehrenheit")
    print("2.  From Fehrenheit to Celcius")
    choice = int(input("Enter your choice:"))
    if choice==1 or choice==2:
        if choice==1:
            temp = float(input("Enter temperature:"))
            f_temp = (temp*9)/5 +32
            print("Temperature in fehrenheit is: ",f_temp)
        elif choice==2:
            temp = float(input("Enter temperature:"))
            c_temp =  (temp-32)*5/9
            print("Temperature in celcius is: ",c_temp)
    else:
        print("You entered invalid choice. Try Again!")
        temp_converter()
temp_converter()

# =======================================program 3====================================

print("\n_________________________________Guess the Number__________________________")
import random
number = random.randint(1,10)
guess = int(input("Guess a Number b/w 1 & 10: "))
while guess!=number:
    print("Your guess is wrong. Try Again!")
    guess = int(input("Guess a Number b/w 1 & 10: "))
else:
    print("Your guess was right. The number is ",number,".")

# =======================================program 4====================================

print("\n________________________Pattern_______________________________")
for x in range(1,6):   
    for y in range(1,x+1):
        print("*", end=' ')
    print()
for x in range(4,0,-1):   
    for y in range(1,x+1):
        print("*", end=' ')
    print()

# =======================================program 5====================================

print("\n________________________Reversing a Word_______________________________")
word = input("Enter a Word:")
rev_word = ""
for letter in word:
    rev_word = letter + rev_word
print(rev_word)

# =======================================program 6====================================

print("\n________________________Number of Even & Odd_______________________________")
print("Series of Number: (1,2,3,4,5,6,7,8,9)")
even = 0 ; odd = 0
for x in range(1,10):
    if x % 2 == 0:
        even= even +1
    else:
        odd= odd +1
print("Number of Even Numbers: ",even)
print("Number of Odd Numbers: ",odd)
    
# =======================================program 7====================================

print("\n________________________List Items & their Types_______________________________")
print("Data_list is a given list in which :")
data_list = [1452,11.23,1+2j,True,'w3resourse',(0,-1),[5,12],{"class":'V',"section":'A'}]
for x in data_list:
    print(x," is an item and its type is ",type(x))

# =======================================program 8====================================

print("\n________________________Expel 3 & 6 using 'continue' ststement_______________________________")
print("Numbers from 0 to 6 except 3 and 6 are:")
for x in range(0,7):
    if x % 3 == 0:
        continue
    print(x)

# =======================================program 9====================================

print("\n________________________Fibonacci Series_______________________________")
print(" Fibonacci Series b/w 0 to 50 is:")
x=0;y=1
z=x+y
print(x,end=',');print(y,end=',');print(z,end=',')
f=0
while f<51:
    f=y+z
    y=z
    z=f
    print(f,end=',')
    x=x+1

# =======================================program 10====================================

print("\n________________________Fizz & Buzz_______________________________")
print("Numbers b/w 1 to 50 with multiple of 3 and 5 are:")
for x in range(1,51):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)

# =======================================program 11====================================

print("\n________________________Two Dimentional Array_______________________________")
print("Two dimentional array is:")
row = int(input("Enter no. of rows:"))
col = int(input("Enter no. of columns:"))
i=0
while i<row:
    j = 0
    while j<col:
        print(i*j,end=',')
        j=j+1
    print()
    i=i+1

# =======================================program 12====================================

print("\n________________________Binary Numbers / by 5_______________________________")
text = input("Enter 4 digit binary numbers separated by comma:")
number = text.split(',')
divisible_list = []
for x in number:
    n=int(x,base=2)
    if int(n%5)==0:
        divisible_list.append(x)
print(','.join(divisible_list))

# =======================================program 13====================================

print("\n________________________Numbers & Letters in String_______________________________")
text = input("Enter a string:")
num=0;lett=0
for x in text:
    if x.isdigit():
        num=num+1
    elif x.isalpha():
        lett=lett+1
print("Number of Letters: ",lett," and Number of Digits: ",num)

# =======================================program 14====================================

print("\n________________________Validity of Password_______________________________")
valid=False
while valid!=True:
    password = input("Enter Password:")
    if len(password)<6:
        print("Password must conatin at-least 6 characters.")
    elif len(password)>16:
        print("Password must conatin less than 16 characters.")
    elif not any(char.isdigit() for char in password):
        print("There must be at-least one digit in the password.")
    elif not any(char.islower() for char in password):
        print("There must be at-least one lower-case letter in the password.")
    elif not any(char.isupper() for char in password):
        print("There must be at-least one upper-case letter in the password.")
    elif not any(char='@' for char in password):
        print("There must be at-least one special charecter i.e [ @ or _ ] in the password.")
    else:
        print("Passord is valid.")
        valid=True
