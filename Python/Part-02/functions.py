# def sum(a, b=1):
#     sum = a+b
#     return sum
# print(sum(4,7))
# print(sum(4)) # default parameter = 1
# print(sum(7)) # default parameter = 1

'''
NOTE: default parameter will always be in the last not in the first 
eg = sum(a, b=2) -> correct
    sum(a=2, b) -> incorrect
'''


'''
LAMBDA FUNCTOINS:
used for high order functions -> Functions who take any funct value in their parameter or
                                they return any function from itself.
chote mote kaam ke liye
'''

# sum = lambda a,b : a+b
# avg = lambda a,b : (a+b)/2
# print(sum(5,10))
# print(avg(5,10))


#Q: FACTORIAL

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

n = int(input("Enter no: "))
print(factorial(n))