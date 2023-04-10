# You can also use tiktoken, a open source tokenizer package from OpenAI to estimate tokens used. Will probably be more accurate for their models.

from langchain.embeddings import OpenAIEmbeddings
import os

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

text = "Hi! It's time for the beach"

text_embedding = embeddings.embed_query(text)
print (f"Your embedding is length {len(text_embedding)}")
print (f"Here's a sample: {text_embedding[:5]}...")
