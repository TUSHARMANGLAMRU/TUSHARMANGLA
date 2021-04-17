#!/usr/bin/env python
# coding: utf-8

# ### LAB 03

# In[1]:


# WAP to demonstrate while loop with else statement.
i = 1
while i<4:
    print(i)
    i+=1
else:
    print("No More!")


# In[6]:


# WAP tp print first five even numbers(use break statement).
n = 2
while True:
    print(n)
    n+=2
    if n>10:
        break
        print(n)


# In[4]:


# WAP to print first four numbers(use continue statement).
for i in range(2,10):
    if i % 2:
        continue
    print(i)


# In[17]:


# WAP to demonstrate pass statement.
i = 4
if i>0:
    pass
print("Chirag is my friend")


# In[19]:


# WAP to calculate length of a string.
name = "GARG"
len(name)


# In[3]:


# WAP to count the number of characters in a string.
str1 = input("Please Enter a String : ")
total = 0
for i in str1:
    total = total + 1
print("Total Number of Characters in this String = ", total)  


# In[10]:


# WAP to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, 
# return instead of the empty string.
inputString="AnacondaIsWorst"
l=len(inputString)
newString=" "

for i in range (0,len(inputString)):
    if l<3:
        break
    else:
        if i in (0,1,l-2,l-1):
            newString=newString+inputString[i]
        else:
            continue
            
print("Input String = " + inputString)
print("New String = " + newString)


# In[14]:


# WAP to get a string from a given string where all occurrences of its first char have been changed to '$', except the first 
# char itself.
def specialreplace(s):
    firstchar = s[0]
    modifiedstr = s[1:].replace(firstchar, "$")
    print(firstchar + modifiedstr)

specialreplace('oompaloompa')


# In[15]:


# WAP to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


# In[17]:


# WAP to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('mix'))
print(add_string('fixing'))


# In[ ]:




