#=================================Stack Implementation=================================
print("\n-------------------------------Stack-------------------------------------")
class stack1:
    values=[]
    def __init__(self):
        self.value=[]
    def push(self,x):
        self.value=[x]+self.value
    def pop(self):
        return self.value.pop(0)
s = stack1()
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.value)
s.pop()
print(s.value)

#=======================================Queue Implementation=============================
print("\n-------------------------------Queue-------------------------------------")
class queue1:
    values=[]
    def __init__(self):
        self.value=[]
    def enqueue(self,x):
        self.value=self.value+[x]
    def dequeue(self):
        return self.value.pop(0)
q = queue1()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.value)
q.dequeue()
print(q.value)

#=======================================Queue Implementation=============================
print("\n-------------------------------Binary Search Algorithm-------------------------------------")
array = [6,12,17,23,38,45,77,84,90]
target = 45
left=0
right=len(array)-1
check=False
while left<=right:
    mid = int((left+right)/2)
    if array[mid]==target:
        check=True
        break
    elif array[mid]<target:
        left=mid+1
    else:
        right=mid-1
        
if check==True:
    print("Target found Successfully!")
else:
     print("Target not found!")

