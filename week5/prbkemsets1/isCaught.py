class Pokemon:
    def __init__(self, name, types, is_caught):
        self.name = name
        self.types = types
        self.is_caught = is_caught

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
    def catch(self):
        self.is_caught = True
        
squirtle = Pokemon("Squirtle", "Water", True)
squirtle.print_pokemon()