import os
import requests
import zipfile

import pandas as pd


def download_unpack_zip_extract_csv(url, filename, path="data"):
    """
    download, unzip and unpack source data

    Parameters
    ----------
    url : string
        a string corresponding to a URL of a zip folder, the target returning a zip folder
    filename : string
        a string corresponding to the `.csv` file desired for analysis
    path : string
        a string corresponding to the zip file path for target filename
    Returns
    -------
    pandas.DataFrame
        a Pandas DataFrame corresponding to the `.csv` file within a zip folder

    """

    # Test: Check for valid input types
    if not isinstance(url, str):
        raise TypeError("Input `url` must be type string")
    if not isinstance(filename, str):
        raise TypeError("Input `filename` must be type string")

    try: 
        request = requests.get(url)
    except: 
        raise NameError("Input `url` is not a valid URL")

    # Test: Check if url input string is a valid URL
    if request.status_code != 200:
        raise NameError("Input `url` is not a valid URL")

    with open(os.path.join("data", "tmp.zip"), "wb") as f:
        f.write(request.content)

    # Test: Check if url downloads a valid zip file
    with zipfile.ZipFile(os.path.join("data", "tmp.zip"), "r") as zip_file:
        if zip_file.testzip() is not None:
            raise TypeError("Zip file is not valid")

    # Test: Ensure target filename is extracted successfully
    try:
        with zipfile.ZipFile(os.path.join("data", "tmp.zip"), "r") as zip_file:
            zip_file.extract(filename, path=path)
        os.remove(os.path.join(path, "tmp.zip"))
    except:
        raise ValueError("Target csv not found within zip file")

    return pd.read_csv(os.path.join(path, filename), encoding="utf-8", low_memory=False)
