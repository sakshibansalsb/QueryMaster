# Import necessary classes and functions from llama_index and other libraries.
import os
import docx2txt
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv

# Load documents from the 'data' directory using SimpleDirectoryReader.
documents = SimpleDirectoryReader("data").load_data()

# Set the API key for accessing the Gemini model.
load_dotenv()
gemini_api_key=os.getenv('GEMINI_API_KEY')
# Set the embedding model to be used in the settings. Here, a HuggingFace model is specified.
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Set the language model to be used in the settings. Here, the Gemini model is specified with an API key.
Settings.llm = Gemini(api_key=gemini_api_key, model_name="models/gemini-pro")

# Create a VectorStoreIndex from the loaded documents. This index will be used for querying.
index = VectorStoreIndex.from_documents(documents,)

# Create a query engine from the index. The query engine will handle querying the documents.
query_engine = index.as_query_engine()

# Query the index with a specific question and print the response.
response = query_engine.query("What did the author do growing up?")
print(response)
