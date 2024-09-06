# Dayhome-Timesheet 📅🖥️

Welcome to the Dayhome-server repo! We're building a cool tool to complement the Crafts Web App, starting with a mocked local database. Our long-term goal? Turning this into a standalone app with some awesome features:

- Document signing (PDF)
- Custom timesheet templates
- Dayhome AI assistant
- more to come...

Check out the frontend repo here: [Dayhome-client](https://github.com/chvaldez10/Dayhome-client.git)

## 🌐 Crafts Web App - Dayhome Management Tool

The Crafts Web App is a solid dayhome management platform. It's got timesheet management, but it's missing a big-picture view of all that data. That's where we come in!

## ⚙️ Development Phases

### Phase 1: ETL and Automation (Done and dusted!)

- **Goal**: Automate data handling and set up a local MySQL database.
- **What we did**:
  - Used Cypress to grab data from CSV files.
  - Wrote scripts to fill up the MySQL database.
  - Set up recurring database updates.
- **Notes**:
  - We're not planning to improve this phase's code - we're moving on to new tools and frameworks.
  - We'll be switching from MySQL to PostgreSQL soon.

### Phase 2: Django Server and Next.js Client (In the works)

- **Goal**: Get a Django server and Next.js client up and running.
- **To-do list**:
  - Build the Next.js client and Django server.
  - Move data from MySQL to PostgreSQL.
  - Say goodbye to MySQL.

### Phase 3: Deployment (Coming up next)

- **Goal**: Get this baby live on a cloud service.
- **Game plan**:
  - Deploy both the Django server and Next.js client.
  - Set up a production database (probably using Supabase).

### Our Tech Stack

- **Frontend**: Next.js, Chakra UI, Cypress
- **Backend**: Django, Django Ninja
- **Database**: MySQL (for now), PostgreSQL (coming soon)
- **Deployment**: Vercel, Supabase (probably)
- **Other tools**: Git, GitHub, Postman, Docker (maybe)
- **Why these choices?**
  - We're using Django Ninja and Chakra UI to speed things up compared to Django REST Framework and Tailwind CSS.
