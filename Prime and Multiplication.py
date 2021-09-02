#!/usr/bin/env python
# coding: utf-8

# In[18]:



###Prime or not


# In[17]:


n=int(input("Enter a number:"))
def CheckIfPrime(n):
    if n<=1 or n%1>0:
        return False
    for i in range (2,n//2):
        if n%i ==0:
            return False
    return True
print(CheckIfPrime(n))


# In[ ]:


#Multiplication


# In[19]:


num = int(12)

for i in range(1, 11):
    print ("%d * %d = %d" % (num, i, num * i))


# In[ ]:




