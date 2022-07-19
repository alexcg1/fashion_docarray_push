from helper import csv_to_docarray

def create_docarray(csv_file, name, max_docs):
    print(f"Creating initial DocumentArray with maximum {max_docs} Documents")
    docs = csv_to_docarray(file_path=csv_file, max_docs=max_docs)

    print(f"Pushing {len(docs)} Documents to cloud with name {name}")
    docs.push(name)
