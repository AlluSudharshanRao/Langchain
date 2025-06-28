from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy

embedding = OpenAIEmbeddings(model = 'text-embedding-3-large', dimensions=300)

documents = [
    ""
    ""
]

query = 'tell me about Virat kohli'

doc_embedding = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embedding)

index, score =sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])

print('similarity score is:', score)