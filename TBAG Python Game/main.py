from room import Room
from character import Enemy
from character import Character
from character import Friend
from item import Item

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dining_hall.set_character(dave)
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dave.set_inventory("laptop")
print(dave.get_inventory())

stevie = Friend("Stevie", "A blind zombie")
ballroom.set_character(stevie)
stevie.set_conversation("Where are you?")

key = Item("key1","blue")
print(key)


current_room = kitchen

while True:     
    print("\n")         
    current_room.get_details()  

    inhabitant = current_room.get_character()
    if inhabitant is not None:              
        inhabitant.describe()

    command = input("> ")    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()
        else:
            print("There is no one here")

    elif command == "fight":
        if inhabitant is not None:
            command = input("What is your weapon?: ")
            if inhabitant.fight(command) == False:
                print("You lost the fight! Adios!")
                break
            elif inhabitant.fight(command) == True:
                inhabitant.kill()
                current_room.remove_character()
        else:
            print("There is no one here")

    elif command == "steal":
        if inhabitant is not None:
            command = input("What are you looking to steal?: ")
            inhabitant.steal(command)
            inhabitant.remove_property()
        else:
            print("There is no one here")

    elif command == "bribe":
            inhabitant.bribe()

    elif command == "gift":
        if inhabitant.get_gift() is None:
            command = input("What is your gift?: ")
            inhabitant.set_gift(command)
            print(inhabitant.get_gift())