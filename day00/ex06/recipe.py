
from audioop import add
from re import split


cookbook = {
    "Sandwich": {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_the_cookbook():
    for k in cookbook:
        print(k)


def print_recipe_details(name):
    if name not in cookbook:
        print("Sorry, this option does not exist.")
        return
    print(f"Ingredients list: {cookbook[name]['ingredients']}")
    print(f"To be eaten for {cookbook[name]['meal']}.")
    print(f"Takes {cookbook[name]['prep_time']} minutes of cooking.")


def add_recipe(name, ing, meal, time):
    dec = {
        "ingredients": ing,
        "meal": meal,
        "prep_time": time
    }
    cookbook[name] = dec


def delete_recipe(name):
    del cookbook[name]


print("Welcome to the Python Cookbook !")
print("""
List of available option:
  1: Add a recipe
  2: Delete a recipe
  3: Print a recipe
  4: Print the cookbook
  5: Quit
""")

while(True):
    option = input("Please select an option:\n>> ")
    name = ""
    ings = []
    ing = ""
    meal = ""
    time = 0
    i = 0

    if (option == '1'):
        name = input("Enter a name:\n>>> ")
        print("Enter ingredients:")
        ing = input()
        while (ing != ""):
            ings.append(ing)
            ing = input()
        meal = input("Enter a meal type:\n>>> ")
        time = input("Enter a preparation time:\n>>> ")
        add_recipe(name, ings, meal, time)
    elif (option == '2'):
        name = input("Please enter a recipe name to delete:\n>> ")
        delete_recipe(name)
    elif (option == '3'):
        name = input("Please enter a recipe name to get it's details:\n>> ")
        print("")
        print_recipe_details(name)
        print("")
    elif (option == '4'):
        print("")
        print_the_cookbook()
        print("")
    elif (option == '5'):
        exit()
    else:
        print("Sorry, this option does not exist.\n")
