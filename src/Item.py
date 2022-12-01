class Item:
    def __init__(self, itemID, itemName, itemPrice, itemType) -> None:
        self.itemID = itemID
        self.itemName = itemName
        self.itemPrice = itemPrice
        self.itemType = itemType
    
    def get_id(self):
        return self.itemID
    def get_name(self):
        return self.itemName
    def get_price(self):
        return self.itemPrice
    def get_type(self):
        return self.itemType

    def set_id(self, id):
        self.itemID = id
    
    def set_name(self, name):
        self.itemName = name
    
    def set_price(self, price):
        self.itemPrice = price

    def set_type(self, item_type):
        self.itemType = item_type
    
    def item_details(self):
        return self.__dict__