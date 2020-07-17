# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.way = {}

    def __str__(self):
        return (f'\nYou are currently --> {self.name} sir.\n\n{self.description}\n\n')
