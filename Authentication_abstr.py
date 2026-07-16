from abc import ABC,abstractmethod
class Login(ABC):    
    @abstractmethod 
    def authenticate(self):
        pass

class GoogleLogin(Login):
    def authenticate(self):
        print(" Loggining with Google")

class Emaillogin(Login):
    def authenticate(self):
        print("Logginig with Email")

class Faceid(Login):
    def authenticate(self):
        print("Loggining with Face id")

g=GoogleLogin()
e=Emaillogin()
f=Faceid()

g.authenticate()

e.authenticate()

f.authenticate()

















