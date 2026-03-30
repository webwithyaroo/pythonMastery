"""This module teaches file handling in python as the       process of 
    creating, writing, updating and reading from a file, just like notebook
    """
    
""" 3 operations involved are:
    open
    write
    close \\ always close a file
    """

file = open("service.pdf", "w")
write_file = file.write(" This is a service file ")
file.close() # Always close file



append_file = open("service.pdf", "a")
append_file.write("\n New line added safely")
append_file.close()

read_file = open("service.pdf", "r")
print(read_file.read())
read_file.close()

