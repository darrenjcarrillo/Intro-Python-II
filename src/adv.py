from room import Room
from player import Player
from item import Item

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Rescue the princess and exit to the south."""),
}


# Link rooms together

room['outside'].way['North'] = room['foyer']
room['foyer'].way['South'] = room['outside']
room['foyer'].way['North'] = room['overlook']
room['foyer'].way['East'] = room['narrow']
room['overlook'].way['South'] = room['foyer']
room['narrow'].way['West'] = room['foyer']
room['narrow'].way['North'] = room['treasure']
room['treasure'].way['South'] = room['narrow']

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

###### PLAYER NAME #####
playerName = input(f'What is your name valiant Knight? ')

player = Player(playerName, room["outside"])

direction = f'Where should we go sir {playerName}? '

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



location = input(f'{player.current_room}\n\n{direction}')


# player_inventory = [x.name for in player.inventory] if len(player.inventory) else "Storage Empty"


# pickItem = input(f'{room.item}')

while location != 'q':
    try:
        player.current_room = player.current_room.way[location.capitalize()]
        location = input(
            f'{player.current_room}\n\n{direction}')

        if location == "pick":
            item_name = [i.name for i in player.current_room.item]
            item_index = item_name.index(item)
            player.pick(player.current_room.item[item_index])
            player.current_room.remove_item(item_index)

        elif location == "drop":
            item_name = [i.name for i in player.current_room.item]
            item_index = item_name.index(item)
            player.current_room.add_item(player.inventory[item_index])
            player.drop(item_index)

    except KeyError:
        location = input(f'You can\'t go there .\n\n{direction}')
