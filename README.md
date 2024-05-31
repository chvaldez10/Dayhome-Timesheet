# Dayhome-Timesheet 📅🖥️

Welcome to the Dayhome-Timesheet repository, a specialized tool designed to complement the Crafts Web App.

## 🌐 Crafts Web App - Dayhome Management Tool

The Crafts Web App is a robust dayhome management platform. While it includes a timesheet management system, it lacks a comprehensive aggregated data display. The Dayhome-Timesheet tool aims to fill this gap.

## ⚙️ Development Phases

### Phase 1 (ETL Tool)

- **Objective**: Automate data handling.
- **Description**: Focus on migrating CSV data to a local MySQL server.
- **Actions**:
  - Extract data from CSV files.
  - Populate the local database.
  - Aggregate data to enhance and automate timesheet processes.

### Phase 2 (On Deck)

- **Objective**: Migrate data to a cloud service and create a Django server.
- **Description**: Aim to migrate all local data to a cloud service like Supabase for multi-machine accessibility.
- **Actions**:
  - Replicate the MySQL database to Supabase.
  - Create a Django server.

### Phase 3 (On Deck)

- **Objective**: Improve user experience and accessibility.
- **Description**: Focus on developing a user-friendly web interface.
- **Actions**:
  - Create a client-facing web application using Next.js and Chakra UI.
  - Present results in an intuitive, user-friendly interface.
