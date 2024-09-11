#!/usr/bin/env python
# coding: utf-8

# Importamos las librerias necesarias

# In[7]:


from itertools import product
from fractions import Fraction 
from collections import defaultdict

Definimos una funcion de probabilidad donde A es el tamaño del evento y Omega es el tamaño de todos los eventos
# In[9]:


def Probabilidad (A, Omega):
    P = Fraction (len(A), len (Omega))
    return P 


# Definimos un espacio muestral Omega dado por: 

# In[10]:


L = [i for i in range (1,7)]
Omega = set (product(L, repeat = 2))
S = {(i,j): abs(i-j) for i,j in Omega}


# Obtenemos las probabilidades de que la diferencia de las caras sea mayor a 1 y menor a 1 
# Sabiendo que la suma de todo es 1 

# In[12]:


dS = defaultdict(set)
for i,j in S.items():
    dS[j].add(i)

KeyS = { k : Probabilidad(A, Omega) for k,A in dS.items() if k>1}
KeyS
suma_probabilidades = sum(KeyS.values())
print(f"Suma de las fracciones: {suma_probabilidades}")
KeyS2 = {k : Probabilidad(A, Omega) for k,A in dS.items() if k<=1}
suma_probabilidades_2 = sum(KeyS2.values())
print(f"Suma de las fracciones: {suma_probabilidades_2}")


# In[14]:


S = {(i,j): i + j for i,j in Omega}

dS = defaultdict(set)
for i,j in S.items():
    dS[j].add(i)

KeyS = { k : Probabilidad(A, Omega) for k,A in dS.items() if k%2 == 0}
KeyS
suma_probabilidades = sum(KeyS.values())
print(f"Suma de las fracciones: {suma_probabilidades}")
KeyS2 = {k : Probabilidad(A, Omega) for k,A in dS.items() if k%2 == 1}
suma_probabilidades_2 = sum(KeyS2.values())
print(f"Suma de las fracciones: {suma_probabilidades_2}")


# In[17]:


S = {(i,j): i + j for i,j in Omega}

dS = defaultdict(set)
for i,j in S.items():
    dS[j].add(i)
KeyS = { k : Probabilidad(A, Omega) for k,A in dS.items()}

import matplotlib.pyplot as plt 

plt.figure(figsize = (10,6))
sumas = list(KeyS.keys())
probabilidades = [float(p) for p in KeyS.values()]
plt.bar(sumas, probabilidades, color = 'red')
plt.xlabel('Suma')
plt.ylabel('Probabilidad')
plt.title('Probabilidad de cada suma en el conjunto de pares')
plt.grid(axis = 'y')
plt.show()


# In[ ]:




