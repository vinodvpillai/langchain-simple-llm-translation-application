from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

import os
from os.path import join, dirname
from dotenv import load_dotenv

# Loading the environment variables
dotenv_path  = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Prompt
prompt = ChatPromptTemplate.from_messages([("system","Translate the following from English into {language}"),("user","{text}")])

# LLM Model
llm = ChatOpenAI(api_key=os.environ.get('OPENAI_API_KEY'), model=os.environ.get('OPENAI_MODEL'), temperature=0.5) # type: ignore

# Output Parser
parser = StrOutputParser()

# Chain
chain = prompt | llm | parser
print(chain.invoke({"language": "italian", "text": "hi"}))