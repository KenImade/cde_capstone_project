import pandas as pd
import pathlib
import logging


def _process_data(**kwargs):
    """
    Writes a nested JSON object to a Parquet file.
    """
    params = kwargs['params']
    input_file_path = f"{params['raw_data_path']}/countries.json"
    output_directory = params['processed_data_path']
    output_file_path = f"{params['processed_data_path']}/countries.parquet"
    url = params['api_url']

    # Ensure directory  exists
    pathlib.Path(output_directory).mkdir(parents=True, exist_ok=True)

    try:
        normalized_data = pd.json_normalize(input_file_path)
    except AttributeError:
        logging.error("Invalid JSON format")

    normalized_data.to_parquet(output_file_path, engine='pyarrow', index=False)
    print(f"Data has been successfully written to {output_file_path}")
