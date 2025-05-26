"""

This project was my first time working with classes, inheritance, and abstract methods in Python.
I designed a small object-oriented system for a fictional "Cozy Cafe" where customers can place
orders for different beverages like coffee, tea, and matcha.

Each beverage is a subclass of an abstract base class called `beverage`, which defines a common
structure and interface. This helped me learn how child classes inherit attributes and methods
from a parent class while also allowing them to override specific behaviors (like `get_description()`).

I also created a customer system with two types of customers: regular and loyalty members.
Both inherit from the abstract `customer` class, but loyalty customers receive a discount when
their total cost is calculated. This part of the project helped me understand polymorphism and 
how different objects can implement the same method in their own unique ways.

Through this project, I got more comfortable with concepts like object composition (customers having a list
of beverage orders), and how to organize real-world scenarios using classes in Python.

prompt I used:

In the Cozy Cafe, the menu features various types of beverages: coffee, tea, and matcha. Each
beverage is customized by its name, size, and price. The cafe serves a diverse clientele (regular
customer, loyalty customer), where each customer can order multiple beverages. Loyalty program
members, receive a discount on their total bill. After placing an order, the total cost is calculated,
including any discounts, and a receipt is printed detailing the list of beverages, their sizes, prices, and
the final total cost.

"""
from abc import ABC, abstractmethod

#parent class
class beverage(ABC):
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    @abstractmethod
    def get_discription(self):
        pass

class coffee(beverage): #child class
    def __init__(self, size, price):
        super().__init__("Coffee", size, price)

    #overriding get_description
    def get_discription(self):
        return f"{self.size} {self.name} : ${self.price}"
    

class tea(beverage): #child class
    def __init__(self, size, price):
        super().__init__("Tea", size, price)

    #overriding get_description
    def get_discription(self): 
        return f"{self.size} {self.name} : ${self.price}"
    
class matcha(beverage): #child class
    def __init__(self, size, price): 
        super().__init__("Matcha", size, price)

    #overriding get_description
    def get_discription(self):
        return f"{self.size} {self.name} : ${self.price}"


#Parent customer
class customer(ABC):
    def __init__(self, name):
        self.name = name 
        #have to use collection for being able to order multiple orders (aka list)
        self.orders =[]
    
    #function to add to list
    def add_order(self,beverage):
        self.orders.append(beverage)

    #total cost function as a loop
    def total_cost(self):
        sum = 0
        for beverage in self.orders:
            sum += beverage.price
        return sum 
    
    #print name and orders
    def print_receipt(self):
        print(f"Receipt for {self.name}: ")
        for beverage in self.orders:
            print(beverage.get_discription())
        print(f"Total: ${self.calculate_final_cost()}")

    @abstractmethod
    def calculate_final_cost(self):
        pass


#Regular and loyalty customer 

class regular_customer(customer):
    def calculate_final_cost(self):
        return self.total_cost()
    
class loyalty_customer(customer):
    def __init__(self, name, discount):
        super().__init__(name)
        self.discount = discount 

    def calculate_final_cost(self):
        total_cost = self.total_cost()
        return total_cost * (1 - self.discount)
    

#examples to show it works
#my objects 

beverage1 = coffee("Medium", 7.50)
beverage2 = tea("Small", 3.50)
beverage3 = matcha("Large", 9.00)

#creating regular customer 
reg_customer = regular_customer("Jadyn")
#creating a loyalty customer with name and discount
loyal_customer = loyalty_customer("Izzy", 0.20)

#for spacing
print()
print()


reg_customer.add_order(beverage1)
reg_customer.add_order(beverage3)
reg_customer.print_receipt()

#for spacing
print()
print("-" * 30)
print()

loyal_customer.add_order(beverage2)
loyal_customer.add_order(beverage1)
loyal_customer.add_order(beverage3)
loyal_customer.print_receipt()

#for spacing
print()
print()

