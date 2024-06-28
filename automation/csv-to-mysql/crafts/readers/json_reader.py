import json
from typing import Dict, Optional


def load_json(filename: str) -> Optional[Dict]:
    """
    Loads a JSON file and returns its contents as a dictionary.
    :param filename: The path to the JSON file.
    :return: A dictionary representation of the JSON file or None if an error occurs.
    """
    try:
        with open(filename, "r") as users_data:
            return json.load(users_data)
    except FileNotFoundError as e:
        print(f"Error reading {filename}. {e}")
        return None
