#!/usr/bin/env python
# coding: utf-8

# # IPL Data Analysis And Visualization

# IPL stands for Indian Premier Leaguea professional T20 league, started in 2008 by BCCI that happens every Year in India.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# # Reading Data using Pandas

# In[2]:


ipl=pd.read_csv("matches.csv")
ipl.head()


# info() Command help us to see the type of values contains in each Columns.

# In[3]:


ipl.info()


# In[4]:


ipl["team1"].unique()


# In[5]:


ipl["city"].unique()


# In[6]:


ipl["winner"].unique()


# # Total Number of Matches won by Teams

# In[7]:


match_winner=ipl["winner"].value_counts().reset_index()
match_winners=match_winner.rename(columns={"index":"Team","winner":"Winner"})
match_winners


# Visualizing the above Data

# In[8]:


plt.figure(figsize=(10,8))
sns.barplot(y=match_winners["Team"],x=match_winners["Winner"],orient="h",palette="rocket")
plt.xlabel("Number of Matches won",fontsize=20)
plt.ylabel("Teams",fontsize=20)
plt.show()


# In[9]:


tosswinner=ipl["toss_winner"].value_counts().reset_index().rename(columns={"index":"Teams","toss_winner":"Toss Winner"})
tosswinner


# In[10]:


plt.figure(figsize=(10,8))
sns.barplot(y=tosswinner["Teams"],x=tosswinner["Toss Winner"],orient="h",palette="rocket")
plt.xlabel("Toss Winner",fontsize=20)
plt.ylabel("Teams",fontsize=20)
plt.show()


# # Mumbai Indians won the Maximun Numbers of Matches as well  Tosses

# # From the above Analysis It presume that Team which wins the toss also wins the Match.  

# 

# # Match Played in Each Season

# In[11]:


seasons=pd.DatetimeIndex(ipl["date"]).year.value_counts().reset_index().rename(columns={"index":"Year","date":"Matches"})
seasons


# In[12]:


plt.figure(figsize=(10,8))
sns.barplot(x=seasons["Year"],y=seasons["Matches"],palette="mako",data=ipl)
plt.xlabel("Seasons",fontsize=20)
plt.ylabel("Total Matches",fontsize=20)
plt.show()


# 

# # Most Preferred Decision On winning Toss i.e. Choose To Bat / Choose To Field
# 
# 

# In[13]:


Q=ipl["toss_decision"].value_counts().reset_index().rename(columns={"index":"Toss Decision","toss_decision":"Counts"})
Q


# In[14]:


plt.figure(figsize=(5,6))
sns.barplot(x=Q["Toss Decision"],y=Q["Counts"],palette="rocket")
plt.xlabel("Decision",fontsize=20)
plt.ylabel("Counts",fontsize=20)
plt.show()


# In[15]:


A=(ipl["toss_decision"]=="field") & (ipl["toss_winner"]==ipl["winner"])
X=A.reset_index().rename(columns={"index":"index",0:"Result"})
Field=X[X["Result"]==True]["Result"].count()
Field


# In[16]:


B=(ipl["toss_decision"]=="bat") & (ipl["toss_winner"]==ipl["winner"])
S=B.reset_index().rename(columns={"index":"index",0:"outcome"})
Bat=S[S["outcome"]==True]["outcome"].count()
Bat


# In[17]:


T=ipl["toss_decision"].value_counts().reset_index().rename(columns={"index":"Decision","toss_decision":"Counts"})
T.at[0,"Counts"]=273
T.at[1,"Counts"]=145
T


# In[18]:


plt.figure(figsize=(6,6))
sns.barplot(x=T["Decision"],y=T["Counts"],orient="v",palette="crest")
plt.title("Decision Success",fontsize=20)
plt.xlabel("Decision ",fontsize=20)
plt.ylabel("Counts",fontsize=20)
plt.show()


# In[22]:


plt.figure(figsize=(10,8))
sns.set_style("white")
sns.countplot(data=ipl,x="Season",hue="toss_decision",palette="icefire")


# From the above visualization it is clear that fielding first result in winning more number of matches.

# # Total Number of Matches and there Result

# In[23]:


seasons=pd.DatetimeIndex(ipl["date"]).year.value_counts().reset_index().rename(columns={"index":"Year","date":"Matches"})
seasons


# In[24]:


seasons["Matches"].sum()


# In[25]:


ipl["result"].value_counts().reset_index()


# In[26]:


plt.figure(figsize=(10,8))
sns.countplot(x=ipl["result"],data=ipl,hue="toss_decision",palette="mako")
plt.xlabel("Seasons",fontsize=20)
plt.ylabel("Total Matches",fontsize=20)
plt.show()


# There is only 13 Matches that tie throughout the Seasons

# # Top 10 Players Throughout the Seasons

# In[27]:


Player_of_Match=ipl["player_of_match"].value_counts().reset_index().rename(columns={"index":"Players","player_of_match":"Player of Match"})
POM=Player_of_Match.head(10)
POM


# In[28]:


plt.figure(figsize=(10,5))
sns.barplot(y=POM["Players"],x=POM["Player of Match"],orient="h",palette="crest")
plt.title("Players Getting Tittle of Player of Match",fontsize=20)
plt.xlabel("Number Of Times Player Get The Tittle of Player Of The Match ",fontsize=20)
plt.ylabel("Players",fontsize=20)
plt.show()


# # Team That Won The IPL Trophy Most  Number Of Times

# In[20]:


abc=pd.DatetimeIndex(ipl["date"]).year
abc


# In[21]:


ipl["Season"]=abc


# In[29]:


final=ipl.groupby("Season").tail(1)
f=final["winner"].value_counts().reset_index()
f


# In[30]:


plt.figure(figsize=(8,5))
sns.barplot(y=f["index"],x=f["winner"],orient="h",palette="flare")
plt.title("Season Winners",fontsize=20)
plt.xlabel("Count ",fontsize=20)
plt.ylabel("Team",fontsize=20)
plt.show()


# # Conclusion Drawn From Analysis

# 1. A total of 816 matches have been played Out of these 816 matches 803 matches were played normally and had a normal result'
# 2. Mumbai Indian's Have Won the Most Number of Matches - "120", followed by Chennai Super Kings with "106" Matches
# 3. IPL-2013 Season Hosted most Number of Matches - "76"
# 4. AB de Villiers has been the Man Of The Match Most Number of Times with "23" Awards followed by Chris Gayle "22".
# 5. Mumbai Indians Have been the IPL Champions Most number of times - 5 followed by Chennai Super Kings - "3".
# 6. Mumbai Indians and Chennai Super Kings have been the dominant Teams.
# 

# In[ ]:




