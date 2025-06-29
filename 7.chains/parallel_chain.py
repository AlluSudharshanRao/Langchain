from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


load_dotenv()

model1 = ChatAnthropic(model = "claude-3-5-sonnet-20241022")
model2 = ChatAnthropic(model = "claude-3-haiku-20240307")

prompt1 = PromptTemplate(
    template = "Generate a report on the {topic}",
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate top palyers of the following \n {topic}",
    input_variables=['text'] 
)

prompt3 = PromptTemplate(
    template= " Merge the report and top players into single document \n notes -> {report} and summary {top_players}",
    input_variables=['report', 'summary']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'report' : prompt1 | model1 | parser,
    'top_players': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"topic" : "cricket"})

print(result)

chain.get_graph().print_ascii()