from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
)


prompt = PromptTemplate.from_template("{question}")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)