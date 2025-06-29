from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatAnthropic(model = "claude-3-5-sonnet-20241022")

prompt = PromptTemplate(
    template = " Generate short note about {topic}",
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result =chain.invoke({"topic": 'cricket'})

print(result)

chain.get_graph().print_ascii()