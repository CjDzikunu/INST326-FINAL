from argparse import ArgumentParser
import sys
import json

class Player:
    """A class representing the player character in a story.
    
    Attributes:
        name (str): the player's name.
        inventory (list): a list containing all of the items 
            a player will pick up.
        health (int): the amount of health points a player has.
    """
    def __init__(self, name, health=100):
        """Initializes a Player object.
        
        Args:
            name (str): the player's name.
            health (int): the amount of health points a player has.
                
        Side Effects:
            Initializes name, inventory, and health.
        """
        self.name = name
        self.inventory = []
        self.health = 100

    def add_item(self, item):
        """Appends an item to an inventory list.
        
        Args:
            item (str): the item that will go into a player's inventory.
        """
        self.inventory.append(item)

    def display_inventory(self):
        """Prints the player's current inventory.
        
        Side Effects:
            Prints result as an f-string.
        """
        print(f"{self.name}'s Inventory: {self.inventory}")
        
    def is_alive(self):
        """Checks player's current health to see if they are alive.
        
        Returns:
            True: if health is greater than 0.
            False: if health is less than 0.
        """
        return True if self.health > 0 else False
    
    def __add__(self, operator):
        """Returns a new Player object with the player's health 
            increased by the given operator.
            
            Args:
                operator (int): the amount that will be added to
                    the player's health.
            
            Returns:
                new_player (Player): the new player object 
                    and their health.
        """
        new_player = Player(self.name, self.health + operator)
        return new_player
        
    def __sub__(self, operator):
        """Returns a new Player object with the player's health 
            decreased by the given operator.
            
            Args:
                operator (int): the amount that will be added to
                    the player's health.
            
            Returns:
                new_player (Player): the new player onject and their 
                    health.
        """
        new_player = Player(self.name, self.health - operator)
        return new_player
    
class Story:
    """A class representing the story for the game.
    
    Attributes:
        story_id (str): a unique key for each possible story path.
        story_text (str): the text in the story.
        choices (dict): the available choices the player can pick as
            their story path.
    """
    def __init__(self, story_id, story_text, choices):
        """Initializes a Story object.
        
        Args:
            story_id (str): a unique key for each possible story path.
            story_text (str): the text in the story.
            choices (dict): the available choices the player can pick as 
                their story path.
                
        Side Effects:
            Initializes story_id, story_text, and choices.
        """
        self.story_id = story_id
        self.story_text = story_text
        self.choices = choices
    
    def display_story(self):
        """Returns the story's current text.
        
        Returns:
            self.story_text: the current text in the story.
        """
        return self.story_text
    
    def get_choices(self):
        """Returns the avaible choices for the given point in the story.
        
        Returns:
            self.choices: the available choices for the current path.
        """
        return self.choices


    def update_story(self, choice):
        """Updates the story based on the player's choice and 
            returns the next part. Returns None if there is no 
            next part.
        
        Args:
            choice (str):
                the story path the player selected.
        
        Returns:
            None: if there is no next choice.
            next_story: the next part of the story based on 
                the selected choice.
        """
        if not choice:
            return None

        if isinstance(choice, str):
            choice_id = choice.strip()
        next_story = self.choices.get(choice_id)
        
        return next_story

class Game(Player):
    """A class representing the game, inherits the Player class.
    
    Attributes:
        filepath (str): the path leading to a file containing 
            the story.
        name (str): the player's name.
        health (int): the amount of health points a player has.
    """
    def __init__(self, filepath, name, health):
        """Initializes a Game object.
        
        Args:
            filepath (str): the path leading to a file containing 
                the story.
            name (str): the player's name.
            health (int): the amount of health points a player has.
                
        Side Effects:
            Initializes name and health.
        """
        super().__init__(name, health)

        self.story_map = {}
        with open(filepath, "r") as f:
            data = json.load(f)
            for story_id, story_data in data.items():
                story_text = story_data.get("story_text")
                choices = story_data.get("Choice")
                self.story_map[story_id] = Story(story_id, story_text, choices)

    def play(self):
        """Displays the story and choices made as the game is played,
            story is updated based on the player's choices.
        
        Side Effects:
            Prints the current story, choices, a game over message, 
                and an invalid choice error.
        """
        current_story_id = "start"
        print(self.story_map.keys())
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
                    print(f"{choice_id}")
                choice = input("Enter your choice: ")
                    
                current_story_id = story.update_story(choice)
                if current_story_id:
                    break
                print("Invalid choice. Please try again") 
            

        
def main(filepath, name, health):
    """A function that runs the program. It allows users to enter
        their name, and reads a story file and the amount of health
        they have to create an instance of a Game object.
    
    Args:
        filepath (str): the path leading to a file containing 
            the story.
        name (str): the player's name.
        health (int): the amount of health points a player has.
    
    """
    name = input("Enter your name: ")
    game = Game(filepath, name, health)
    game.play()

if __name__ == "__main__":
    """This is executed when the script is run directly 
        (not imported as a module). It creates an argument 
        parser and defines the arguments, then calls the
        main() function.
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help="path to story file")
    parser.add_argument("--name", help="player name (default: Player)", default="Player")
    parser.add_argument("--health", help="player health (default: 100)", type=int, default=100)
    args = parser.parse_args()
    main(args.filepath, args.name, args.health)