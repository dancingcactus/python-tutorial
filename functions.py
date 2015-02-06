#Created by Justin Grover 2015

################################
# Tutorial on how functions work in Python using minecraft py
################################



# A function is bunch of code that you can call to execute and it will do something for you. 
# A function is usually denoted by the parenthesis
# print() is an example of a function. If you give it a string it will take care of printing it out to the string
print("This is a function call")

# You can define your own functions by using the following syntax
#######
# def function_name(argument, argument, ...):
#   Some code
#   return a_value
#######

# The return statement is optional


####### Simple Function ######
# This is a simple function to add two numbers together. 
# It takes an argument of a and an argument of b and adds them together
# Then it returns the result
def add(a,b):   
    return a + b


# Now I can call the function like this 
result = add(321,123)
#Let's see what it returned
print(result)
# Output: 444

# I can now use this function to add anytwo numbers together. 

####### Nested Function ########
# In this example we are going call another function within our own function. 
def print_name(firstname,lastname):
    print("Your Name is "+firstname + " " + lastname)
    
# Lets call it and see what happens
print_name("Justin", "Grover")
# Output: Your Name is Justin Grover

# Notice that this function didn't return anything and that is okay.


