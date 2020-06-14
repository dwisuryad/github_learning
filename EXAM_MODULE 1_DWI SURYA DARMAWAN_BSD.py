#!/usr/bin/env python
# coding: utf-8

# In[25]:


# soal 1

def Hastag(string):
    kata = len(string)
     
    for kata in range (len(string)):
        if kata<140 and kata>=1:
             print('#'+string.title())
        elif kata>140:
            print('false')
        else:
            kata = ('')
            print('false')

Hastag('Hello there how are you doing')
Hastag('Hello World')
Hastag('')


# In[21]:


# soal 2

def create_phone_number(number):
    
    number = []
        for a in range(0,9):
            if (a(0,2)):
                print(a, "()")
            elif (a(3,5)):
                a + ("-")
            else:
                print(a(6:))

                


# In[ ]:


# soal 3

def sort_odd_even(num):
    
    angka = 0
    for a in num%2 == 0:
        
    

