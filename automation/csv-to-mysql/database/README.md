# DayHome Database 🏡

## Overview

This tool uses the MySQL database management system (DBMS) to manage the DayHome Database. Ensure that you have MySQL installed and properly configured before proceeding🏡.

## ⬇️ Installation Guide

### Windows 💻

1. **Download MySQL**: Download MySQL from the official [MySQL Downloads](https://dev.mysql.com/downloads/) page.
2. **Install MySQL**: Run the installer and follow the instructions. Make sure to add MySQL to your path variables.
3. **Start MySQL Server**: Use the MySQL Command-Line tool. For Windows, ensure MySQL is added to your PATH. You might need to restart your command prompt or terminal.
   - **Loosen Privileges**: If you have MySQL Workbench installed, ensure the appropriate privileges are set.
4. **Create Database**:
   - Open your MySQL command line and type `CREATE DATABASE DayHomeDatabase;`.

### macOS 🍎

1. **Install Homebrew**: If not already installed, [install Homebrew](https://brew.sh/).
2. **Install MySQL**: Run `brew install mysql` in your terminal.
3. **Start MySQL Server**: Use `brew services start mysql`.
4. **Create Database**:
   - Open Terminal and connect to MySQL using `mysql -u root -p` and type `CREATE DATABASE DayHomeDatabase;`.

## 🔧 Configuration

- **Create Tables**: Navigate to the directory containing your `dayhome.sql` file and run the following command to create your tables according to the schema:
  ```bash
  mysql -u [username] -p DayHomeDatabase < ./dayhome.sql
  ```
