# Appliance Interface
#
# Create an abstract class Appliance with methods turn_on() and turn_off().
# Implement Fan and AirConditioner classes and define their behaviors.

from abc import ABC,abstractmethod
class Appliance(ABC):
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class Fan(Appliance):
    def turn_on(self,on):
        if Fan.