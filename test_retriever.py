from Src.retriever import get_retriever

retriever = get_retriever()

query = "What is CMMI?"

docs = retriever.invoke(query)

print("Retrieved Documents:\n")

for i, doc in enumerate(docs, 1):
    print("=" * 50)
    print(f"Document {i}")
    print(doc.page_content[:500])