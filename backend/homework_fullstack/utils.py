from typing import List
import json
import importlib.resources
import pandas as pd
import re
import os


def read_codes():
    """Load the Swiss cantons built-in code-label data."""
    codes = json.load(
        importlib.resources.open_text("homework_fullstack", "cantons.json")
    )
    return codes


def normalize_string(col: str) -> str:
    """Remove unexpected chars and lower string."""
    name = re.sub("[^a-zA-Z]+", "", col)
    return name.lower()


def to_int(value: str) -> int:
    """Clean string before parsing it to an integer."""
    return int(re.sub("[^0-9]+", "", value))


def validate_column_names(columns: List[str]) -> bool:
    """Validate that the column names contain the mandatory ones."""
    return "canton" in columns and "femmes" in columns and "hommes" in columns


def read_data(path: str):
    """Read the user data in a data.frame, drop empty columns/rows and clean headers."""
    # read CSV file into a data frame, silently ignoring char encoding errors
    cantons = pd.read_csv(
        path,
        encoding_errors="replace",
    )
    # remove empty rows and columns
    cantons = cantons.dropna(how="all").dropna(how="all", axis=1)
    # normalize column names
    cantons.columns = cantons.columns.map(normalize_string)
    # check mandatory column names
    if not validate_column_names(list(cantons.columns)):
        raise ValueError(
            "Bad column names in data file, expecting at least (ignoring case): 'canton', 'femmes', 'hommes'"
        )
    return cantons


def read_cantons():
    """Read cantons data and format as a dictionary, where keys are canton codes."""
    # read data from file
    cantons = read_data(os.getenv("DATA_DIR", "../dataset") + "/canton.csv")
    # sort alphabetically by Canton value, "should" have same order despite weird chars
    # as the built-in canton labels
    codes = pd.DataFrame.from_dict(
        read_codes(), orient="index", columns=["canton"]
    ).sort_values(by="canton")
    cantons = cantons.set_index(codes.index)
    cantons["code"] = codes.index
    cantons["canton"] = codes["canton"]
    # apply expected data types
    cantons["hommes"] = cantons["hommes"].map(to_int)
    cantons["femmes"] = cantons["femmes"].map(to_int)
    cantons = cantons.rename(
        columns={
            "canton": "title",
            "hommes": "male",
            "femmes": "female",
            "autres": "other",
        }
    )
    if "other" not in cantons:
        cantons["other"] = 0
    # silently remove useless columns
    columnsToDrop = list()
    for col in list(cantons.columns):
        if col not in ["title", "male", "female", "other", "code"]:
            columnsToDrop.append(col)
    cantons = cantons.drop(columns=columnsToDrop, errors="ignore")
    return cantons.to_dict("index")
