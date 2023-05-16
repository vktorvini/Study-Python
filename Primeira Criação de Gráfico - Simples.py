#!/usr/bin/env python
# coding: utf-8

# In[4]:


#importando a biblioteca e nomeando para deixar mais facil
import matplotlib.pyplot as plt


# In[5]:


#atribuição dos valores com duas tabelas
meses = ['janeiro','fevereiro','março','abril','maio','junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]


# In[15]:


#criar a tabela com os campos anteriores sendo(X,Y)
plt.plot(meses,valores,color='blue',marker='o')
#da titulo ao grafico
plt.title('Faturamento no primeiro semestre de 2017')
# label da rotulo aos eixos X e Y
plt.xlabel('meses')
plt.ylabel('Faturamento em R$')
#o ylim() limita o valor da linha y para uma melhor vizualização
plt.ylim(100000,120000)
#show mostra o gráico
plt.show()


# In[4]:





# In[ ]:





# In[ ]:




