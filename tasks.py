import os
from invoke import task

from pathlib import Path
from zipfile import ZipFile


data_dir = Path("data") / "raw"

@task
def get_dataset(c):
    """Automation for the dataset getting.
    Task to automate the download and unpacking of the data.
    """
    if "Iowa_Liquor_Sales.csv" not in os.listdir(data_dir):
        c.run(
            f"poetry run kaggle datasets download -d residentmario/iowa-liquor-sales -p {data_dir}"
        )
        print("Extracting data...")
        with ZipFile(data_dir / "iowa-liquor-sales.zip", "r") as dataset_obj:
            dataset_obj.extractall(path=data_dir)
        c.run(f"rm -rf {data_dir / 'iowa-liquor-sales.zip'}")
    print("Done!")
