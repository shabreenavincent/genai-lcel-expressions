#!/usr/bin/env python
# coding: utf-8

# # LangChain Expression Language (LCEL)

# In[10]:


import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


# In[11]:


#!pip install pydantic==1.10.8


# In[12]:


from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser


# ## Simple Chain

# In[13]:


prompt = ChatPromptTemplate.from_template(
    "Write a {tone} introduction about {topic} for a blog post."
)
model = ChatOpenAI()
output_parser = StrOutputParser()


# In[19]:


chain = prompt | model | output_parser


# In[20]:


result = chain.invoke({
    "topic": "Generative AI in Education",
    "tone": "friendly"
})


# In[21]:


print(result)

