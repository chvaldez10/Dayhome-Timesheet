from database.my_sql_database import MySQLDatabase
from readers.json_reader import load_json

# json data
USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

def summarize_month(provider_id:str, year: int, month: int) -> None:
    pass