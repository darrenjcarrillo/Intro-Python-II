# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.way = {}
        # self.n_to = None
        # self.s_to = None
        # self.e_to = None
        # self.w_to = None

    def __str__(self):
        return (f'\nYou are currently at --> {self.name} sir.\n\nYou Found a ###THIS WILL BE AN ITEM##\n\nClue: {self.description}\n\nPlease choose which way to go --> ' + ', '.join(list(self.way.keys())))
        # return f"Room: {self.room_name}, Description: {self.room_description}"

    def remove_item(self, item):
        del self.item[item]

    def add_item(self, item):
        self.item.append(item)
