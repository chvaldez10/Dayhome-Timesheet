import pandas as pd

# Define your month and year
year = 2024
month = 1

# Create a date range for the entire month
# The start is the first of the month
start_date = f"{year}-{month:02d}-01"
# The end is the start date plus one month, minus one day
end_date = pd.to_datetime(start_date) + pd.offsets.MonthEnd(0)

date_range = pd.date_range(start=start_date, end=end_date)

# Find out the day of the week for the first day of the month
start_day_of_week = date_range[0].dayofweek

# Initialize an empty DataFrame
# The DataFrame has the number of rows depending on the number of days and start day
num_days = len(date_range)
num_weeks = (start_day_of_week + num_days - 1) // 7 + 1
calendar_df = pd.DataFrame(index=range(1, num_weeks + 1),
                           columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Populate the DataFrame with the actual dates
for date in date_range:
    # Calculate the week number
    week_of_month = (date.day + start_day_of_week - 1) // 7 + 1
    # Get the day name
    day_of_week = date.strftime('%A')
    # Insert the date into the DataFrame
    calendar_df.at[week_of_month, day_of_week] = date.strftime('%m/%d')

# Replace NaN values with empty strings or some placeholder
calendar_df = calendar_df.fillna('')

# Export to CSV
calendar_csv_path = 'calendar.csv'
calendar_df.to_csv(calendar_csv_path)

print(f"Calendar CSV has been created at: {calendar_csv_path}")
