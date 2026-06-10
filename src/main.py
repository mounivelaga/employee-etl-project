import json

from extract import extract_data
from transform import transform_data
from load import load_data

with open("config.json") as file:
    config = json.load(file)

data = extract_data(config["input_file"])
df = transform_data(data)
load_data(df, config)

print("ETL pipeline completed sucessfully")
