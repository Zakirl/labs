import random


def remove_duplicate(numbers):
    x=[]
    i=0
    while i<len(numbers) :
        if(i==len(numbers)-1):
            x.append(numbers[i])
            break
        if numbers[i]==numbers[i+1] :
            x.append(numbers[i])
            i+=2
        else:
            x.append(numbers[i])
            i+=1    
    return(x)
print(remove_duplicate([1,2,3,3,4,5,6,6,7,7,8]))


print("------------------------------------------")


def split (myStr):
    length =len(myStr)
    if(length % 2 ==0 ):
        return([myStr[:(length//2)],myStr[(length//2):]])
    else:
        return([myStr[:(length//2+1)],myStr[(length//2)+1:]])

def concat(str1,str2):
    if (len(str1) == 0 or len(str2)==0):
        return("enter valid strings")
    else :
        str1=split(str1)
        str2=split(str2)
        print(str1,str2)
        return(str1[0]+str2[0],str1[1]+str2[1])    

print(concat("ahmed","zaki"))


print("------------------------------------------")


def check_duplicates(numbers):
    return len(numbers)==len(set(numbers))

print(check_duplicates([1,2,3,1]))

print("------------------------------------------")

def bubble(numbers):
    
    for j in range (len(numbers)):
        op=0
        for i in range(1,len(numbers)):
            if numbers[i]<numbers[i-1]:
                temp=numbers[i]
                numbers[i]=numbers[i-1]
                numbers[i-1]=temp
                op+=1
        if op==0:
            return(numbers)                
  
print("bubble sort :",bubble([13,4,6,3,9,0,-10,9,11]))

print("------------------------------------------")


def game():
    rand = random.randint(0, 100)
    i=0
    guessed=[]

    while(i<10):
        print("")
        state=0
        user_input=int(input("Enter a number between 0 and 100 : "))
        if user_input in guessed:
            print("you used this number before")
            continue
        guessed.append(user_input)
        if(user_input>100 or user_input<0):
            print("please enter a number between 0 and 100") 
            continue
        elif user_input> rand : 
            print("your number is bigger than the random number ")
            print(f"you have {10-i-1} more tries")   
            i+=1      
        elif user_input < rand: 
            print("your number is smaller than the random number ")
            print(f"you have {10-i-1} more tries") 
            i+=1
        elif user_input==rand:
            print("congrats ")
            print(f"you can now guess another number")
            rand = random.randint(0, 100)
            guessed=[]
            state=1
            i+=1

    check=input("do you want to play again ? (y/n)")
    if check =='y':
        game()
game()



