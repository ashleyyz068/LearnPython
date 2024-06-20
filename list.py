user = ['jojo', 'bella', 'me']
print ('jojo' in user)
print(user[0])
print(user[-1])
print(user.index('me'))
user.append('elal')
user += ['dude', 'bro']
print(user)
#this indicates that you replace starting and ending at the same position so it didn't replace any values
user[2:2] = ['eddie', 'bob']
print(user)
#replace items in a list ; slice; this starts at 1 and ends at 2
user[1:3] = ['robert', 'amy']
print(user)
del user[0]
print(user)
user[1:2] =  ["Dave"]
#ignores the fact that it is uppercase because upper case automatically foes in teh front 
user.sort(key=str.lower)
print(user)

mytuple = tuple(('dave', 42, True))

