# Python resolves variable names using LEGB rule - it searches in this exact order

"""
L - Local 
E - Enclosing
G - Global
B - Built-in
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)    # prints "local" — found at L

    inner()
    print(x)        # prints "enclosing" — found at E

outer()
print(x)            # prints "global" — found at G
"""






count = 0

def increment():
    global count
    count += 1


increment()
print(count)



# Lambda function - one-line anonymous function


addition = lambda x, y: x + y

print(addition(16, 4))