import pandas as pd
from logger import logger


def transform_data(data):
    logger.info("Transformation Started")

    df = pd.json_normalize(data)

    required_columns = ["employee_id", "name", "department", "salary", "location"]
    print("Columns in DataFrame:", df.columns.tolist())

    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"{col} column missing")

    df["salary"] = df["salary"].fillna(0)

    df["name"] = df["name"].str.title()

    logger.info("Transformation completed.")

    return df
