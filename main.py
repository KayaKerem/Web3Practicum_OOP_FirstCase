from datetime import date
class Vehicle:
    def __init__(self,hgsNumber,name,date,balance):
       self.hgsNumber=hgsNumber
       self.name=name
       self.date=date
       self.balance=balance
       
       
class Car(Vehicle):
    fee = 15
    def __init__(self, hgsNumber, name, date, balance):
        super().__init__(hgsNumber, name, date, balance)

class Bus(Vehicle):
    fee = 25
    def __init__(self, hgsNumber, name, date, balance):
        super().__init__(hgsNumber, name, date, balance)

class Minibus(Vehicle):
    fee=20
    def __init__(self, hgsNumber, name, date, balance):
        super().__init__(hgsNumber, name, date, balance)

class Gise:
    listOfCars= list()
    def __init__(self):
        pass

    def getPay(self,vehicle):
        vehicle.balance -= vehicle.fee
        if vehicle.balance >= 0:
            self.listOfCars.append(vehicle)
            vehicle.balance -=vehicle.fee
            print("Successfull => Your payment has been received")
        else:
            print("Failed => Insufficient balance")
            vehicle.balance += vehicle.fee

    def getTotalIncome(self,date=date.today()):
        total=0
        for i in self.listOfCars:
            if(i.date == date):
                total = total+i.fee
        print("Total income of "+str(date) +": "+str(total))

