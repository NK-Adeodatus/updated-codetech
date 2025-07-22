#!/bin/zsh

# Activate the virtual environment
source backend/venv/bin/activate

# Start backend in the background
(cd backend && uvicorn main:app --reload) &

# Start frontend in the background
(npm run dev) & 