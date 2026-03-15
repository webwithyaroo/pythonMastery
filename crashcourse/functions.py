# A function in python is an object just like int you can store in into a variable, pass into another function and returned from another function



def name(name):
    return(f" Hello {name}")


say_hello = name #stored as a variable
print(say_hello("Richie"))


# Pass a function to another function

def run_twice(func, value):
    return func(func(value))


def add_ten(x):
    return x + 10



print(run_twice(add_ten, 5))






# *args allows a function to take any number of positional arguments  --- inside of a function it becomes a turple containing all extra arguments

def sum_all(*args):
    total = 0
    
    for num in args:
        total+=num
        
    return(total)    



print(sum_all(1,2,3,4,5,6))

# **kwargs allows a function to take any number of keyword  arguments  --- inside of a function it becomes a dictionary containing all extra arguments


def display_details(**kwargs):
    """ Prints all keyword arguments."""
    
    for key, value in kwargs.items():
        print(f"{key} : {value }")
    
    
display_details(name="olawale", age=30, city="New York")