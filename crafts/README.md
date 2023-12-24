📁 The scripts in this folder expect CSV file extracts from the web application named `Crafts Web App`. The workflow described below is specifically tailored for the `Crafts Web App`. 🌐

📋 Please copy and paste all CSV files into the `csv` folder.

✏️ Rename all files in the date format `yyyy-mm-dd`.

### Scripts:

- `populate.py`: 🚀 Main script for operating the database.
- `my_sql_database.py`: 💾 Contains the MySQL database class to establish a connection with the MySQL database.
- `csv_reader.py`: 📚 Contains the CSV Reader class to read CSV files.

📝 Note: Create a `.env` file in the format below:

```
DATABASE_NAME="DayHomeDatabase"
DATABASE_USER="root"
DATABASE_PASSWORD="password"
DATABASE_HOST="localhost"
DATABASE_PORT="3306"
```
