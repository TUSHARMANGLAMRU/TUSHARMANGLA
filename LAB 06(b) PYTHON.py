#!/usr/bin/env python
# coding: utf-8

# ### LAB 06

# In[1]:


# WAP to create a set.
a = {1,3,5,7}
print(a)


# In[6]:


# WAP to add an element to the set.
a = {1,3,5,7}
a.add(9)
print(a)


# In[7]:


# WAP to add multiple items using update function.
a = {1,2,3}
b = {4,5,6}
result = a.update(b)
print(a)


# In[8]:


# WAP to find length of a set.
a = {1,2,3,4,5}
print(len(a))


# In[9]:


# WAP to remove a value from a set.
a = {1,2,3,4}
a.remove(4)
print(a)


# In[11]:


# WAP to pop an element from a set.
a = {1,2,3,4,5}
a.pop()
print(a)


# In[12]:


# WAP to update a set.
a = {1,2,3}
b = {4,5,6}
result = a.update(b)
print(a)


# In[13]:


# WAP to create an intersection of sets.
a = {1,2,3}
b = {3,4,5}
c = a & b
print(c)


# In[15]:


# WAP to create a union of sets.
a = {1,2,3}
b = {3,4,5}
c = a | b
print(c)


# In[16]:


# WAP to clear a set.
a = {1,2,3,4,5,6,7,8,9}
a.clear()
print(a)


# In[19]:


# WAP to issubset and issuperset.
a = {1,2,3,4,5}
b = {2,4,1}
print(a.issubset(b))
print(a.issuperset(b))


# In[23]:


# WAP to create set difference.
a = {1,2,3}
b = {3,4,5}
print(a - b)


# In[25]:


# WAP to create symmetric difference.
a = {1,2}
b = {2,3}
print(a^b)

