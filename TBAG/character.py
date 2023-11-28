
# Character class
class Character():

    # Constructor for Character class
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describes the character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Sets conversation for the character
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
# Enemy class
class Enemy(Character):

    # Constructor for Enemy Class
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.inventory = []
        self.morality = None
        self.alive = True

    # Sets weakness for the enemy
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    # Gets weakness for the enemy
    def get_weakness(self):
        return self.weakness
    
    # Sets inventory for the enemy
    def set_inventory(self, item):
        self.inventory = item

    # Gets inventory for the enemy
    def get_inventory(self):
        return str(self.inventory)
    
    # Removes inventory for the enemy
    def remove_inventory(self):
        self.inventory = None

    # Gets morality of the enemy
    def get_morality(self):
        return self.morrality
    
    # Gets awarness of the enemy
    def get_awarness(self):
        return self.alive

    # Fights enemy
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            return True
        else:
            print(self.name + " crishes you, puny adventurer")
            return False
     # Steals from enemy   
    def steal(self, property):
        if property == self.asset:
            print("You nicked " + property + " from " + self.name)
            return True
        else:
            print(self.name + " does not have that item on them or it has already been nicked")
            return False

    # Bribes enemy     
    def bribe(self):
        if self.morality != False:
            self.morality = False
            print(self.name + " has now been corrupted! What a shame!")

    # Kills enemy
    def kill(self):
        self.alive = False
        print(self.name + " is now dead")

# Friend class
class Friend(Character):

    # Constructor for friend class
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None

    # Sets gift for the enemy
    def set_gift(self,gift):
        self.gift = gift

    # Gets gift for the enemy
    def get_gift(self):
        return self.gift

        

    

