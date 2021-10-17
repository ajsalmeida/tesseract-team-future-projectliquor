import os

from pathlib import Path
from zipfile import ZipFile


data_dir = Path("../data")


def get_iowa_licor_dataset():
    if "Iowa_Liquor_Sales.csv" not in os.listdir(data_dir):
        os.system(
            f"poetry run kaggle datasets download -d residentmario/iowa-liquor-sales -p {data_dir}"
        )
        print("Extracting data...")
        with ZipFile(data_dir / "iowa-liquor-sales.zip", "r") as dataset_obj:
            dataset_obj.extractall(path=data_dir)
        os.remove(data_dir / "iowa-liquor-sales.zip")
    print("Done!")