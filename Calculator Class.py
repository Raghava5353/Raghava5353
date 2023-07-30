#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2 / self.num1

# Test the Calculator class with the provided sample input
obj = Calculator(10, 94)
print(obj.add())        # Output: 104
print(obj.subtract())   # Output: 84
print(obj.multiply())   # Output: 940
print(obj.divide())     # Output: 9.4


# In[ ]:




