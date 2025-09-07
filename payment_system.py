from abc import ABC,abstractmethod

class payment_class(ABC):
    @abstractmethod
    def pay(self,ammount):
        pass 
    @abstractmethod
    def refund(self,ammount):
        pass
    
class CreditCard(payment_class):
    def pay(self,ammount):
        print(f"Paid {ammount} using CreditCard.")
    def refund(self,ammount):
        try :
            if ammount>0:
                print(f"Refund {ammount} using CreditCard.")
        except Expectations as e:
            print(e)
    
class PayPal(payment_class):
    def pay(self,ammount):
        print(f"Paid {ammount} using PayPal.")
    def refund(self,ammount):
        try :
            if ammount>0:
                print(f"Refund {ammount} using CreditCard.")
        except Expectations as e:
            print(e)
class Cash(payment_class):
    def pay(self,ammount):
        print(f"Paid {ammount} using CreditCard.")
    def refund(self,ammount):
        try  :
            if ammount>0:
                print(f"Refund {ammount} using CreditCard.")
        except Expectations as e:
            print(e)
list_of_class = [CreditCard(),PayPal(),Cash()]
for cls in list_of_class:
    cls.pay(1000)
    cls.refund(500)



