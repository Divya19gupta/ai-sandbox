'''
slicing works like [start:stop:step]
'''

str = 'string'
print(str[0:3:1])
print(str[::]) #access whole string
print(str[::-1]) #access in reverse

print(str * 20) #repeat 20 times
# print(str + 20) #will give error