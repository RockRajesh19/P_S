'''
Created on Nov 17, 2019

@author: rajesh
'''


class employee:
    
    _company = "Amazon"
    
    def printcompany(self):
        print(self._company)
        

obj = employee()

obj.printcompany()

print(employee._company)