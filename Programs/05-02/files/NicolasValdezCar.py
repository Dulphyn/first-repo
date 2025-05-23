# Programming Exercise 9-1

class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model;
        self.__make = make
        self.__speed = speed
    
    def set_year_model(self, year_model):
        self.__year_model = year_model
    
    def set_make(self, make):
        self.__make = make
    
    def set_speed(self, speed):
        self.__speed = speed
    
    def get_year_model(self):
        return self.__year_model
    
    def get_make(self):
        return self.__make
    
    def get_speed(self):
        return self.__speed

    def accelerate(self):
        accel=5
        self.__speed += accel
        return self.__speed
    
    def brake(self):
        brake=5
        self.__speed -= brake