"""
DECORATION
- catching or memoization
- timing function
- role permission
- logging fun names, arg, deburging
- input validation
- rate limit
- 
    """
    
from functools import wraps
def time_execution(retry=3):
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                for num in range(retry):
                    print(f"{num} retry")
                    result = func(*args, **kwargs)
                    return result

            except Exception as e:
                print("The function failed to run")
                raise e
        return wrapper
    return decorator

@time_execution(3)
def greet():
    print(home)
greet()