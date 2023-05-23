#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pyautogui.click -> clique com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar uma combinação de teclas (ex: Ctrl + D)
# Passo a passo


# In[19]:


import pyautogui
import time

pyautogui.PAUSE = 1

# Passo 1 : acessar o sistema da empresa

pyautogui.hotkey("ctrl", "n")
pyautogui.click(x=203, y=61)
pyautogui.click(x=1214, y=31)
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Fazer login no sistema da empresa

pyautogui.click(x=1360, y=384)
pyautogui.write("meu login")

pyautogui.click(x=1348, y=461)
pyautogui.write("minha senha")

pyautogui.click(x=1290, y=527)

time.sleep(5)

# Passo 3 : Baixar a base de dados

pyautogui.click(x=361, y=471)
pyautogui.click(x=481, y=361)
pyautogui.click(x=562, y=791)


# In[14]:


# Passo 4: Calcular os indicadores

import pandas as pd

# importar dados
tabela = pd.read_csv(r"C:\Users\Fernando\Downloads\Compras.csv", sep=";")
display(tabela)

# calculo dos indicadores

# total gasto -> somar coluna valor final
total_gasto = tabela["ValorFinal"].sum()

# quantidade -> somar coluna quantidade
quantidade = tabela["Quantidade"].sum()

# preço médio -> total gasto / quantidade
preco_medio = total_gasto / quantidade

display(total_gasto)
display(quantidade)
display(preco_medio)


# In[ ]:


# Passo 5: Enviar o e-mail para diretoria


# In[18]:


time.sleep(5)
print(pyautogui.position())


# In[25]:


get_ipython().system('pip install pyautogui')


# In[ ]:




