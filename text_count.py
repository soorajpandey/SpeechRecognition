
# coding: utf-8

# In[23]:


name = input('Enter file: ')


# In[28]:


handle = open(name, 'r')


# In[4]:


text = handle.read()


# In[5]:


words = text.split()


# In[8]:


counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None


# In[26]:


word


# In[27]:


for word,count in counts.items():
    if bigcount is None or count:
        
        bigcount
        bigword = word
        bigcount = count

print (bigword + "\t" + str(bigcount))

