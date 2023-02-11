from typing import List
import json
import importlib.resources
import pandas as pd
import re


def read_codes():
    """Load the Swiss cantons built-in code-label data."""
    codes = json.load(
        importlib.resources.open_text("homework_fullstack", "cantons.json")
    )
    return codes


def normalize_string(col: str) -> str:
    """Remove unexpected chars and capitalize string."""
    name = re.sub("[^0-9a-zA-Z]+", "", col)
    return name.lower().capitalize()


def to_int(value: str) -> int:
    """Clean string before parsing it to an integer."""
    return int(re.sub("[^0-9]+", "", value))


def validate_column_names(columns: List[str]) -> bool:
    """Validate that the column names contain the expected ones."""
    return (
        "Canton" in columns
        and "Etrangers" in columns
        and "Femmes" in columns
        and "Hommes" in columns
        and "Suisses" in columns
    )


def read_data(path: str):
    """Read the user data in a data.frame and try to clean headers and values."""
    # read CSV file into a data frame, silently ignoring char encoding errors
    cantons = pd.read_csv(
        path,
        encoding_errors="replace",
    )
    # remove empty rows and columns
    cantons = cantons.dropna(how="all").dropna(how="all", axis=1)
    # normalize column names
    cantons.columns = cantons.columns.map(normalize_string)
    # sort alphabetically by Canton value, even with weird chars "should" have same order
    # as the built-in canton labels
    codes = pd.DataFrame.from_dict(
        read_codes(), orient="index", columns=["Canton"]
    ).sort_values(by="Canton")
    cantons = cantons.set_index(codes.index)
    cantons["Canton"] = codes["Canton"]
    # apply expected data types
    cantons["Hommes"] = cantons["Hommes"].map(to_int)
    cantons["Femmes"] = cantons["Femmes"].map(to_int)
    cantons["Suisses"] = cantons["Suisses"].map(to_int)
    cantons["Etrangers"] = cantons["Etrangers"].map(to_int)
    return cantons
