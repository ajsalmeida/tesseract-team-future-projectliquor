import os
from invoke import task

from pathlib import Path
from zipfile import ZipFile

root_path = Path("./")
data_dir = root_path / Path("data") / "raw"

@task
def get_dataset(c):
    """Automation for the dataset getting.
    Task to automate the download and unpacking of the data.
    """
    if "Iowa_Liquor_Sales.csv" not in os.listdir(data_dir):
        c.run(
            f"kaggle datasets download -d residentmario/iowa-liquor-sales -p {data_dir}"
        )
        print("Extracting data...")
        with ZipFile(data_dir / "iowa-liquor-sales.zip", "r") as dataset_obj:
            dataset_obj.extractall(path=data_dir)
        c.run(f"rm -rf {data_dir / 'iowa-liquor-sales.zip'}")
    print("Done!")


@task
def install(c):
    """Project installation.

    Task to automate the project reinstallation. It creates the virtualenv and install the package.
    """
    if build_path := "dist" in os.listdir(root_path):
        c.run(f"rm -rf {build_path}")
    c.run("python -m build")
    c.run("pip install -e .[dev]")

