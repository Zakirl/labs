import collections ,math
import sys
file_name=sys.argv[1]
f = open(file_name,'r')
text=f.read()
f.close()
words={}
for word in text.split() :
    if word in words:
        words[word] +=1
    else:
        words[word] = 1
word_counter=collections.Counter(words)
most = open("popular_words.txt", "w")
for word, count in word_counter.most_common(20):
    most.write(f"word :{word} , count: {count} \n")


print("----------------------------------------------------------------")


def distance(x1,y1,x2,y2):
    return( math.sqrt(pow(x2 - x1,2) + pow(y2 - y1,2)) )

print("distance",distance(2,3,2,5))

print("----------------------------------------------------------------")

# class Vehicle :
#     pass

class Vehicle:
    def __init__(self, max_speed, mileage ):
        self.max_speed = max_speed
        self.mileage  = mileage 
car_1 = Vehicle(20,1000)
print(car_1.max_speed)


print("----------------------------------------------------------------")



def rev_str(mystr):
    words=mystr.split()
    return(' '.join(reversed(words)))

print(rev_str("this string is reversed"))



print("----------------------------------------------------------------")


class printStr:
    def get_String(self,myStr):
        self.myStr=myStr

    def  print_String(self):
        print(self.myStr)

p1=printStr()
p1.get_String("string")
p1.print_String()


print("----------------------------------------------------------------")


class Circle:
    def __init__(self, radius  ):
        self.radius  = radius 
    def area (self):
        return((math.pi)*(self.radius**2))
    def perimeter (self):
        return((math.pi)*2*(self.radius))

c1=Circle(3)        
print("area",c1.area())
print("perimeter",c1.perimeter())