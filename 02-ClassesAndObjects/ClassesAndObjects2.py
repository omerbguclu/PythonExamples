import random

class Humanbeing:
    arm =2
    leg =2
    live=1

    def limbs(self):
        if(self.live!=0):
            print(self.arm, "arms",self.leg,"legs")
        else:
            print("Patient is dead now We are sorry")
    def carAccident(self):
        print("There was an accident. You are at hospital now")
        possibilities = random.randrange(0, 3)
        if(possibilities==0):
            self.arm-=1
            print("You lose a arm. We are sorry")
        elif(possibilities==1):
            self.leg-=1
            print("You lose a leg. We are sorry")
        else:
            self.live=0
            print("We lost the patient. We are sorry")

ahmet=Humanbeing()

ahmet.limbs()
ahmet.carAccident()
ahmet.limbs()
