str ='email@123'
print('@' in str)


def numcount(num):
    while num > 0:
        yield num
        num -= 1

for i in numcount(5):
    print(i)

#  💡 Analogy

# Think of the generator (numcount) as a vending machine that dispenses numbers one by one.

# The while loop inside controls when the machine stops dispensing.

# The for loop outside is you pressing the button repeatedly to get each number.
# You need both: one to produce, one to request.

# 🧩 Why you need the for loop (or something like it)

# Without the for, the generator won’t automatically keep asking for values.
# You’d have to do it manually, like:

# g = numcount(5)
# print(next(g))
# print(next(g))
# print(next(g))
# # etc.


# So for is just a convenient way to call next() repeatedly until the generator is done.