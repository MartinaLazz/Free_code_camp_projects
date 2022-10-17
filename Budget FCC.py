#!/usr/bin/env python
# coding: utf-8

# In[13]:


#Complete the Category class in budget.py. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list.

class Category:
    def __init__(self, cat):
        self.cat = cat
        self.ledger = []
        self.balance = 0
        
    #A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True
    
    #A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        
    #A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False
    
    #A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
        return self.balance
    
    #A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    def transfer(self, amount, other_cat):
         if self.check_funds(amount):
            self.withdraw(amount, ("Transfer to " + other_cat.cat))
            other_cat.deposit(amount, ("Transfer from " + self.cat))
            return True
         else:
            return False
        
    #When the budget object is printed it should display:

#A title line of 30 characters where the name of the category is centered in a line of * characters.
#A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
#A line displaying the category total.

    def __str__(self):
        first = '*' * int((15 - len(self.cat) / 2)) + self.cat + '*' * int((15 - len(self.cat) / 2))
        second = ''
        for element in self.ledger:
            if len(element['description']) <= 23: 
                second += '{:23} {:7.2f}'.format(element['description'], element['amount']) + '\n' 
            else:
                second += '{}{:7.2f}'.format(element['description'][:23], element['amount']) + '\n'
        second = second.rstrip()
        third = 'Total: {:.2f}'.format(self.balance)
        return first + '\n' + second + '\n' + third
        


# In[14]:


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)


# In[ ]:




