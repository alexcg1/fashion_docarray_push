from docarray import DocumentArray
from config import DOCARRAY_NAME

docs = DocumentArray.pull(DOCARRAY_NAME)

for doc in docs:
    print(doc)
    print(doc.tags)
