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
                for attempt in range(retry):
                    
                    result = func(*args, **kwargs)
                    return result

            except Exception as e:
                print(f"Retry {attempt+1} failed")
        return wrapper
    return decorator

@time_execution(3)
def greet():
    print(3030)
greet()