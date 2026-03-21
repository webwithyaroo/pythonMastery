""" This modules builds a logger func that prints the fucntions states"""
from functools import wraps
from time import time

def logger(func):
    @wraps(func) # Remembers what the func is 
    
    # 1 - Extra capabilities
    def wrapper(*args, **kwargs):
        # print(f"Calling {func.__name__} with args {args}")
        result = (func(*args, **kwargs))
        # print(f"Result: {result}")
        # print(f"{func.__name__} finished")
        return result
    return wrapper

@logger
def add(a, b):
    """ This function adds a, b"""
    return(a + b) 

# print(add.__name__)
# print(add.__doc__)
add(2, 3)



"""🔥 FINAL DECORATOR CHALLENGE (Don’t Skip This)"""

def require_auth(func):
    @wraps(func)  # Remembers what the func is 
    
    def wrapper(*args, **kwargs):
        user = kwargs.get("user")
        if not user:
            print("Unauthorized")
            return
        
        # print(f"Authorized User {user}")
        result = func(*args, **kwargs)
        return result
    return wrapper



@require_auth
def get_dashboard(*args, **kwargs):
    print("Welcome to dashboard")
        
# get_dashboard(user="olawale")


""" This function deletes users based on Role"""


def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("role")
    
            if user_role and user_role.lower() == role.lower():
                print(f"[AUTH] {user_role} authorized for {func.__name__}")
                return func(*args, **kwargs)
            
            return f"Access denied for role: {user_role}"
        return wrapper
    return decorator

@require_role(role ="Admin")
def delete_user(*args, **kwargs):
    print("user deleted")
    
# delete_user(role ="Admin")


# when func start
# when func ends

# time took = end-start

import time
def time_execution(func):
    @wraps(func)
    
    def wrapper(*args, **kwargs):
        func_start = time.perf_counter()
        result = func(*args, **kwargs)
        func_end = time.perf_counter()
        
        duration =  func_end - func_start
        print(f"Function {func.__name__} took {duration:.4f} seconds")
        
        return result
        
    return wrapper



@time_execution
def greet():
    time.sleep(1.5)
    print("Task Complete!")
    
# greet()


""" catching in decorator  memoization"""


def cache(func):
    storage = {}

    @wraps(func)
    def wrapper(*args):
        if args in storage:
            print("Fetching from cache...")
            return storage[args]

        result = func(*args)
        storage[args] = result

        return result

    return wrapper


@cache
def slow_square(n):
    time.sleep(2)
    result =  n * n
    print(result)

# slow_square(4)  # slow
# slow_square(4)  # instant ⚡



import time
from functools import wraps

def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {attempt+1} failed")
                
            print("All retries failed")
        return wrapper
    return decorator

@retry(3)
def er():
    print("hello")
er()   