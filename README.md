## Design and Implementation of LangChain Expression Language (LCEL) Expressions

### AIM:
To design and implement a LangChain Expression Language (LCEL) expression that utilizes at least two prompt parameters and three key components (prompt, model, and output parser), and to evaluate its functionality by analyzing relevant examples of its application in real-world scenarios.

### PROBLEM STATEMENT:
LangChain Expression Language (LCEL) simplifies interactions with large language models (LLMs) by creating reusable and structured expressions. This task involves:

1.Designing an LCEL expression with dynamic prompt parameters (e.g., topic and length).

2.Using three essential components: Prompt- A structured input with placeholders for parameters, Model- An LLM used to process the prompt and Output Parser- A parser to interpret the model's output.

3.Demonstrating the LCEL expression's functionality in generating structured, relevant outputs.
### DESIGN STEPS:

#### STEP 1:
Identify the parameters (topic and length) to allow dynamic customization of prompts.

#### STEP 2:
Create a structured prompt template with placeholders for parameters.

#### STEP 3:
Design an output parser to format and structure the model's output.
#### STEP 4:
Combine the prompt template, model, and output parser into a LangChain pipeline.

#### STEP 5:
Test the LCEL expression using multiple input values for topic and length.

### PROGRAM:
```
developed by:Shabreena Vincent
reg no:212222230141
```
```
import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

#!pip install pydantic==1.10.8

from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "Write a {tone} introduction about {topic} for a blog post."
)
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

result = chain.invoke({
    "topic": "Generative AI in Education",
    "tone": "friendly"
})


print(result)
```
### OUTPUT:


<img width="1285" height="130" alt="image" src="https://github.com/user-attachments/assets/28a57f36-7647-4521-aacb-d06ec1d31bdf" />

### RESULT:
Thus, the LangChain Expression Language (LCEL) expression that utilizes two prompt parameters and three key components (prompt, model, and output parser) was designed and implemented successfully. And also evaluated its functionality by analyzing relevant examples of its application in real-world scenarios.
