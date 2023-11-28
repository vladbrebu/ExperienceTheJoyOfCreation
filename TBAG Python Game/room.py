# Room class
class Room():
    # constructor for Room class
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None

    # gets description of room
    def get_description(self):
        return self.description
    
    # sets description of room
    def set_description(self, room_description):
        self.description = room_description

    # sets name of the room
    def set_name(self, room_name):
        self.name = room_name
    
    # gets name of the room
    def get_name(self):
        return self.name
    
    # sets a character in the room
    def set_character(self, new_character):
        self.character = new_character

    # returns the character in the room
    def get_character(self):
        return self.character
    
    # removes character from the room
    def remove_character(self):
        self.character = None
    
    # links room to other rooms
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    # prints description of the roo
    def get_details(self):
        print(self.name)
        print("--------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    # moves from one room to another
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self