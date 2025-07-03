# PowerShell script to run both backend and frontend

# Start backend
Start-Process powershell -ArgumentList 'cd backend; .\venv\Scripts\Activate; uvicorn main:app --reload'

# Start frontend
Start-Process powershell -ArgumentList 'npm run dev' 