#Problem 8: Pokemon Evolution
#Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, 
# each instance of Pokemon has an attribute evolution.
# The attribute will either be the default value of None or another Pokemon instance.

#Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

#The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.

class Pokemon():
    def __init__(self, name, types, evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

def get_evolutionary_line(starter_pokemon):
    evo_list = []
    while starter_pokemon:
        evo_list.append(starter_pokemon.name)
        starter_pokemon = starter_pokemon.evolution
    return evo_list

# Example evolution chain
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

# Testing the function
charmander_list = get_evolutionary_line(charmander)
print(charmander_list)  # ['Charmander', 'Charmeleon', 'Charizard']

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)  # ['Charmeleon', 'Charizard']

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)  # ['Charizard']
