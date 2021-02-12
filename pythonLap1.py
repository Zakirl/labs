import math


first_name =input("enter your first name :")
last_name =input("enter your last name :")
print(last_name,first_name)


print("\n---------------------------------\n")


n= int(input("enter number"))
print(n+n*n+n*n*n)

print("\n---------------------------------\n")


mystr= """a string that you "don't" have to escape
This
is a .......\n multi-line
heredoc string --------> example"""
print(mystr)


print("\n---------------------------------\n")


volume= (4/3)*(math.pi)*(5**3)
print(volume)

print("\n---------------------------------\n")

base =float(input("enter triangle base :"))
height =float(input("enter triangle height :"))
print(f"triangle area is : {(base*height)/2}")

print("\n---------------------------------\n")


for i in range(1,6):
    for j in range(i):
        print ('*',end="")
    print("")
for i in range(4,0,-1):
    for j in range(i):
        print ('*',end="")
    print("")

print("\n---------------------------------\n")

name=input("enter your name :")
rev_name=""
for i in range(len(name)-1,-1,-1):
    rev_name+=name[i]
print(rev_name)


print("\n---------------------------------\n")

for i in range(7):
    if(i==3 or i==6):
        continue
    print(i)        


print("\n---------------------------------\n")

n1=0
n2=1
while n1 < 50 :
    print(n1,end=" ")
    nn=n1+n2
    n1=n2
    n2=nn


print("\n---------------------------------\n")


digits=0
letters=0
mystr= input("enter a string: ")
for char in mystr:
    if char.isdigit():
        digits+=1
    elif char.isalpha():
        letters+=1
print(f"digits:{digits}, letters: {letters}")    
   
