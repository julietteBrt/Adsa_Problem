#!/usr/bin/env python
# coding: utf-8

# In[14]:


suspects = [1,4,5]
adjacency_matrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
      [0, 1, 0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
      [1, 0, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
      [0, 1, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 0, 0, 0, 1], 
      [0, 0, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 1, 0, 0]]
dead_players = [0]


# In[15]:


def getSusPairs(suspects, adjacency_matrix,dead_players):
    """Return the pairs of suspects of a game.
    
    :param suspects: Array of suspect players.
    :param adjacency_matrix: Matrix of players that have seen each other.
    :param dead_players: Array of players that have been eliminated.
    :return: Array of pairs of suspects.
    """
    suspects_pairs = []
    for suspect in suspects:
        for column in range(len(ajacency_matrix)):
            if(adjacency_matrix[suspect][column] == 0 and column not in dead_players and column != suspect):
                suspects_pairs.append([suspect,column])
    return suspects_pairs


# In[16]:


suspects = getSusPairs(suspects,adjacency_matrix,dead_players)
print(suspects)


# In[ ]:




