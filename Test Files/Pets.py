#Testing classes
class Pet:
    def __init__(self, name, type):
        self.name=name
        self.type=type
    def speak(self):
        if self.type=="Cat":
            return "Meow"
        if self.type=="Human":
            return "Don't poke me"

Pixel=Pet("Pixel","Cat")
Monty =Pet("Monty","Cat")
Daniel=Pet("Daniel","Human")
List = [Pixel,Monty,Daniel]
for i in List:
    print(i.name)
    print(i.type)
    print(i.speak())