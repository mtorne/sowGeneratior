#!/bin/bash

# Backend
cd /home/ubuntu/labs/sowGenGit/backend
source venv/bin/activate
nohup uvicorn main:app --reload --host 0.0.0.0  --port 8000 > uvicorn.log 2>&1 &
echo $! > uvicorn.pid
echo "Servidor backend (FastAPI) arrancat (PID $(cat uvicorn.pid))"

# Frontend
cd /home/ubuntu/labs/sowGenGit/frontend
nohup npm start > frontend.log 2>&1 &
echo $! > frontend.pid
echo "Servidor frontend (React) arrancat (PID $(cat frontend.pid))"

