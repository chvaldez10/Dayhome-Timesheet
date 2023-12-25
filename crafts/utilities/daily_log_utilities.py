import pandas as pd
from datetime import datetime

def generate_provider_log(daily_log_df: pd.DataFrame):
    date_entry = daily_log_df.iloc[0]["Date Entry"]
    min_in_time = daily_log_df["In Time"].dropna().min()
    max_out_time = daily_log_df["Out Time"].dropna().max()
    total_time = (datetime.combine(datetime.min, max_out_time) - datetime.combine(datetime.min, min_in_time)).seconds/3600
    print(date_entry, min_in_time, max_out_time, total_time)
