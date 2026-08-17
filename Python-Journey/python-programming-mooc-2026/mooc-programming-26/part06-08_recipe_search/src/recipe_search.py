#returns recipe in a dictionary list
def parse_recipe(filename: str):
    #Store each recpie stanza as lists
    recipes = [[]]
    with open(filename) as new_file:
        i=0
        for line in new_file:      
            if line=="\n":
                i+=1
                recipes.append([])
                continue
            recipes[i].append(line.replace('\n',''))

    #parse the stanza lists into a dictionary of items
    complete_recipe = []
    for recipe in recipes:
        new_dict = {}
        new_dict["name"]=recipe[0]
        new_dict["time"]=int(recipe[1])
        ingredients=[]
        for i in range(2,len(recipe)):
            ingredients.append(recipe[i])
        new_dict["ingredients"]=ingredients
        complete_recipe.append(new_dict)
    return complete_recipe

def search_by_name(filename: str, word:str):
    recipe_dictionary = parse_recipe(filename)
    result = []
    for recipe in recipe_dictionary:
        if word.lower() in recipe["name"].lower():
            result.append(recipe["name"])
    return result

def search_by_time(filename: str, prep_time: int):
    recipe_dictionary = parse_recipe(filename)
    result = []
    for recipe in recipe_dictionary:
        if recipe["time"]<prep_time:
            new_str = f'{recipe["name"]}, preparation time {recipe["time"]} min'
            result.append(new_str)
    return result

def search_by_ingredient(filename: str, ingredient: str):
    recipe_dictionary = parse_recipe(filename)
    result = []
    for recipe in recipe_dictionary:
        if ingredient in recipe["ingredients"]:
            new_str = f'{recipe["name"]}, preparation time {recipe["time"]} min'
            result.append(new_str)
    return result

if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)