""" Main game module """

import game

kozelnytska = game.Street("Kozelnytska street")
krakivska = game.Street("Krakivska street")
zelena = game.Street("Zelena street")
ivana_franka = game.Street("Ivana Franka street")
stryiska = game.Street("Stryiska street")
shevchenka_avenue = game.Street("Shevchenka Avenue")
ring_road = game.Street("Ring road")

kozelnytska.link_street(stryiska, "west")

stryiska.link_street(ivana_franka, "north")
stryiska.link_street(kozelnytska, "east")
stryiska.link_street(ring_road, "south")

ivana_franka.link_street(shevchenka_avenue, "north")
ivana_franka.link_street(stryiska, "south")

ring_road.link_street(stryiska, "west")
ring_road.link_street(zelena, "east")

zelena.link_street(krakivska, "north")
zelena.link_street(ring_road, "west")

shevchenka_avenue.link_street(krakivska, "north")
shevchenka_avenue.link_street(ivana_franka, "south")

krakivska.link_street(shevchenka_avenue, "south")

student = game.Friend("Student")
student.set_advice("you should know more to pass SuperBoss!")
kozelnytska.set_character(student)

lotr = game.Enemy("Lotr", "Rogue, robber. Facet")
lotr.set_conversation("You won't pass if I am alive!")
lotr.set_weakness("gun")
stryiska.set_character(lotr)

zbuj = game.Enemy("Zbuj", "Robber standing next to a pile of some goods.")
zbuj.set_conversation("I need a bag to put all that inside. Do you have one?")
zbuj.set_weakness("bag")
ivana_franka.set_character(zbuj)

batyar = game.SuperEnemy("Batyar", "The man clings to all passers-by.")
batyar.set_conversation("I bein' wise man, yo' man must to pass ma' test man \
and give me more knowledge man")
batyar.set_passphrase("What country ma' university UCU located??", "Ukraine")
batyar.set_weakness("book")
ring_road.set_character(batyar)

cavalier = game.Enemy("Cavalier", "Fat cavalier waiting for something.")
cavalier.set_conversation("I am so hungry! \
You can fight me only with a use of huge portion of secret dish!")
cavalier.set_weakness("borscht")
zelena.set_character(cavalier)

robot = game.Friend("Robot")
robot.set_advice("Great! Find the way back and you will win!")
krakivska.set_character(robot)

lajdak = game.Enemy("Lajdak", "Lajdak is so lazy that only whispers a bit.")
lajdak.set_conversation("I need money")
lajdak.set_weakness("money")
shevchenka_avenue.set_character(lajdak)

borscht = game.FoodItem("borscht")
borscht.set_description("Borscht from Trapesna")
kozelnytska.set_item(borscht)

gun = game.WeaponItem("gun")
gun.set_description("A really good gun to protect yourself.")
stryiska.set_item(gun)

bag = game.Item("bag")
bag.set_description("Empty bag.")
ring_road.set_item(bag)

book = game.Item("book")
book.set_description("Great book.")
ivana_franka.set_item(book)

money = game.Item("money")
money.set_description("Some coins on the floor.")
krakivska.set_item(money)

current_street = kozelnytska
previous_street = current_street
backpack = []

final_street_passed = False

dead = False

while not dead:

    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_street_2 = current_street.move(previous_street, command)
        if current_street_2 != current_street:
            previous_street = current_street
            current_street = current_street_2

        if current_street.name == 'Krakivska street':
            final_street_passed = True
        if final_street_passed:
            if current_street.name == 'Stryiska street':
                print("Congratulations, you have won the game!")
                dead = True

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            if isinstance(inhabitant, game.Friend):
                current_street.character = None

    elif command == "fight":
        if (inhabitant is not None) and isinstance(inhabitant, (game.Enemy, game.SuperEnemy)):
            # Fight with the inhabitant, if there is one
            print(f"What will you fight with? You have {backpack}")
            fight_with = input("> ")

            # Do I have this item?
            if fight_with in backpack:
                backpack.remove(fight_with)

                if inhabitant.fight(fight_with):
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_street.character = None

                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
