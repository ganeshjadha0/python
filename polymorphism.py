class parrot:

    def fly (self):
        print("parrot can fly")
    def swim(self):
        print("parrot can swim")


class Penguin:
    def fly (self):
        print("parrot can't fly")
    def swim(self):
        print("parrot can't swim")

def Flying_test(bird):
     bird.fly()

blu=parrot()
pegg=Penguin()


Flying_test(blu)
Flying_test(pegg)