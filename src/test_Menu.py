from Menu import Menu_

def __init__(self):
        pass
    
def add_item(self, item):
        menu = Menu_()
        menu.add_item("naan")
        assert "naan"  in menu.get_item()

def delete_item(self, id):
        menu = Menu_()
        menu.delete_item(2)
        assert 2 not in menu.get_item()


    
