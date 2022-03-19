""" Game module """


class Room:
    """ Room class """

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.character = None
        self.item = None
        self.linked_rooms = {}

    def set_description(self, description):
        """ Set room description """
        self.description = description

    def link_room(self, room, direction):
        """ Link another room """
        self.linked_rooms[direction] = room

    def get_character(self):
        """ Get character of the room """
        return self.character

    def set_character(self, character):
        """ Set character of the room """
        self.character = character

    def get_item(self):
        """ Get item of the room """
        return self.item

    def set_item(self, item):
        """ Set item of the room """
        self.item = item

    def get_details(self):
        """ Print details """
        print(self.name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is {direction}")

    def move(self, command):
        """ Move to another room """
        return self.linked_rooms.get(command, self)


class Enemy:
    """ Enemy class """
    defeated = 0

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def set_description(self, description):
        """ Set enemy description """
        self.description = description

    def set_conversation(self, conversation):
        """ Set enemy conversation """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """ Set enemy weakness """
        self.weakness = weakness

    def describe(self):
        """ Print enemy description """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """ Enemy talks """
        print(f"[{self.name} says]: {self.conversation}")

    def fight(self, fight_with):
        """ Fight with enemy """
        if fight_with == self.weakness:
            Enemy.defeated += 1
            print(f'You fend {self.name} off with the {fight_with}')
            return True

        print(f'{self.name} crushes you, puny adventurer!')
        return False

    @classmethod
    def get_defeated(cls):
        """ Get number of defeated enemies """
        return Enemy.defeated


class Item:
    """ Item class """

    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def set_description(self, description):
        """ Set item description """
        self.description = description

    def get_name(self):
        """ Get item name """
        return self.name

    def describe(self):
        """ Print item description """
        print(f"The [{self.name}] is here - {self.description}")
