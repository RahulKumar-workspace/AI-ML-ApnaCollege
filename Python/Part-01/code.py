print("hello world")
age = 35
print(type(age))

#NOTE: whaterver value we take input, by default it'll be a sting input:
b = input("enter b: ")
c = input("enter c: ")

d = b+c
print(d) # will consider b and c as strings and will be Concatinated.


#SOLN: take input as int:
e = int(input("enter b: "))
f = int(input("enter c: "))
g=e+f
print(g)