import os
import sys
import zipfile

# Referenced from https://github.com/ttimbers/breast_cancer_predictor_py/blob/main/tests/test_read_zip.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.download_unpack_zip_extract_csv import download_unpack_zip_extract_csv
import pandas as pd
import pytest


# Test: Check for valid input types
def test_input_types():
    with pytest.raises(TypeError):
        download_unpack_zip_extract_csv("string", 37)
    with pytest.raises(TypeError):
        download_unpack_zip_extract_csv(["hello"], "string")


# Test: Check if url input string is a valid URL
def test_url_exists():
    with pytest.raises(NameError):
        download_unpack_zip_extract_csv("my_string?", "string")


# Test: Check if url downloads a valid zip file
def test_url_valid():
    with pytest.raises(zipfile.BadZipFile):
        download_unpack_zip_extract_csv(
            "https://raw.githubusercontent.com/UBC-MDS/fifa-potential/main/tests/test_data/not_a_zip_file.md",
            "string",
        )


# Test: Check if filename inside zip is correct
def test_csv_in_zip():
    with pytest.raises(KeyError):
        download_unpack_zip_extract_csv(
            "https://github.com/UBC-MDS/fifa-potential/raw/main/tests/test_data/this_is_a_zip_file.zip",
            "string",
        )


# Test: Check if downloaded csv is valid
def test_csv_valid():
    assert download_unpack_zip_extract_csv(
        "https://github.com/UBC-MDS/fifa-potential/raw/main/tests/test_data/this_is_a_zip_file.zip",
        "this_is_a_csv_file.csv",
    ).equals(
        pd.read_csv(
            os.path.join(
                os.path.dirname(__file__), "test_data", "this_is_a_csv_file.csv"
            )
        )
    )


def test_cleanup():
    os.remove(os.path.join("data", "this_is_a_csv_file.csv"))
