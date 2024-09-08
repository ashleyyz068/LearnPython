def hello():
    print("Hello World")

hello()

def sum(num1=4, num2=4):
    #these are default parameter values 
    if (type(num1) is not int or type(num2) is not int):
        return 
    #this would return none meaning that its not true or false 
    else:
        return num1 + num2

print(sum(2))

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("hi","bye","cool")

