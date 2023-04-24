from argparse import ArgumentParser
import sys
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

class Game(Player):
    def __init__(self, name, filepath, health):
        super().__init__(name, health)

        self.story_map = {}
        with open(filepath, "r", "utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()

    def __init__(self, player_name, story_id, story_text, choices):
        self.player = Player(player_name, health=100)
        self.story = Story(story_id, story_text, choices)

    def play(self):
        while not self.story.is_game_over():
            print(self.story.display_story())
            choices = self.story.get_choices()
            for choice_id, choice_data in choices.items():
                print(f"{choice_id}: {choice_data['choice_text']}")
            choice = input("Enter your choice: ")
            self.story.update_story(choice)
        print("Game Over")
        
def main():
    player_name = input("Enter your name: ")
    game = Game(player_name, "story.txt")
    game.play_game()

if __name__ == "__main__":
    main()
        
def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file where
    each line consists of a name, a tab character, and a phone number.
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="file of story")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)