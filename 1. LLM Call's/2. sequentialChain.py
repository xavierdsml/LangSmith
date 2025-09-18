from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
os.environ['LANGCHAIN_PROJECT']='Sequential LLM'
load_dotenv()

model1 = ChatGoogleGenerativeAI(
  model = "gemini-1.5-flash",
  temperature=0.7
)


model2 = ChatGoogleGenerativeAI(
  model = "gemini-2.5-flash",
  temperature=0.5
)

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()
chain = prompt1 | model1 | parser | prompt2 | model2 | parser

config = {
  'tags':['llm app', 'report-generation', 'report-summarizaer'],

  'metadata':{
    'model1': 'gemini-1.5-flash', 
    'model1-temp': 0.7, 
    'parser': 'strOutputParser'
  }
}

result = chain.invoke({'topic': 'Unemployment in India'})
print(result)