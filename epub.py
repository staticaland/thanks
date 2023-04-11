from langchain.document_loaders import UnstructuredEPubLoader

loader = UnstructuredEPubLoader("captain-charles-johnson_a-general-history-of-the-pirates.epub")

data = loader.load()

print(data)