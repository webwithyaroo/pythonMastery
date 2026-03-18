# A function in python is an object just like int you can store in into a variable, pass into another function and returned from another function



def name(name):
    return(f" Hello {name}")


say_hello = name #stored as a variable
# print(say_hello("Richie"))


# Pass a function to another function

def run_twice(func, value):
    return func(func(value))


def add_ten(x):
    return x + 10



# print(run_twice(add_ten, 5))






# *args allows a function to take any number of positional arguments  --- inside of a function it becomes a turple containing all extra arguments

def sum_all(*args):
    total = 0
    
    for num in args:
        total+=num
        
    return(total)    



# print(sum_all(1,2,3,4,5,6))

# **kwargs allows a function to take any number of keyword  arguments  --- inside of a function it becomes a dictionary containing all extra arguments


def display_details(**kwargs):
    """ Prints all keyword arguments."""
    
    for key, value in kwargs.items():
        print(f"{key} : {value }")
    
    
# display_details(name="olawale", age=30, city="New York")




def summarize(*args, **kwargs):
    print(f" Positional args: {args}")
    print(f" Keyword args: {kwargs}")
    
    
# summarize(1,2,3,4, name="olawale", age=40)







# Collect Arguments into turples
def numbers(*args):
    print(args)
# numbers(1,2,3,4,5,6)


# Collect keyword Arguments into dictionary
def key_arg(**kwargs):
    print(kwargs.values())


# key_arg(name ="yaro", age = 20)


# Order matters
def mix( *args, **kwargs):
    # print(a, b)
    print(args)
    print(kwargs)

# mix(1, 2, 3, 4, name="Yaroo", skill="Dev")


# Arguments unpacking

num = [1,2,3,4]
def add_num(a, b, c, d):
    print(d, a, c, b)

# add_num(*num)


dog = { "name":"speed", "age":25}

def dog_obj(name, age):
    print(name, age)
    
# dog_obj(**dog)


""" A function that 3 numbers and returns their average"""


def average_num(*nums)-> int:
    sum = 0
    
    for num in nums:
        sum += num
        
    total = sum / len(nums)
    
    return total   



result = average_num(2,3,4,5)
# print(result)



def ecommerce_checkout(*items, **details):
    new_items = ", ".join(items)
    item_header = (f"Items: {new_items}")

    
    details_list = [f"{key.title()}: {value}" for key, value in details.items()]
    print(details_list)
    # return "\n".join([item_header] + details_list)
    return "\n".join([item_header, *details_list])
    
    
result = ecommerce_checkout("Laptops","Mouse", name="Yaroo", location="Lagos", payment="Card")

print(result)



