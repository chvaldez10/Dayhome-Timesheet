from database.my_sql_database import MySQLDatabase
from readers.json_reader import load_json
from database.my_sql_helper import query_for_daily_total

# json data
USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

def summarize_month(provider_id:str, year: int, month: int, day:int) -> None:
    summarize_day("Me", provider_id, year, month, day, "ProviderLog", "ProviderID")
    for user, user_id in USER_ID_MAP.items():
        summarize_day(user, user_id, year, month, day, "DailyLog", "ChildrenID")
    

def summarize_day(user: str, user_id: str, year: int, month: int, day:int, table_name: str, id_name: str) -> None:
    my_database = MySQLDatabase()
    daily_entry = query_for_daily_total(my_database, user_id, year, month, day, table_name, id_name)
    
    if daily_entry:
        time = daily_entry[0][0]
        print(f"{user}: {time} h")