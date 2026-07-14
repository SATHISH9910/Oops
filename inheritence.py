class Emoloyee():
    def working(self):
        print("Emoloyee is working")
    
class Developer(Emoloyee):
    def coding(self):
        print("developer is coding")

class Tester(Emoloyee):
    def testing(self):
        print("Tester is testing")

e=Emoloyee()
e.working()

d=Developer()
d.coding()
d.working()

t=Tester()
t.testing()
t.working()
