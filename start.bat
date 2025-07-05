@echo off
echo Starting CodeTech Learning Platform...
echo.

echo Starting Backend Server...
cd backend
start "Backend Server" cmd /k "python main.py"

echo.
echo Starting Frontend Server...
cd ..
start "Frontend Server" cmd /k "npm run dev"

echo.
echo Both servers are starting...
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Admin Login: AdminIbra@gmail.com / IbraGold@1
echo Student Login: student@alu.edu / password123
echo.
pause 