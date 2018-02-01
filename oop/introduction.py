# GETTING STARTED

print("Hello world!")


# KEYWORDS AND IDENTIFIER

# invalid syntax:
# global = 1

# invalid syntax:
# a@ = 0


# STATEMENTS AND COMMENTS


# multi-line statement

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)
print(a)

colors = ['red',
          'blue',
          'green']
print(colors)

a = 1; b = 2; c = 3
print(a, b, c)


# identation

for i in range(1,11):
    print(i)
    if i == 5:
        break

if True:
    print('Hello')
    a = 5

if True: print('Hello'); a = 5


# comments

#This is a comment
#print out Hello
print('Hello')

#This is a long comment
#and it extends
#to multiple lines

"""This is also a
perfect example of
multi-line comments"""


# docstring

def double(num):
    """Function to double the value"""
    return 2*num

print(double.__doc__)


# DATATYPES


# variable assignment

a = 5
b = 3.2
c = "Hello"

print(a, b, c)


# multiple assignment

a, b, c = 5, 3.2, "Hello"
print(a, b, c)


# data types

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

a = 1234567890123456789
print(a)

b = 0.1234567890123456789
print(b)

c = 1+2j
print(c)


# list

a = [5,10,15,20,25,30,35,40]
print (a)
print("a[2] = ", a[2])
print("a[0:3] = ", a[0:3])
print("a[5:] = ", a[5:])


# tuple

t = (5,'program', 1+3j)
print("t[1] = ", t[1])
print("t[0:3] = ", t[0:3])

# Generates error:
#t[0] = 10


# string

s = "This is a string"
print(s)

s = '''a multiline
string'''
print(s)

s = 'Hello world!'
print("s[4] = ", s[4])
print("s[6:11] = ", s[6:11])

# Generates error:
#s[5] ='d'


#set

a = {5,2,3,1,4}
print("a = ", a)
print(type(a))

# Generates error:
#s[5] = 'd'


# dictionary

d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);

# Generates error:
#print("d[2] = ", d[2]);


# conversion

print(float(5))
print(int(10.6))
print(int(-10.6))
print(float('2.5'))
print(str(25))
# Generates error:
# print(int('1p'))
print(set([1,2,3]))
print(tuple({5,6,7}))
print(list('hello'))
print(dict([[1,2],[3,4]]))
print(dict([(3,26),(4,44)]))


# INPUT OUTPUT


# output

print('This sentence is output to the screen')

a = 5
print('The value of a is', a)
print('The value of a is %i' % a)

print(1,2,3,4)
#print(1,2,3,4,sep='*')
#print(1,2,3,4,sep='#',end='&')

print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)


# input

# num = input('Enter a number: ')
# print(num)


# import

import math
print(math.pi)

from math import pi
print(pi)


# OPERATORS


# arithmetic operators

print(2+3)

x = 15
y = 4

print ('x = 15')
print('y = 4')
print('x + y =', x+y)
print('x - y =', x-y)
print('x * y =', x*y)
print('x / y =', x/y)
print('x // y =', x//y)
print('x ** y =', x**y)


# comparation operators

x = 10
y = 12

print ('x = 10')
print('y = 12')
print('x > y  is', x>y)
print('x < y  is', x<y)
print('x == y is', x==y)
print('x != y is', x!=y)
print('x >= y is', x>=y)
print('x <= y is', x<=y)


# logical operators

x = True
y = False
print('x = True')
print('y = False')
print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)


# identity operators

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)


# membership operators


x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x)
print('hello' not in x)
print(1 in y)
print('a' in y)


# NAMESPACE AND SCOPE


a = 2
print('id(2) =', id(2))
print('id(a) =', id(a))

a = 2
print('id(a) =', id(a))
a = a+1
print('id(a) =', id(a))
print('id(3) =', id(3))
b = 2
print('id(2) =', id(2))

def printHello():
    print("Hello")
a = printHello()
a


# variable scope


def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)


def outer_function2():
    global a
    a = 20

    def inner_function2():
        global a
        a = 30
        print('a =', a)

    inner_function2()
    print('a =', a)


a = 10
outer_function2()
print('a =', a)

