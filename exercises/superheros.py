# Write your solutions for 1.5 here!
class Superheros:
    def __init__(self,name,superpower,strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength

    def print(self):
        print(self.name)
        print(self.strength)

    def save_civilian(self,work):
        if(work < self.strength):
             self.strength = self.strength - work
        else:
            print("Superhero is not strong enough")

Superheros_1 = Superheros("xx","fly",1000)

Superheros_1.print()
Superheros_1.save_civilian(100000)
Superheros_1.print()  

    

