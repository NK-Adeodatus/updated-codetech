#!/bin/zsh

# Ensure the database and tables exist
python3 backend/init_db.py

# Start backend in the background
(cd backend && source venv/bin/activate && uvicorn main:app --reload) &

# Start frontend in the background
(npm run dev) & 