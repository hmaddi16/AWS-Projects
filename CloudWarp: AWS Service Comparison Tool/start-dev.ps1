# AWS Service Comparison Tool - Development Startup Script
# This script starts both the backend and frontend servers

Write-Host "Starting AWS Service Comparison Tool..." -ForegroundColor Green
Write-Host "=====================================" -ForegroundColor Green

# Start backend server
Write-Host "`nStarting backend server..." -ForegroundColor Yellow
Start-Process -FilePath "powershell" -ArgumentList "-Command", "cd backend; python main.py" -WindowStyle Normal

# Wait a moment for backend to start
Start-Sleep -Seconds 3

# Start frontend server
Write-Host "Starting frontend server..." -ForegroundColor Yellow
Start-Process -FilePath "powershell" -ArgumentList "-Command", "cd frontend; npm start" -WindowStyle Normal

Write-Host "`nBoth servers are starting..." -ForegroundColor Green
Write-Host "Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend App: http://localhost:3000" -ForegroundColor Cyan
Write-Host "API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host "`nPress any key to continue..." -ForegroundColor Gray
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
