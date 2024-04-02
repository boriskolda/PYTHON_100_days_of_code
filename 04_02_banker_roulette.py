names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")

from random import randint

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = randint(0, num_items - 1)
# Choose and print a random name.
print(f"{names[randint(0,len(names)-1)]} is going to buy the meal today!")