#Source to learn : BRO CODE VIDEO STAMPS :
#There are four Datatypes :

#STRING

first_name = "gnana"
last_name = "raj"
full_name = first_name+last_name
print(full_name)


#INTEGER
age  = 20
age += 1
print("My age is :"+ str(age))


#FLOAT

height = 180.5
print("My Height is :"+str(height)+"cm")


#BOOLEAN

human = True
print("you are a human :"+ str(human))



#Multiple assignments allows us to assign multiple variable at the same time in one line of code.
name,age = "Krishna",17
print(name)
print(age)

#Few Usefull Methods for strings
name = "gnanaraj"
print(len(name))
print(name.capitalize())
print(name.isalpha())
print(name.isdigit())
print(name.count("a"))
print(name.find("g"))
print(name.replace("a","o"))
print(name.upper())
print(name.lower())
print(name*3)

#Type Casting = convert the data type of a value to another datatype.

x = 1
y = 2.0
z = "3"

print("x is a number "+str(x)) #int
print("y is a number "+str(y)) #float
print("z is a number "+str(z)) #string


name = input("what is your name :")
age= int(input("what is your age :"))
height=float(input("What is you height :"))

print("Hello",name)
age = age + 1
print("your are "+str(age)+" years old")
print("you are "+str(height)+"cm taller")
















