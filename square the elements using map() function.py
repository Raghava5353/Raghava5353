#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sample list of integers
sample_list = [4, 5, 2, 9]

# Define a lambda function to square the numbers
square = lambda x: x ** 2

# Use map to apply the lambda function to each element in the list
squared_list = list(map(square, sample_list))

# Print the result
print("Sample list:", sample_list)
print("Square of list numbers:", squared_list)


# In[ ]:




