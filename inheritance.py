class Bird:
    def __init__(self):
        print("bird is ready")

    def Thisisbird(self):
        print("bird")


    def Swim (self):
        print("swim faster")
class Penguin(Bird):
    def __init__(self):
        print ("Pnguin is ready")

    def Thisisbird(self):
        print("Penguin")
    def run(self):
        print("runFaster")


peggy = Penguin()
peggy.Thisisbird()
peggy.Swim()
peggy.run()