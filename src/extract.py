import json
from logger import logger


def extract_data(file_path):
    logger.info("Extraction Started")

    with open(file_path, "r") as file:
        data = json.load(file)
    logger.info("Extraction Completed")

    return data
