class Player:
    def __init__(self, name, health):
        self.name = name
        self.inventory = []
        self.health = 100

    def add_item(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {self.inventory}")
        
    def is_alive(self):
        return self.health > 0

