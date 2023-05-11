#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Statements Assessment Test
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[3]:


st = 'Print only the words that start with s in this sentence'


# In[6]:


#Code here
words = st.split()
for word in words:
    if word[0] == 's':
        print(word)


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[11]:


#Code Here
for num in range(0, 11):
    if num % 2 == 0:
        print(num)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[15]:


#Code in this cell
[num for num in range(1, 50) if num % 3 == 0]


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[22]:


st = 'Print every word in this sentence that has an even number of letters'


# In[24]:


#Code in this cell
for word in st.split(' '):
    if word.count('') % 2 != 0:
        print(word)


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[26]:


#Code in this cell
for num in range(1, 100):
    if (num % 3 == 0) and (num % 5 == 0):
        print("FizzBuzz")
    elif (num % 3 == 0):
        print("Fizz")
    elif (num % 5 == 0):
        print("Buzz")
    else:
        print(num)


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[28]:


st = 'Create a list of the first letters of every word in this string'


# In[31]:


#Code in this cell
newList = list()
for word in st.split(" "):
    newList.append(word[0])
newList


# ### Great Job!
