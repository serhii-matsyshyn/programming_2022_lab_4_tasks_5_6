""" Game module """


class Street:
    """ Street class """

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.character = None
        self.item = None
        self.linked_streets = {}

    def set_description(self, description):
        """ Set street description """
        self.description = description

    def link_street(self, street, direction):
        """ Link another street """
        self.linked_streets[direction] = street

    def get_character(self):
        """ Get character of the street """
        return self.character

    def set_character(self, character):
        """ Set character of the street """
        self.character = character

    def get_item(self):
        """ Get item of the street """
        return self.item

    def set_item(self, item):
        """ Set item of the street """
        self.item = item

    def get_details(self):
        """ Print details """
        print(self.name)
        print("--------------------")
        if self.description:
            print(self.description)
        for direction, street in self.linked_streets.items():
            print(f"The {street.name} is {direction}")

    def move(self, previous_street, command):
        """ Move to another street """
        if ((self.character is None) or
                (self.linked_streets.get(command).name == previous_street.name)):
            return self.linked_streets.get(command, self)

        print('You should pass characters first to pass the street!')
        return self


class Character:
    """ Character class """

    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.conversation = None

    def set_description(self, description):
        """ Set character description """
        self.description = description

    def set_conversation(self, conversation):
        """ Set character conversation """
        self.conversation = conversation

    def describe(self):
        """ Print character description """
        print(f"{self.name} is here! - {self.description}")

    def talk(self):
        """ Character talks """
        print(f"[{self.name} says]: {self.conversation}")


class Enemy(Character):
    """ Enemy class """

    def __init__(self, name, description=""):
        name = f"Enemy {name}"
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, weakness):
        """ Set enemy weakness """
        self.weakness = weakness

    def fight(self, fight_with):
        """ Fight with enemy """
        if fight_with == self.weakness:
            print(f'You fend {self.name} off with the {fight_with}')
            return True

        print(f'{self.name} crushes you, puny adventurer! \
You cannot fend {self.name} off with the {fight_with}')
        return False


class Friend(Character):
    """ Friend Character class """
    def __init__(self, name, description="Your friend."):
        name = f"Friend {name}"
        super().__init__(name, description)

        self.advice = None
        self.conversation = "I can give you advice!"

    def set_advice(self, advice):
        """ Set friend advice """
        self.advice = advice

    def talk(self):
        """ Character talks """
        print(f"[{self.name} says]: {self.conversation}")
        print(f"[{self.name} says]: The advice is {self.advice}")


class SuperEnemy(Enemy):
    """ Super Enemy class """
    def __init__(self, name, description=""):
        super().__init__(name, description)

        self.name = f"Super Enemy {name}"
        self.question = ""
        self.passphrase = ""

    def set_passphrase(self, question, passphrase):
        """ Set enemy passphrase """
        self.question = question
        self.passphrase = passphrase

    def fight(self, fight_with):
        """ Fight with Super Enemy """
        print("That's not easy to fight me!")
        print(f"Answer a question: {self.question}")
        answer = input("> ")
        if self.passphrase == answer:
            print("Correct! You can continue the fight!")
            return super().fight(fight_with)

        print(f'{self.name} crushes you, puny adventurer!')
        return False


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


class WeaponItem(Item):
    """ Weapon Item class """
    def describe(self):
        """ Print weapon item description """
        print(f"The weapon item [{self.name}] is here - {self.description}")


class FoodItem(Item):
    """ Food Item class """
    def describe(self):
        """ Print weapon item description """
        print(f"The food item [{self.name}] is here - {self.description}")
