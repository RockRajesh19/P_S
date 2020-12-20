'''
Created on Oct 14, 2019

@author: rajesh
'''


def prime_numbers_count(x , y):
    count = 0
    for num in range(x , y + 1):
        if num > 1:
            for z in range(2, num):
                if (num % z) == 0:
                    break
            else:
                count += 1
                print(num, end = " ")
    print(count)
                
prime_numbers_count(1, 100)