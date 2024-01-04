from exporters.csv_exporter import MonthlyCalendar

def export_database(filename: str, year: int, month: int) -> None:
    my_calendar = MonthlyCalendar(year, month)
    my_calendar.generate_calendar()
    my_calendar.populate_calendar()
    my_calendar.print_calendar()