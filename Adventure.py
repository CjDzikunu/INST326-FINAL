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
    
class Story:
    def __init__(self, story_id, story_text, choices):
        self.story_id = story_id
        self.story_text = story_text
        self.choices = choices
    
    def display_story(self):
        return self.story_text
    
    def get_choices(self):
        return self.choices
    
    def update_story(self, choice):
        return self.choices.get(choice, None)

class Game:
    def __init__(self, name, filepath):
        self.player = Player(name)
        self.story_map = {}
        with open(filepath, "r", "utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()


def main():
    player_name = input("Enter your name: ")
    game = Game(player_name, "story.txt")
    game.play_game()

if __name__ == "__main__":
    main()
