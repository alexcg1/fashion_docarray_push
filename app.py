from helper import csv_to_docarray
from config import CSV_FILE, DOCARRAY_NAME, CSV_FILE, DATA_DIR, MAX_DOCS
import os
import subprocess
import sys
from zipfile import ZipFile
import shutil
import csv

data_dir = "../data"
dataset_name = "paramaggarwal/fashion-product-images-small"
# filename = "fashion-product-images-small.zip"
csv_filename = "styles.csv"


def create_docarray(csv_file, name, max_docs):
    print(f"Creating initial DocumentArray with maximum {max_docs} Documents")
    docs = csv_to_docarray(file_path=csv_file, max_docs=max_docs)

    print(f"Pushing {len(docs)} Documents to cloud with name {name}")
    docs.push(name)


def filter_good_rows(
    desired_field_count=MAX_DOCS,
    input_file=CSV_FILE,
):
    """
    Some CSVs may have different number of fields per row, which really messes up doc.tags. We'll remove these malformed rows
    """
    good_list = []
    wtflist = []

    output_filename = f"fixed_{input_file.split('/')[-1]}"
    output_file = f"{DATA_DIR}/{output_filename}"

    print("- Removing malformed rows")
    # Get fields
    with open(input_file, "r") as file:
        fields_string = file.readlines()[0]
        fields_list = fields_string.split(",")
        fields_list = [field.strip() for field in fields_list]

    with open(output_file, "w") as file:
        file.write(fields_string)

    with open(input_file, "r") as in_file, open(output_file, "a") as out_file:
        reader = csv.DictReader(in_file)

        writer = csv.DictWriter(out_file, fieldnames=fields_list)
        for row in reader:
            if len(row.keys()) == desired_field_count:
                good_list.append(row)
                writer.writerow(row)
            else:
                wtflist.append(row)

    print(f"GOOD: {len(good_list)} rows with {desired_field_count} keys")
    print(f"BAD: {len(wtflist)} rows with weird number of keys")


def __main__():
    filter_good_rows()
    create_docarray(csv_file=CSV_FILE, name=DOCARRAY_NAME, max_docs=MAX_DOCS)

    print(f"- Deleting original {csv_filename}")
    os.remove(csv_filename)

    print(f"- Renaming sanitized CSV to {csv_filename}")
    os.rename("fixed_styles.csv", csv_filename)
