#Problem 8: Pokemon Evolution
#Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, 
# each instance of Pokemon has an attribute evolution.
# The attribute will either be the default value of None or another Pokemon instance.

#Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

#The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.
class Pokemon:
    name = ""
    types = []
    is_caught = False
    
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
        
    def add_type(self, new_type):
        self.types.append(new_type)



def get_by_type(my_pokemon, pokemon_type):
    lst = []
    for pokemon in my_pokemon:
        for i in pokemon.types:
            if i == pokemon_type:
                lst.append(pokemon.name)

                
        
        
            
    
    return lst

jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
#print(jigglypuff.print_pokemon())