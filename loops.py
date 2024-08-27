# for x in range(0, 100, 5): 
#     print (x)
# else: 
#     print ("glad")

names = ["hello", "bell", "anton"]
actions = ["codes", "east", "sleeps"]

for name in names:
    for action in actions:
        print (name + "is" +action)

value = 0

#double equal sign is used for comparision 
while value <= 10: 
    value +=1
    if value == 5: 
        continue 
    print(value)
    print("value equal: " + str(value))else:
    print("vlaue is now equal to " +str(value))

for x in "Mississippi": 
    if x == "s": 
        continue
    print (x)
# it includes the number that you start on but not the one that you stop on    
for x in range(2,4,2): 
    print(x)
    #this would include 2 but nothing else 
    



#break is not going to allow you to have that else statement 