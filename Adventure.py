from argparse import ArgumentParser
import sys
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.inventory = []
        self.health = int(health)

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

class Game(Player):
    def __init__(self, name, filepath, health):
        super().__init__(name, health)
        self.story_map = {}
        with open(filepath, "r", encoding = "utf-8") as f:
            story_id = None
            story_text = " "
            choices = {}
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) == 2:
                    story_id, story_text = parts
                    choices = {}
                elif len(parts) == 3:
                    choice_id, choice_text, result = parts
                    if result == "game_over":
                        choices[choice_id] = {"choice_text": choice_text, "is_game_over": True}
                    else:
                        choices[choice_id] = {"choice_text": choice_text, "next_story": result}
                else:
                    raise ValueError(f"Invalid line: {line}")
                self.story_map[story_id] = Story(story_id, story_text, choices)
            print(f"story_map: {self.story_map}")
   

    def play(self):
        current_story_id = "start"
        print(self.story_map.keys())
        while not self.story_map[current_story_id].get_choices().get("game_over", {}).get("is_game_over"):
            story = self.story_map[current_story_id]
            print(story.display_story())
            choices = story.get_choices()
            for choice_id, choice_data in choices.items():
                print(f"{choice_id}: {choice_data['choice_text']}")
            choice = input("Enter your choice: ")
            current_story_id = story.update_story(choice).get("next_story")
        print("Game Over")
        
def main():
    player_name = input("Enter your name: ")
    game = Game(player_name, "story.txt")
    game.play_game()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to stroy file")
    parser.add_argument("--name", help="player name (default: Player)", default="Player")
    parser.add_argument("--health", help="player health (default: 100)", type=int, default=100)
    args = parser.parse_args()
    main(args.filepath, args.name, args.health)
    

