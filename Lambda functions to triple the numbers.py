#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Sample list of integers
sample_list = [1, 2, 3, 4, 5, 6, 7]

# Define a lambda function to triple the numbers
triple = lambda x: x * 3

# Use map to apply the lambda function to each element in the list
tripled_list = list(map(triple, sample_list))

# Print the result
print("Sample list:", sample_list)
print("Triple of list numbers:", tripled_list)


# In[ ]:




