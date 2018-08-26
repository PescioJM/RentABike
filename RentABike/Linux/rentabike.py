
# -*- coding: utf-8 -*-
#!/usr/bin/env python

# metadata:
__author__ = "Juan Manuel Pescio"
__email__ = "juanmp012@gmail.com"

import time

class Client:

    def __init__(self):
        self.first_name = raw_input("Please, enter your first name: ")
        self.last_name =  raw_input("Enter your last name: ")
        self.contact = input("Enter your phone number: ")
        self.address = raw_input("Enter your address: ")
        self.zip = input("Enter your ZIP Code: ")

        print ("******************************************************\
                \n***%s %s, it has been successfully registered ***\
                \n******************************************************"\
                %(self.first_name,self.last_name))

    def __str__(self):
        return (self.first_name,self.last_name,self.contact,self.address,\
            self.zip,self.credit)

class Rent:

    def __init__(self):
        self.bikes = input("How many bicycles do you want to rent ?   ")
        self.mod = str(input("Please, enter: \n \t '1' if you want to rent per\
 hour \n \t '2' if you want to rent per day \n \t '3' if you want to rent per week  "))

    def rent_cost (self):
        type = {'1':5, '2':20, '3':60}
        time_r = input("Enter the amount of time (In hours, days or weeks as\
appropriate):  ")
        var = True
        if (self.bikes >= 3 and self.bikes <= 5):
            var = input("If you want a family promotion enter 0, \
otherwise enter any other key:  ")
        if var == False:
        	print ("Cost of rent: USD %s \n \n *** See you soon,\
 Rent a Bike wishes you luck! ***"\
            %((self.bikes*type[self.mod]*time_r)*0.7))
        else:
            print ("Cost of rent: USD %s \n \n *** See you soon,\
 Rent a Bike wishes you luck! ***"\
            %(self.bikes*type[self.mod]*time_r))
        time.sleep(3)

def main():
    client1 = Client()
    rent1 = Rent()
    rent1.rent_cost()

if __name__ == '__main__':
    main()
