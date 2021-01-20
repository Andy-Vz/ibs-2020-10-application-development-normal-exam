class Aquarium():
    def __init__(self):
        self.fishList = []
    def addFish(self,Fish):
        self.fishList.append(Fish)
    def removeFish(self,Fish):
        self.fishList.remove(Fish)
    def getStatus(self):
        for fish in self.fishList:
            print(fish)

class Fish:
    def __init__(self,name,weight,color, feedrate):
        self.name = name
        self.weight = weight
        self.color = color
        self.feedrate = feedrate
    def status(self):
        aditionalProp = ""
        try :
            self.stmLoss
            aditionalProp = ", short-term memory loss: true"
        except:pass
        try:
            aditionalProp = ", additional color : " + self.additionalColor
        except:pass
        #Print the formated properties
        print(self.name,", weight: ", self.weight, ", color: " ,self.color, aditionalProp)

    def feed(self):
        # Increse wight based on the fish feedrate
        self.weight += self.feedrate

#Class inheriting from the Fish parent class
class Clownfish(Fish):
    def __init__(self, name, weight, color, feedRate, additionalColor):
        super().__init__(name, weight, color, feedRate)
        self.additionalColor = additionalColor

class Tang(Fish):
    def __init__(self, name, weight, color, feedRate, stmLoss):
        super().__init__(name, weight, color, feedRate)
        self.stmLoss = stmLoss

class Kong(Fish):
    def __init__(self, name, weight, color, feedRate):
        super().__init__(name, weight, color, feedRate)


clownFish = Clownfish("Bobby",20,"red", 1, "red")
tang = Tang("Tongy",10,"green", 1, True)
kong = Kong("Kongy",15,"red", 2)

aquarium = Aquarium()
aquarium.addFish(clownFish)
aquarium.addFish(tang)
# aquarium.feed() # Feeds all fish
aquarium.removeFish(clownFish)
aquarium.getStatus() # Prints status of all fishes


tang.feed()
tang.status()