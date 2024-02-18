
""""Demonstrate Basic List"""

#Initialize an empty list
grocery_list: list[str] = list() #is a list constructor
grocery_list: list[str] = [] #literal


print(grocery_list)

#add an item to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print(grocery_list)

#create an already populated list
grocery_list2: list[str] = ["bananas", "milk", "bread"]
print(grocery_list2)
grocery_list2.append("eggs")

print(grocery_list2)
print(grocery_list[0])

#modifying by index
grocery_list[1] = "almond milk"
print(grocery_list)


#measuring length
print(len(grocery_list))

#remove item from list
grocery_list.pop(1)
print(grocery_list)

#Function name: display
# parameter: list[str]
#return nothing
#print out the list

def display(word: list[str])-> None:
    print(word)
display(grocery_list)
x = display(["alyssa", "erin"])
print(x)

#create a list!
#name: create
#parameters: str and str
#RV: list[str]
# put both parameters into list and return that list

def create(word1: str, word2: str) -> list[str]:
    my_list: list[str] = [word1, word2]
    return my_list

print(create("Hello", "world"))
#or do this
x: list[str] = create("Hello", "world")
print(x)


print(grocery_list)

print["eggs","bananas"][1]