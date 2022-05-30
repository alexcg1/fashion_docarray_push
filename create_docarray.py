from jina import Flow
from helper import csv_to_docarray, remove_tensor
from config import CSV_FILE

MAX_DOCS = 10

pushed_name = "paramaggarwal-fashion-product-images-small"

# def embed_docs():

    # flow = (
        # Flow()
        # .add(
            # uses=f"jinahub://CLIPEncoder/v0.3.0",
            # name="image_encoder",
            # uses_with={"device": DEVICE},
            # install_requirements=True,
            # replicas=2,
        # )
    # )

    # with flow:
        # embedded_docs = flow.index(inputs=docs, show_progress=True, return_results=True)

    # return embedded_docs

print(f"Creating initial DocumentArray with maximum {MAX_DOCS} Documents")
docs = csv_to_docarray(file_path=CSV_FILE, max_docs=MAX_DOCS)

# Create embeddings
# print(f"Embedding {len(docs)} Documents via Flow")
# embedded_docs = embed_docs()

# Remove tensors to save space
# print(f"Removing tensors from {len(embedded_docs)} Documents to save space")
# embedded_docs.apply(remove_tensor)

# Push to cloud so others can download later
print(f"Pushing {len(docs)} Documents to cloud with name {pushed_name}")
docs.push(pushed_name)
