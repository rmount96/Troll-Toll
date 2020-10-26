
class Unit:
    def __init__(self, name, position, health =10, attack_power =2):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.position = position #{"x":1, "y":1} [1,1]
    
    def get_hit(self, power):
        #print("The creature attacks you for %s HP" %  power)
        self.health = self.health - power
    
    def attack(self, enemy):
        enemy.get_hit(self.attack_power)

    def move(self, dir):
        if dir == "up":
            self.position = [self.position[0], self.position[1]-1]
        elif dir == "down":
            self.position = [self.position[0], self.position[1]+1]
        elif dir == "left":
            self.position = [self.position[0]-1, self.position[1]]
        elif dir == "right":
            self.position = [self.position[0]+1, self.position[1]]

class Player(Unit):
    def __init__(self, name, position, health =10, attack_power =2):
        super().__init__(name, position, 15, 5)
        self.inventory = []

    def __str__(self):
        inv = ""
        for ivt in self.inventory:
            inv += " "+ivt.name
        return """
        ***************
        Health: %s
        Position: %s
        Inventory: %s
        ***************""" % (self.health, self.position, inv)

    def get_hit(self, power):
        print("The creature attacks you for %s HP" %  power)
        self.health = self.health - power

    def attack(self, enemy):
        print("You attack the %s for %s power" % (enemy.name, self.attack_power))
        enemy.get_hit(self.attack_power)

    def pickup_item(self, item):
        self.inventory.append(item)
        item.get_picked_up(self)

    def troll_encounter(self, enemy):
        print("You are able to attack twice before he rises!")
        self.attack(enemy)
        self.attack(enemy)
        print("UH-OH! He looks angry!")

class Troll(Unit):
    def __init__(self, name, position, health =10, attack_power =2):
        super().__init__("Troll", [6,3], 15, 7)
    
    def smash(self, enemy):
        print("I WILL CRUSH YOU!")
        super().attack(enemy)
        print("...and sends you flying back to the entrance")
        enemy.position = [5,5]
        #super().get_hit(enemy.attack_power)
    
    # def troll_encounter(self, enemy):
    #     print("You are able to attack twice before he rises!")
    #     player.attack(enemy)
    #     player.attack(enemy)
    #     super().attack(Player)
    #     print("UH-OH!")
        