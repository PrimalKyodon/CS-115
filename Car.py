####################################################################
#   Aaren Patel
#   I pledge my honor that I have abided by the Stevens Honor System
#   12/13/22
#   CS 115 - Lab 12
####################################################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    """Car class to create a car object"""
    def __init__(self, make, model, mpg, tank_capacity):
        """Initializes the car object with the values make, model, mpg, and tank_capacity"""
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity

    def get_make(self):
        """Getter for the make of the car object"""
        return self.__make

    def get_model(self):
        """Getter for the model of the car object"""
        return self.__model

    def get_mpg(self):
        """Getter for the mpg of the car object"""
        return self.__mpg

    def get_tank_capacity(self):
        """Getter for the tank_capacity of the car object"""
        return self.__tank_capacity

    def set_make(self, make):
        """Setter for the make of the car object"""
        self.__make = make

    def set_model(self, model):
        """Setter for the model of the car object"""
        self.__model = model

    def set_mpg(self, mpg):
        """Setter for the mpg of the car object"""
        self.__mpg = mpg

    def set_tank_capacity(self, tank_capacity):
        """Setter for the tank_capacity of the car object"""
        self.__tank_capacity = tank_capacity

    def get_total_range(self):
        """Returns the total range that the car can drive on a full tank"""
        return self.__mpg * self.__tank_capacity
        
    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):
    """Class for a Hybrid Car object that inherits from the Car class"""
    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        """Initializes a hybrid car object with the values from car, battery_kWh, and miles_per_kWh"""
        super().__init__(make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

    def get_battery_range(self):
        """Returns the total distance the car can travel on a fully charged battery."""
        return self.__battery_kWh * self.__miles_per_kWh

    def get_total_range(self):
        """Returns the total distance the car can travel on a full gas tank and battery"""
        return super().get_total_range() + self.get_battery_range()
    
    def __str__(self):
        """A string for printing information about a car."""
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
