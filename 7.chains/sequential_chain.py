from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model1 = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
model2 = ChatAnthropic(model = "claude-3-haiku-20240307")

prompt1 = PromptTemplate(
    template = "Generate a report on the {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate summary of the following text \n {text}",
    input_variables=['text'] 
)

parser = StrOutputParser()


chain = prompt1 | model1 | parser | prompt2 | model2 | parser 

result= chain.invoke({'topic' : 'cricket'})

print(result)

chain.get_graph().print_ascii()