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
    print(303)
# greet()


import time
def rate_limit(seconds: int):
    def decorator(func):
        last_called = 0
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_called
            now = time.time()
            print(now)
            if now - last_called < seconds:
                print("Too many requests")
                return 
            
            last_called = now 
            return func(*args, **kwargs)
        
        
        return wrapper
    return decorator

@rate_limit(3)
def func():
    print(103)
func()
time.sleep(3)
func()
time.sleep(3)
func()
time.sleep(3)
func()