
# coding: utf-8

# # Symbolinen laskenta sympy-kirjastoa käyttäen
# 
# Tässä muistikirjassa käydään läpi Pythonin symbolisen laskennan sympy-kirjaston perusulottuvuuksia.

# In[1]:


import sympy


# In[2]:


z**


# In[3]:


sympy.var('z') # esitellään muuttuja ensin


# In[5]:


z**2 # nyt sillä voidaan laskea


# In[7]:


True^True # ^ on varattu Pythonissa XOR-operaatiolle


# In[8]:


True^False


# In[11]:


z**(1/2) 


# Yllä Python laskee suluissa olevan jakolaskun ensin
# ja siitä tulee Python-objekti ennen kuin SymPy ehtii muuttaa sen SymPyn olioksi.

# Ratkaisu on käyttää sympify() tai Rational-luokkaa.

# In[14]:


z**(sympy.sympify(1)/2)


# In[16]:


z**sympy.Rational(1/2)


# Esitellään muuttujia:

# In[21]:


from sympy import symbols
x, y, z = symbols('x y z')
u, v, w = symbols('u v w')
symbols('j0:7')


# In[23]:


g, h = symbols('h g')


# In[24]:


g


# In[25]:


h


# Variables Assignment does not Create a Relation Between Expressions

# In[28]:


from sympy import Symbol
a=Symbol('a') # muuttujan a arvo a


# In[29]:


b=a+1 # muuttujan b arvo lauseke a+1


# In[30]:


print(b)


# In[31]:


a=4 # nyt a osoittaa kokonaislukuun 4, ei symboliin a


# In[32]:


print(a)


# In[33]:


print(b) # b osoittaa lausekkeeseen, jonka arvo a+1


# In[34]:


p=Symbol('p')


# In[36]:


sympy.sqrt(p**2)


# In[37]:


p=Symbol('p', positive=True)


# In[38]:


sympy.sqrt(p**2)

