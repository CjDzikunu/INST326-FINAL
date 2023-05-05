from argparse import ArgumentParser
import sys
import json

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.inventory = []
        self.health = 100

    def add_item(self, item):
        self.inventory.append(item)

    def display_inventory(self):
        print(f"{self.name}'s Inventory: {self.inventory}")
        
    def is_alive(self):
        return True if self.health > 0 else False
    
    def __add__(self, operator):
        new_player = Player(self.name, self.health + operator)
        return new_player
        
    def __sub__(self, operator):
        new_player = Player(self.name, self.health - operator)
        return new_player
    
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
        if not choice:
            return None

        if isinstance(choice, str):
            choice_id = choice.strip()
        next_story = self.choices.get(choice_id)
          
        
        return next_story

class Game(Player):
    def __init__(self, filepath, name, health):
        super().__init__(name, health)

        self.story_map = {}
        with open(filepath, "r") as f:
            data = json.load(f)
            for story_id, story_data in data.items():
                story_text = story_data.get("story_text")
                choices = story_data.get("Choice")
                self.story_map[story_id] = Story(story_id, story_text, choices)

    def play(self):
        current_story_id = "start"
        
        while True:
            if current_story_id.__contains__("game_over"):
                story_is_over = self.story_map[current_story_id]
                print(story_is_over.display_story())
                print("Game Over")
                break
            story = self.story_map[current_story_id]
            print()
            print(story.display_story())
            choices = story.get_choices()
            print()
            if not choices:
                break
            while True:
                for choice_id in choices:
                    print(f"{choice_id}:")
                choice = input("Enter your choice: ")
                    
                current_story_id = story.update_story(choice)
                if current_story_id:
                    break
                print("Invalid choice. Please try again") 
            

        
def main(filepath, name, health):
    name = input("Enter your name: ")
    game = Game(filepath, name, health)
    game.play()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to story file")
    parser.add_argument("--name", help="player name (default: Player)", default="Player")
    parser.add_argument("--health", help="player health (default: 100)", type=int, default=100)
    args = parser.parse_args()
    main(args.filepath, args.name, args.health)