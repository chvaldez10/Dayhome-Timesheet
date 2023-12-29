from database.my_sql_queries import insert_data, read_data
from readers.json_reader import load_json

# python packages
import pandas as pd
from typing import Tuple, List

# json data
USER_FILENAME = "./json/users.json"
USERNAMES = load_json(USER_FILENAME)


def insert_to_daily_log_table(provider_log_df: pd.DataFrame, column_names: List[str]) -> None:
    for index, row in provider_log_df.iterrows():
        data_to_insert = tuple(row[column_name] for column_name in column_names)
        insert_data(data_to_insert)
        break
