"""
Create Bike Rental Class and initialize stock attribute
"""

import datetime as dt
class BikeRental:
    
    def __init__(self,stock=0):
        """Intailzer for bike Rental Class"""
        self.stock = stock
        
    def display_stock(self):
        """ Displays the bikes currently available for rent in the system"""
        print(f"We have currently {self.stock} bikes available in the System")
        return self.stock
    
    def rent_bike_on_hourly_basis(self,n):
        """Rent bike on Hourly Basis"""
        if n <=0:
            print("Invalid Selection")
            return None
        elif n > self.stock:   
            print(f"We have only {self.stock} bikes availabel with us")
            return None
        else:
            now = dt.datetime.now()
            print(f"You have Selected {n} bikes for hourly basis today at {now.hour}:{now.minute}:{now.second}")
            print("You will be charged $5 for each bike per hour")
            self.stock -= n
            return (now)
    
    


rental_bike = BikeRental(50)
rental_bike.rent_bike_on_hourly_basis(5)
rental_bike.display_stock()



