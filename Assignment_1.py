#!/usr/bin/env python
# coding: utf-8

#     
# Write a program which will find all such numbers which are divisible by 7 but are not 
# a multiple of 5 ,between 2000 and 3200 ( both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line

# In[31]:


list1=list(range(2000, 3201))
list2=[]
for number in list1:
    lastDigit = int(repr(number)[-1])    
    remaining_digits=int(repr(number)[0:3])
    double_lastDigit=lastDigit*2    
    substracted_digit=remaining_digits-double_lastDigit
    if (substracted_digit%7==0 and number%5!=0 ) :
        list2.append(number)
str1=str(list2)
print(str1[1:-1])
        

        

    
     

    


#  Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name

# In[12]:


first_name=input("enter first name-")
last_name=input("enter first name-")
full_name="{} {}".format(first_name,last_name)
reversed_name = "".join(reversed(full_name))
print(reversed_name)
lambda full_name:print(reversed(full_name))


# In[13]:


first_name=input("enter first name-")
last_name=input("enter first name-")
full_name="{} {}".format(first_name,last_name)
full_name[::-1]


# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3

# In[32]:



radius=float(input("enter radius to find sphere diameter"))
pi=3.14
v=4/3*(pi*(radius**3))
print(v)


# In[ ]:




