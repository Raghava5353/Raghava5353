#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber

# Test the Student class
student = Student()
student.setName("John Doe")
student.setRollNumber("12345")

print(student.getName())       # Output: John Doe
print(student.getRollNumber()) # Output: 12345


# In[ ]:




