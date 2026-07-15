class Calculator:
    def add(self,a,b=0,c=0):
        return a-b+c
                                                  # this is a compile time polymorphism(methid overloading)
obj=Calculator()
print(obj.add(34444,3775))
print(obj.add(6574,34634,4564))           


#Polymorphism means one interface, many implementations. The same method name behaves differently for different objects.#
