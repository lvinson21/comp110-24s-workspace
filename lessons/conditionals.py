"""Demonstate behavior of conditionals"""

user_input: str = input("Pick a Number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))

# if user number is even, print "even"
if user_number %2 == 0:
    print("even")
else: #user number is odd
    print ("odd")


print(user_input)