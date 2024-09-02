# Dayhome-Timesheet 📅🖥️

Welcome to the Dayhome-Timesheet repository, a specialized tool designed to complement the Crafts Web App.

## 🌐 Crafts Web App - Dayhome Management Tool

The Crafts Web App is a robust dayhome management platform. While it includes a timesheet management system, it lacks a comprehensive aggregated data display. The Dayhome-Timesheet tool aims to fill this gap.

## ⚙️ Development Phases

### Phase 1: ETL and Automation (Completed)

- **Objective**: The first phase of the project focuses on automating the data handling process. This results in a mocked local database using MySQL.
- **Steps**:
  - Used Cypress to automate the extraction of data from CSV files.
  - Created scripts to populate the local MySQL database.
  - Populated the local database on a recurring basis.

### Phase 2: Django Server and Next.js Client (In Progress)

- **Objective**: Create a Django server and a Next.js client.
- **Actions**:
  - Create a Next.js client and Django server.
  - Copy MySQL data to PostgreSQL.
  - Deprecate MySQL.

### Phase 3: Deployment (On Deck)

- **Objective**: Deploy the application to a cloud service.
- **Actions**:
  - Deploy Django server and Next.js client.
  - Create production copy of database using a predetermined database provider (likely Supabase).
