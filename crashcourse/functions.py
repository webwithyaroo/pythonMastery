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







def sum_all(**args):
    total = 0
    
    for num in args:
        total+=num
        
    return(total)    



print(sum_all[1,2,3,4,5,6])