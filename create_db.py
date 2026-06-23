import os

from Src.pdf_loader import load_document
from Src.text_splitter import split_text
from Src.embeddings import get_embeddings
from Src.vector_store import create_vector_store

# -----------------------------
# Load All PDF & Word Documents
# -----------------------------

documents = []

data_folder = "Data"

for file in os.listdir(data_folder):

    if (
    (file.endswith(".pdf") or file.endswith(".docx"))
    and not file.startswith("~$")
):

        file_path = os.path.join(data_folder, file)

        print(f"\nLoading: {file}")

        docs = load_document(file_path)

        documents.extend(docs)

print("\nTotal Documents:", len(documents))

# -----------------------------
# Split Text into Chunks
# -----------------------------

chunks = split_text(documents)

print("Total Chunks:", len(chunks))

if len(chunks) > 0:
    print("\nFirst Chunk:")
    print(chunks[0].page_content[:500])

# -----------------------------
# Load Embeddings
# -----------------------------

embeddings = get_embeddings()

print("\nEmbeddings Loaded Successfully")
print(type(embeddings))

# -----------------------------
# Create Vector Store
# -----------------------------

vector_db = create_vector_store(chunks)

print("\nVector Store Created Successfully!")