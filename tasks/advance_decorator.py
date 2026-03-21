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
            
            for attempt in range(retry):
                try: 
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Retry {attempt+1} failed")
                
           
            print("All retries failed")
        return wrapper
    return decorator

@time_execution(3)
def greet():
    print(home)
greet()