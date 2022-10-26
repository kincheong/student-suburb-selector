
import os
import pandas as pd
from ast import literal_eval as make_tuple  # parse tuple stored in csv files


DATA_PATH = os.path.join(os.getcwd(), "../data/")
RAW_DATA_PATH = os.path.join(DATA_PATH, "raw")
DERIVED_DATA_PATH = os.path.join(DATA_PATH, "derived")


def getSuburbsMetadata(type="derived"):
    if type.lower() in ["derived", "d", "clean", "c"]:
        FILE_PATH = os.path.join(DERIVED_DATA_PATH, "SuburbMetadata.csv")
    elif type.lower() in ["raw", "r", "original", "o"]:
        FILE_PATH = os.path.join(RAW_DATA_PATH, "australian_postcodes.csv")
    else:
        raise ValueError(f"Type '{type}' is not recognised.")
    # read file
    localities_details_df = pd.read_csv(FILE_PATH)
    # filter for victorian localities: postcode starts with '3'
    localities_details_df = localities_details_df[localities_details_df["postcode"].astype(str).str.contains("^3[0-9]{3}")]
    # make locality and lga title case
    localities_details_df["locality"] = localities_details_df["locality"].str.title()
    localities_details_df["lgaregion"] = localities_details_df["lgaregion"].str.title()
    # drop areas with duplicate locality names
    localities_details_df = localities_details_df.drop_duplicates("locality")
    # convert coordinates column into tuple
    if type.lower() in ["derived", "d", "clean", "c"]:
        localities_details_df["coordinates"] = localities_details_df["coordinates"].apply(make_tuple)

    return localities_details_df


def getSuburbData():
    return pd.read_csv(os.path.join(DERIVED_DATA_PATH, "SuburbData.csv"))


def getPreferenceData():
    return pd.read_csv(os.path.join(DERIVED_DATA_PATH, "GeneratedPreferences.csv"))


def getTrainingData():
    return pd.read_csv(os.path.join(DERIVED_DATA_PATH, "TrainingData.csv"))


def main():
    print(getSuburbsMetadata())


if __name__ == "__main__":
    main()
