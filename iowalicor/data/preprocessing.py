import re
import unicodedata
from numpy import dtype
import pandas as pd
import dask.dataframe as dd

from random import randint, random



def slugify(text: str) -> str:
    slug = unicodedata.normalize("NFKD", text) \
        .encode("ascii", "ignore") \
        .lower().decode("utf-8")
    if "'" in slug:
        slug = slug.replace("'", "")
    if "-" in slug:
        slug = slug.replace("-", "")
    return re.sub(r"[^\w]+", "_", slug).strip("_")


def get_dataset_slice(filename: str, shuffle: bool =False) -> pd.DataFrame:
    dataset_chunks = dd.read_csv(
        filename,
        dtype={
            'County Number': "float64",
            'Bottle Volume (ml)': 'float64',
            'Bottles Sold': 'float64',
            'Item Number': 'float64',
            'Pack': 'float64',
            'Store Number': 'float64',
            'Vendor Number': 'object'
        })
    dataset_list = []
    for i in dataset_chunks.partitions:
        dataset_list.append(i)
    random_index = randint(0, len(dataset_list) - 1)
    if shuffle:
        return pd.DataFrame(
            dataset_list[random_index].compute().sample(frac=1)
        )
    else:
        return pd.DataFrame(dataset_list[random_index].compute())