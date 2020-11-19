#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# we set infinity as a value much higher than any of our possible values
infinity = 99999 

# If there is no edge between two nodes, we set the adjacency value as infinity
crewmates_graph = [[0, 15, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 10, 9, 12, 9],
[15, 0, 9, infinity, infinity, infinity, 11, infinity, 12, infinity, 10, infinity, infinity, infinity], 
[infinity, 9, 0, 10, infinity, 7, infinity, infinity, infinity, infinity, infinity,infinity, infinity, infinity], 
[infinity, infinity, 10, 0, 12, 10, infinity, infinity, infinity, infinity, infinity, infinity,infinity, infinity], 
[infinity, infinity, infinity, 12, 0, 13,infinity, 6, 11, infinity, infinity, infinity, infinity,infinity], 
[infinity, infinity, 7, 10, 13, 0, infinity, infinity, infinity, infinity,infinity, infinity, infinity, infinity], 
[infinity, 11, infinity, infinity, infinity, infinity, 0, infinity, 8, infinity, infinity, infinity, infinity,infinity], 
[infinity, infinity, infinity, infinity, 6, infinity, infinity, 0, 9, infinity, infinity, infinity, infinity,infinity], 
[infinity, 12, infinity, infinity, 11, infinity, 8, 9, 0, 10, infinity, infinity, 14, infinity], 
[infinity, infinity, infinity, infinity,infinity, infinity, infinity, infinity, 10, 0, infinity, infinity, 14, infinity], 
[10, 10, infinity, infinity, infinity, infinity,infinity, infinity, infinity, infinity, 0, infinity, infinity, infinity], 
[9, infinity, infinity, infinity, infinity,infinity, infinity, infinity, infinity,infinity, infinity, 0, 9, 6], 
[12,infinity, infinity, infinity, infinity,infinity, infinity, infinity, 14, 14, infinity, 9, 0, 9], 
[9, infinity, infinity, infinity, infinity,infinity, infinity, infinity, infinity,infinity, infinity, 6, 9, 0]]

impostors_graph = [[0, 15, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 10, 9, 12, 0, infinity], 
[15, 0, 9, infinity, infinity, infinity, 0, infinity, 12, infinity, 10, infinity, infinity, infinity, 0], 
[infinity, 9, 0, 0, infinity, 7, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity], 
[infinity, infinity, 0, 0, 0, 10, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 6], 
[infinity, infinity, infinity, 0, 0, infinity, infinity, 6, 11, infinity, infinity, infinity, infinity, infinity,  6], 
[infinity, infinity, 7, 10, infinity,  infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity,  10], 
[infinity, 0, infinity, infinity, infinity, infinity, 0, infinity, 8, infinity, infinity, infinity, infinity, infinity, 0], 
[infinity, infinity, infinity, infinity, 6, infinity, infinity, 0, 9, infinity, infinity, infinity, infinity, infinity, infinity],  
[infinity, 12, infinity, infinity, 11, infinity, 8, 9, 0, 10, infinity, infinity, 14, infinity, infinity], 
[infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 10, 0, 0, 0, 14, infinity, infinity], 
[10, 10, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 0, 0, 0, infinity, infinity, infinity], 
[9, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 0, 0, 0, 9, 6, infinity],
[12, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 14, 14, infinity, 9, 0, 0, infinity],
[0, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 6, 0, 0, infinity], 
[infinity, 0, infinity, 6, 6, 10, 0, infinity, infinity, infinity, infinity, infinity, infinity, infinity, 0]]

names_rooms_crew = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Unnamed1", "Unnamed2", "Storage",  "Electrical", "Medbay", "Security", "Lower E", "Reactor"]

names_rooms_imp = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Unnamed1", "Unnamed2", "Storage", "Electrical", "MedBay", "Security", "Lower E", "Reactor", "Corridor W"]


# In[7]:


def floydWarshall(matrix):
    """Return the minimal distances between every node.
    
    :param matrix: Matrix of adjacency of a graph.
    :return: Matrix of minimal distances between every node.
    """
    dist = matrix
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)): 
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# In[8]:


df_crew = pd.DataFrame(floydWarshall(crewmates_graph), columns = names_rooms_crew, index = names_rooms_crew)
df_crew


# In[9]:


df_imp = pd.DataFrame(floydWarshall(impostors_graph), columns = names_rooms_imp, index = names_rooms_imp)
df_imp


# In[ ]:




