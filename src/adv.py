from tkinter import Tk

rooms = {
    "outside": {
        "name": "Outside Cave Entrance",
        "description": "North of you, the cave mouth beckons.",
        "n_to": "foyer",
    },

    "foyer": {
        "name": "Foyer",
        "description": "Dim light filters in from the south. Dusty passages run north and east.",
        "n_to": "overlook",
        "s_to": "outside",
        "e_to": "narrow",
    },

    "overlook": {
        "name": "Grand Overlook",
        "description": """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
        "s_to": "foyer",
    },

    "narrow": {
        "name": "Narrow Passage",
        "description": "The narrow passage bends here from west to north. The smell of gold permeates the air.",
        "w_to": "foyer",
        "n_to": "treasure",
    },

    "treasure": {
        "name": "Treasure Chamber",
        "description": """You've found the long-lost treasure
chamber. Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
        "s_to": "narrow",
    },

}

class TextUtilities:
    def print_title(self, title):
        title_sep = ''.center(len(title), '-')
        print('\n{}\n{}'.format(title, title_sep))

    def print_description(self, description):
        print('{}\n'.format(description))
    
    def print_error(self, message):
        message_wrapper = ''.center(len(message) + 4, '!')
        print('\n{1}\n! {0} !\n{1}'.format(message, message_wrapper))

    def print_list_of_dicts(self, list):
        for item in list:
            for key, val in item.items():
                print('[{}] {}'.format(key, val))

class GameObject:
    def __init__(self, play):
        self.play = play
        self.Text = TextUtilities()
    
    def quit_game(self):
        self.play = False
        print("\nGoodbye")


class Player(GameObject):
    def __init__(self, location, play):
        super().__init__(play)
        self.location = location
        self.command = ''
        self.commands = {
            "n": self.move,
            "s": self.move,
            "e": self.move,
            "w": self.move,
            "q": self.quit_game,
            "g": self.get_available_directions
        }
    
    def get_command(self):
        self.command = input("\nWhat do you want to do? ")
        self.process_command()
    
    def process_command(self):
        try:
            self.commands[self.command]()
        except KeyError:
            self.Text.print_error("Not sure what you mean")
    
    def get_available_directions(self):
        available_directions = []
        for attr in rooms[self.location]:
            if attr.endswith("_to"):
                direction = attr.replace("_to", "")
                room = rooms[self.location][attr]
                available_directions.append({direction:room})
        return available_directions
    
    def look(self):
        self.Text.print_title(rooms[self.location]["name"])
        self.Text.print_description(rooms[self.location]["description"])
        self.Text.print_title("Available Directions")
        self.Text.print_list_of_dicts(self.get_available_directions())

    def move(self):
        direction = self.command + '_to'
        try:
            self.location = rooms[self.location][direction]
        except KeyError:
            self.Text.print_error("Whoops, that's not a valid direction")


def game_loop():
    player = Player("outside", True)
    print("\n\n*** And so our story begins... ***\n\n")
    while player.play:
        player.look()
        player.get_command()


game_loop()
