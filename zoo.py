# Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("giraffes", "pandas", "spider monkeys", "mollusks", "lynx", "squid", "rabbits", "cats", "dogs", "horses")
# Find one of your animals using the tuple.index(value) syntax on the tuple.
# Example
# flowers = ("daisy", "rose")
# print(flowers.index("rose")) # Output is 1
print(zoo.index("lynx")) 
# print(zoo.index("sparrow")) 
# Determine if an animal is in your tuple by using value in tuple syntax.
animal_to_find = "lynx"
if animal_to_find in zoo:
    # Print that the animal was found
    print(f"{animal_to_find} was found")
# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"
# Create a variable for the animals in your zoo tuple, and print them to the console.
animals = ("giraffes", "pandas", "spider monkeys", "mollusks", "lynx", "squid", "rabbits", "cats", "dogs", "horses")
(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10) = animals
# Convert your tuple into a list.
animals = list(animals)
print(animals)
# Use extend() to add three more animals to your zoo.
animals.extend(["baracuda"])
animals.extend(["french bulldog"])
animals.extend(["kangaroo"])
# Convert the list back into a tuple. 
animals = tuple(animals)
print(animals)
print(type(animals))