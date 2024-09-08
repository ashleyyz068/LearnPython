name1 = "dave"

# def greeting(name): 
#     print(name)
# greeting("john")

# def another():
#     greeting("dave")

def another2():
    color = "blue"
    def greeting(name):
        global name1
        full_name = name1 + " " + name 
        print(full_name)
        nonlocal color 
        color ="blue"
        print(color)
    greeting("alice")

another2()