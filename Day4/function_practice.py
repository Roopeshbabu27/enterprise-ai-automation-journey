def my_function():
  print("Hello from a function")

my_function()

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("Last argument:", args[-1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)


def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

def myfunc():
  x = 300
  def myinnerfunc():
    x=200
    print(x)
  myinnerfunc()

myfunc()