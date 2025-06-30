from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = 'claude-3-5-sonnet-20241022')

prompt1 = PromptTemplate(
    template="Explain the facts about the {topic}",
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template="Hight the top 5 facts from the explantion \n {text}",
    input_variables=['text']
)

parser = StrOutputParser() 

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

print(chain.invoke({'topic':"crime rate in India"}))