print('# ITERATOR')


print('# iterators')

my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())
try:
    next(my_iter)
except StopIteration:
    print('No more')


for element in my_list:
    print(element)


print('# building iterator')


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

a = PowTwo(4)
i = iter(a)

try:
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
except StopIteration:
    pass

for i in PowTwo(5):
    print(i)


print('# infinite iterators')

class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

a = iter(InfIter())
print(next(a))
print(next(a))
print(next(a))
print(next(a))


print('# GENERATOR')


def my_gen():

    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed last')
    yield n

a = my_gen()

print(next(a))
print(next(a))
print(next(a))

# already iterated
for item in a:
    print(item)

for item in my_gen():
    print(item)


# generators with a loop

def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
for char in rev_str("hello"):
     print(char)


# generator expression

my_list = [1, 3, 6, 10]
print(my_list)

for x in [x**2 for x in my_list]: # comprehension
    print(x)

for x in (x**2 for x in my_list): # generator
    print(x)


# easy to implement

def PowTwoGen(max = 0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

for item in PowTwoGen(5):
    print(item)


# infinite stream


def all_even():
    n = 0
    while True:
        yield n
        n += 2

all_even = all_even()
print(next(all_even))
print(next(all_even))
print(next(all_even))
print(next(all_even))

# pipelining generators


with open('sells.log') as file:
    pizza_col = (line[3] for line in file)
    per_hour = (int(x) for x in pizza_col if x != 'N/A')
    print("Total pizzas sold = ",sum(per_hour))


print('# CLOSURE')


# nested function

def print_msg(msg):
    def printer():
        print(msg)
    printer()

print_msg('Hello')


# closure function

def print_msgc(msg):
    def printer():
        print(msg)
    return printer

hello = print_msgc("Hello")
hello()


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(times5(times3(2)))


print('# DECORATORS')


def first(msg):
    print(msg)

first("Hello")
second = first
second("Hello")


print('# higher order functions')

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))
print(operate(dec,3))

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

new()


print('# decorators')


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

ordinary()
pretty = make_pretty(ordinary)
pretty()

ordinary = make_pretty(ordinary)
ordinary()

def new_pretty(func):
    def inner():
        print('new pretty')
        func()
    return inner

@new_pretty
def old_ugly():
    print('old ugly')

old_ugly()


print('# decorating with parameters')


def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return a/b

print(divide(2,5))
print(divide(2,0))

def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner

@works_for_all
def some_func(a, b, c):
    return a + b + c

print(some_func(1, 2, c=3))


print('# chaining decorators')


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")


print('# PROPERTY')


class Celsius1:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

man = Celsius1()
man.temperature = 37
print(man.temperature)
print(man.to_fahrenheit())

class Celsius2:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

c = Celsius2(37)
print(c.get_temperature())
c.set_temperature(10)
c._temperature = -300
print(c.get_temperature())

class Celsius3:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

c = Celsius3()
print(c.temperature)

c.temperature = 37
print(c.to_fahrenheit())

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius()
print(c.temperature)

c.temperature = 37
print(c.to_fahrenheit())
