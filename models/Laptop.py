class Laptop:

    def __init__(self, speed, manufacturerName, ramVolume):
        self.speed = speed
        self.manufacturerName = manufacturerName
        self.ramVolume = ramVolume

    def show(self):
        print(self.manufacturerName + " \t " + str(self.speed) + " \t " + str(self.ramVolume))

