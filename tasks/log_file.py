def write_log(message: str):
    with open("app.log", "w") as file:
        file.write(message)
    with open("app.log", "r") as file:
        print(file.read())
        
        
        
write_log("Server started")
write_log("User logged in")
