from exporters.csv_exporter import MonthlyCalendar
from database.my_sql_database import MySQLDatabase
from database.my_sql_helper import query_for_daily_entry

def export_database(filename: str, year: int, month: int) -> None:
    my_database = MySQLDatabase()
    my_calendar = MonthlyCalendar(year, month)
    my_calendar.generate_calendar()

    # my_calendar.populate_calendar()
    # my_calendar.print_calendar()