"""Module providing a function to process JSON data to Parquet"""
import pandas as pd
import pathlib
import json
import logging


def _process_data(**kwargs):
    """
    Writes a nested JSON object to a Parquet file.
    """
    params = kwargs['params']
    input_file_path = f"{params['raw_data_path']}/countries.json"
    output_directory = params['processed_data_path']
    output_file_path = f"{params['processed_data_path']}/countries.parquet"

    # Ensure directory  exists
    pathlib.Path(output_directory).mkdir(parents=True, exist_ok=True)

    try:
        with open(input_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        normalized_data = pd.json_normalize(data)
        normalized_data.to_parquet(output_file_path, engine='pyarrow', index=False)
        logging.info("Data has been successfully written to %s", output_file_path)
        print(f"Data has been successfully written to {output_file_path}")
    except FileNotFoundError:
        logging.error("Input file %s not found.", input_file_path)
    except json.JSONDecodeError:
        logging.error("Invalid JSON format in file: %s", input_file_path)
