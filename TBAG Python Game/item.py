# Item class
class Item():
    # constructor for Item class
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    # gets name of the item
    def get_name(self):
        return self.name
    
    # sets name of the item
    def set_name(self, item_name):
        self.name = item_name
    
    # gets description of the item
    def get_description(self):
        return self.description
    
    # sets description of the item
    def set_description(self, item_description):
        self.description = item_description
