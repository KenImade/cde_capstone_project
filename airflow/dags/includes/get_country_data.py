"""Module providing a function to fectch JSON data from the Country REST API"""
import pathlib
import json
import logging
import requests


def get_country_data(**kwargs):
    """
    Fetches country data from the Country REST API
    """
    params = kwargs['params']
    directory_path = params['raw_data_path']
    file_path = f"{directory_path}/countries.json"
    url = params['api_url']

    # Ensure directory exists
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        json_data = response.json()

        with open(file_path, 'w', encoding="utf-8") as file:
            json.dump(json_data, file)
        logging.info("Data fetched and saved to %s", file_path)
    except requests.exceptions.RequestException as error:
        logging.error("Error fetching data from API: %s", error)
        raise
    except IOError as error:
        logging.error("Error saving JSON file: %s", error)
        raise
