""" This modules builds a logger func that prints the fucntions states"""
from functools import wraps

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
            
            if not user_role:
                print("Access denied: No role provided")
                return
    
            if user_role.lower() != role.lower():
                print("Access denied")
                return
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role(role ="Admin")
def delete_user(*args, **kwargs):
    print("user deleted")
    
delete_user()