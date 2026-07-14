class Emoloyee():
    def working(self):
        print("Emoloyee is working")                # in oops inheritence is where one class gets properties and methods of another class
    
class Developer(Emoloyee):                       #child >- parent 
                                                                                          
                                                             # employee is parent class
                                                #developer,tester is child class
    def coding(self):
        print("developer is coding")                                                    # this enables code reusability 
                                                  # dev,test inherits() working( method) from employee
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
