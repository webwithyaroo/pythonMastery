""" Delogger_decorator(greet)corator - A function that wraps another functions"""
""" logger_deco is the wraper that contains extra abilites (wrapper) and it wraps  the func greet"""
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper


@logger_decorator
def greet(a, b):
    return (a + b)

# greet(5, 10) 


from datetime import datetime
def auto_log(func):
    def wrapper(*args, **kwargs):
        # Automatically logs the function call using your previous logic
        print(f"[{datetime.now()}] EXECUTING: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@auto_log
def save_user_data():
    print("Saving to database...")

save_user_data()
