def add_one(num):
    if (num<=9):
        return num  +1 
    
    total = num + 1
    print(total)

    return add_one(total)

# basically this calls the function again until num is; recursion is where the function calls itself