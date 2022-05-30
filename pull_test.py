from docarray import DocumentArray

pushed_name = "paramaggarwal-fashion-product-images-small"
docs = DocumentArray.pull(pushed_name)

for doc in docs:
    print(doc)
    print(doc.tags)
