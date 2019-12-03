
# code to check if a reversed string is the same as an input string
def my_print_function(): # No parameters
  x = "ddddd"
#   y = ''.join(reversed(x))
  y = x[::-1] # another reverse technique
  # z = x.split(',')
#   a = x[0:-1]
#   g = ''.join(a)
  if (y==x):
      print("They are equal")
  else:
      print("They are not equal")    
my_print_function()

num1 = 10
num2 = 20
result = 4000
print("---------------")
 
# function within function[mini-calc]

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def calc(operation, a,b):
    return operation(a,b)
result=calc(add, 10,5)
print(result)


# lambda functions
print("---------------")
def check(operation,x,y):
    return operation(x,y)
val = check(lambda x, y: x* y, 10,10)
print (val)

print("---------------")

listt = "4 4"
num_list =listt.split()
double_list = map (lambda n : n * 2, num_list)
print (list(double_list))

print("---------------")

numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = filter(lambda n : n > 10, numList)
print (list(greater_than_10))


print("---------------")

# recursion functions
def rec_count (number):
    # to count down a number
  print (number)
  # Base case
  if number == 0:
    return 
  rec_count (number - 1) # A recursive call with a different argument
  print (number) # optional

rec_count (5)


print("---------------")

# print "333333333344444"
def rep_cat(x, y):
    return str(x) * 10 + str(y) * 5

res = rep_cat(3,4)    
print(res)

print("---------------")

def factorial(n):
    if n <= 1:
      return n
    if n == 2 or n <= 3:
      return n * (n-1)  
    else:
      return n *(n-1) * (n-2)  * (n-3) * (n-4)

res = factorial(5)   
print(res)

# with recursion
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    if n < 0:
        return -1
    # Recursive call
    return n * factorial(n - 1)
res = factorial(5)  
print(res)  

def mod(b):
    if (b % 2) == 0:
     print("even")
    else:
     print("odd")
res = mod(20)
print(res)  