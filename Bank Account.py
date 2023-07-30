#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

# Test the classes
account = Account("Ashish", 5000)
print(f"Account Title: {account.title}, Balance: {account.balance}")

savings_account = SavingsAccount("Ashish", 5000, 5)
print(f"Savings Account Title: {savings_account.title}, Balance: {savings_account.balance}, Interest Rate: {savings_account.interestRate}")


# In[ ]:




