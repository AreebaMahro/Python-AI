# if, if-else, else-if statements

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

# for loop

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
l = ["Areeba", "Nadia", "Aqsa"]
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
