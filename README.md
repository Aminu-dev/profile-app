# Profile App

A small Flask web app where you can edit a personal profile (name, email, bio).
Data is stored in MongoDB, with Mongo Express as a database admin page.
Everything runs with Docker Compose.

## Tech
- Python, Flask, pymongo
- MongoDB, Mongo Express
- Docker, Docker Compose

## How to run
1. Copy the example environment file and set your own password:
   ```bash
   cp .env.example .env
   ```
2. Start everything:
   ```bash
   docker compose up --build
   ```
3. Open:
   - App: http://localhost:5000
   - Mongo Express: http://localhost:8081

## Stop
```bash
docker compose down        # keeps your data
docker compose down -v     # also deletes your data
```

## What I learned
- Running multiple containers together with Compose
- Containers talking to each other by service name
- Keeping secrets in a `.env` file that is not committed
- Persisting data with volumes