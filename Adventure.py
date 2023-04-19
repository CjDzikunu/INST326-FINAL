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
    def __init__(self,story_id,story_text,choices):
        self.story_id =story_id
        self.story_text = story_text
        self.choices = choices
        
    def display_story(self):
        return self.story_text
    
    def get_choices(self):
        return self.choices
    
    def update_story(self, choice):
        return self.choices.get(choice, None)

class Game:
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
