import abc
from abc import ABCMeta

class Vehicle(object):
    __metaclass__=ABCMeta

    @abc.abstractmethod
    def who_are_you(self):
        print "I am a vehicle and also an abstract method"

class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)

    def who_are_you(self):
        super(Car,self).who_are_you()
        print "I'm a car"

car = Car()
car.who_are_you()


"""
http://www.3engine.net/wp/2015/02/clases-abstractas-en-python/
"""
