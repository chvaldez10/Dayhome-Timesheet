from utilities.calendar_df_utilities import export_user_data
from readers.json_reader import load_json

# json data
USER_FILENAME = "./json/users.json"
USER_ID_MAP = load_json(USER_FILENAME)

def export_database(provider_id: str, year: int, month: int) -> None:
    """
    Export database records for users and a provider to CSV files.
    """
    for user, user_id in USER_ID_MAP.items():
        export_user_data(user, user_id, year, month, "DailyLog", "ChildrenID", True)

    export_user_data("Provider", provider_id, year, month, "ProviderLog", "ProviderID", True)