from Effects import Effect
class Item:
    def __init__(self,name,value,effect,quantity):
        self.name=name
        self.value=value
        self.effect=effect  #Effect is its own class
        self.quantity=quantity

