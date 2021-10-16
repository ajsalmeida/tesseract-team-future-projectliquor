import os

from zipfile import ZipFile


def get_iowa_licor_dataset():
    if "Iowa_Liquor_Sales.csv" not in os.listdir("data/"):
        os.system(
            "poetry run kaggle datasets download -d residentmario/iowa-liquor-sales -p data"
        )
        print("Extracting data...")
        with ZipFile("data/iowa-liquor-sales.zip", "r") as dataset_obj:
            dataset_obj.extractall(path="data/")
        os.remove("data/iowa-liquor-sales.zip")
    print("Done!")