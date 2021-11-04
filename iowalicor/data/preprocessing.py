import re
import unicodedata
from numpy import dtype
import pandas as pd
import dask.dataframe as dd

from random import randint



def slugify(text: str) -> str:
    """Standardizes the text data to lowercase without accent.
    Spaces are replaced to underlines and apostrophes are removed.

    Parameters
    ----------
    text: str
        text to be slugified.
    
    Returns
    -------
    Slugified (Standardized) text.

    Examples
    --------
    >>> slugify("O'brein County")
    obrein_county
    >>> slugify("Isso é uma coisa")
    isso_e_uma_coisa
    """
    slug = unicodedata.normalize("NFKD", text) \
        .encode("ascii", "ignore") \
        .lower().decode("utf-8")
    if "'" in slug:
        slug = slug.replace("'", "")
    if "-" in slug:
        slug = slug.replace("-", "")
    return re.sub(r"[^\w]+", "_", slug).strip("_")


def get_dataset_slice(
    filename: str,
    shuffle: bool = False,
    random_state: int = None
) -> pd.DataFrame:
    """Get a random slice of the dataset.
    It uses the dask library to handle multiple chunks of the big dataset.

    Parameters
    ----------
    filename: str
        File path to the dataset .csv.
    shuffle: bool
        If True, the function returns a random chunk of the dataset with shuffled data. 
        If False, it returns a yet random chunk, but the data will not be shuffled.
    random_state: int
        If this argument receives an integer, this value is used as a seed to the
        pseudo random generator.
    
    Returns
    -------
    A pandas DataFrame with the random chunk, shuffled or not.
    """
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
            dataset_list[random_index].compute().sample(
                frac=1,
                random_state=random_state
            ).reset_index(drop=True)
        )
    else:
        return pd.DataFrame(dataset_list[random_index].compute())