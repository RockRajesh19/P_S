'''
Created on Nov 13, 2019

@author: rajesh
'''

class computer:
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print('config is',self.cpu, self.ram)

c = computer("i5", 16)
c1 = computer("rezen", 8)


c.config()
c1.config()