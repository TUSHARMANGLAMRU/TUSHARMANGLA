#!/usr/bin/env python
# coding: utf-8

# ### LAB 06

# In[1]:


# Create an empty dictionary.
d1 = {}
print(d1)


# In[2]:


# Create the following dictionary 
# a. Key value
# b. A   10
# c. B   20
d1 = {"Key":"Value","A":"10","B":"20"}
print(d1)


# In[5]:


# Create a dictionary with different datatypes for keys.
d1 = {1:'abc', 2:12, 3:[1,2,3] ,4:12.21}


# In[3]:


# Print all the items of a dictionary.
d1 = {"A":"apple","B":"banana","C":"carrot"}
print(d1.items())


# In[4]:


# Delete an element of a dictionary.
d1 = {"A":"apple","B":"banana","C":"carrot"}
d2 = d1.pop("B")
print(d1)


# In[6]:


# Delete full dictionary.
d1 = {"A":"apple","B":"banana","C":"carrot"}
d2 = d1.clear()
print(d1)


# In[7]:


# Print a value for a key.
d1 = {"A":"apple"}
d2 = d1.values()
print(d2)


# In[8]:


# To check if a key is present in a dictionary.
def checkKey(dict, key):    
    if key in dict.keys():
        print("Present, ", end =" ")
        print("value =", dict[key])
    else:
        print("Not present")

dict = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dict, key)  


# In[9]:


# Update a value of a key.
d1 = {"name":"Chirag","country":"India","Gender":"Male"}
d2 = {"friend":"Tushar"}
d1.update(d2)
print(d1)


# In[10]:


# Add a new key value pair.
d1 = {"A":"apple","B":"banana"}
d1["C"]="carrot"
print(d1)


# In[1]:


# Print dictionary for keys{1,10} and values as square of keys.
d1=dict()
for x in range(1,11):
    d1[x]=x**2
print(d1)


# In[16]:


# Print nested dictionary.
d1 = {"A": {"name":"Tushar","age":"18","sex":"Male"},
      "B": {"name":"Chirag","age":"19","sex":"Male"}}

print(d1)


# In[17]:


# Concatenate three dictionaries. 
d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d4 = {}
for d in (d1, d2, d3): d4.update(d)
print(d4)


# In[18]:


# Sum all the values of a dictionary.
d1 = {"a":100,"b":-54,"c":247}
print(sum(d1.values()))


# In[19]:


# Accessing an element of a nested dictionary.
d1 = {"A": {"name":"Tushar","age":"18","sex":"Male"},
      "B": {"name":"Chirag","age":"19","sex":"Male"}}
print(d1["A"]["name"])
print(d1["A"]["age"])
print(d1["A"]["sex"])


# In[2]:


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are 
# square of keys.
d1=dict()
for x in range(1,16):
    d1[x]=x**2
print(d1)


# In[21]:


# Insert factorial of keys in values. And print dictionary.
d1 = {"1":"1","2":"2","3":"6","4":"24","5":"120","6":"720"}
print(d1)

