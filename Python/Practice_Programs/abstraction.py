'''
Created on Nov 17, 2019

@author: rajesh
'''
from abc import abstractmethod,ABC


class A(ABC):
    
    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def display2(self):
        pass
    
    def name(self):
        print("rajesh")
        
class B(A):
    
    def display(self):
        print("print display")
        
    def display2(self):
        print("print display2")

obj = B()

obj.display()
obj.display2()
obj.name()