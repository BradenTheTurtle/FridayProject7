# Mad Libs Game

# Welcome message for the user
print("Welcome to the Mad Libs Game!")

# Prompt the user for inputs
large_object = input("Enter a large object: ")  # Get a large object
large_objects_plural = input("Enter large objects (plural): ")  # Get plural large objects
adjective = input("Enter an adjective: ")  # Get an adjective
body_part = input("Enter a body part: ")  # Get a body part
restaurant = input("Enter a restaurant: ")  # Get a restaurant name
food_1 = input("Enter a food: ")  # Get the first food
food_2 = input("Enter another food: ")  # Get the second food

# Print the generated Mad Lib story
print("\nHere's your Mad Lib story:\n")
print(f"I’ve had a very {adjective} day.")  # Story line with adjective
print(f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.")  # Story line with plural objects and body part
print(f"Then, at lunch, I went to {restaurant} for their delicious {food_1},")  # Story line with restaurant and first food
print(f"But the waiter brought me {food_2}, which I was not hungry for.")  # Story line with the second food
print(f"Finally, on my way home, I was cut off by a van with a large {large_object} strapped to the roof.")  # Story line with large object

