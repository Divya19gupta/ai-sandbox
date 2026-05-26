
val = '''multistring I can set'''

print(val)
print(val[1])
print(val[-1]) #2 indexed

for i in val:
    print(i+' ') #3 iterable

val = 34 #immutable
print(val)



'''
1) STRINGS ARE MUTABLE
Mutable (list):
nums = [1, 2, 3]
nums[0] = 9   # ✅ works
print(nums)   # [9, 2, 3]

Immutable (string):
word = "cat"
word[0] = "b"  # ❌ error
word = "bat"   # ✅ new string created, old one untouched


So when you “change” a string, what you’re really doing is:
not editing it
but replacing it with a brand new one.
That’s what “immutable” means — not “you can’t change variables,” but “you can’t modify the actual object once created.”

2) STRINGS ARE INDEXED:
keep in mind it gives index to space as well

3) STRINGS ARE ITERABLE

'''