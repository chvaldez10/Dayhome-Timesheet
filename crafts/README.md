📁 The scripts in this folder are specifically designed for CSV file extracts from the web application named `Crafts Web App`. The workflow outlined is tailored uniquely for the `Crafts Web App` usage. 🌐

📋 **Step 1**: Please _copy_ and _paste_ all CSV files into the `csv` folder.

✏️ **Step 2**: Rename all files using the date format `yyyy-mm-dd`.

🔧 **Step 3**: To utilize the script, ensure to download the required packages listed in `requirements.txt`. Execute the command `pip install -r requirements.txt`.

📝 **Step 4**: Create a `.env` file containing the essential environment variables:

```
DATABASE_NAME="DayHomeDatabase"
DATABASE_USER="root"
DATABASE_PASSWORD="password"
DATABASE_HOST="localhost"
DATABASE_PORT="3306"
EMAIL_SENDER="sender@example.com"
EMAIL_PASSWORD="aaaa bbbb cccc ddd"
EMAIL_RECEIVER="receiver@example.com"
```

🗂️ **Step 5**: Create a `users.json` in the `json` folder to list the currently enrolled students in the dayhome.

```
{
  "child first and last name": "children.id",
}
```

🗂️ **Step 6**: Populate the MySQL database by following the schema under `..\database\dayhome.sql`.

🚀 **Running the Script**: Use the following python command to execute the script `main.py <provider_id> [-v] [-p] [-s SUMMARY] [-e EXPORT]`.

### Options:

    -e, --export:          export data to a CSV file (requires an additional argument)
    -p, --populate:        populate the database with data
    -s, --summary:         summarize monthly data (requires an additional argument)
    -v, --version:         print the script's version
