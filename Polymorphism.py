#polymorphism >- poly means many ,morphism means form >> many forms  , so it is the ability of a sigle method or function to perform Maany actions
class Electronics:
    def work(self):                                    
        print(" Electronics Uses elctricity to run")
        print(f"-------------------------")              #  depeding on the object or data it works with
class Car:
    def work(self):
        print("Cars  can go by Fuel&electricity")
        print(f"-------------------------")                        
class Generator:
    def work(self):
        print("Generator consumes fuel & produce electricity")
        print(f"-------------------------")
class Battery:
    def work(self):
        print("Battery Uses electricity to charge Itself")
        print(f"-------------------------")
class Humans:
    def work(self):
        print("Humans are Utilizing all above listed")
        print(f"--------------------------")



devices = [Electronics(), Car(),Generator(),Battery(),Humans()]
for devices in devices:
    devices.work()


       ''' Runtime polymorphism happens when a child class overrides a method of its parent class. '''