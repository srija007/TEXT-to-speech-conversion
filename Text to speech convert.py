#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pyttsx3')


# In[2]:


import pyttsx3


# In[3]:


text_speech = pyttsx3.init()


# In[41]:


answer = input("What do you want me to tell: ")
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[1].id) 
rate = text_speech.getProperty('rate')
text_speech.setProperty('rate',125)

text_speech.say(answer)
text_speech.runAndWait()


# In[ ]:




