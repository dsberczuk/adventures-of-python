class Effect:
    #H# __init__(): initiates the effect
    #I# self allows the class to reference it's current iteration
    ### modify is a string value that represents the statistics that are being modified
    #P# Value is the specific value becing modified 
    #E# 
    #R# The amount is how much the value is being changed by
    #S# This class is meant to be used on items
    #O# 
    #N# 
    
    from Targets import Characters
    def __init__(self,target,modify,amount):
        self.target=target
        self.modify=modify
        self.amount=amount
    def process(self, target):
        if self.modify == "gold":
            if target.gold:
                if target.gold <= 0:
                    target.gold += self.amount
