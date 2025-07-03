# FastAPI Backend

## Setup

1. Create and activate a virtual environment (if not already):
   ```sh
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Mac/Linux
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the server:
   ```sh
   uvicorn main:app --reload
   ```

## API Endpoints

- `POST /signup` — Register a new user (email, password)
- `POST /login` — Login and get JWT token (OAuth2)
- `GET /me` — Get current user info (requires Bearer token)

The database is stored in `users.db` (SQLite). 