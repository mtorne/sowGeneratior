#!/bin/bash

stop_process() {
    PID_FILE=$1
    NAME=$2

    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        echo "Aturant $NAME (PID $PID)..."

        # Troba el PGID (Process Group ID) del procés
        PGID=$(ps -o pgid= -p "$PID" | tr -d ' ')

        if [ -n "$PGID" ]; then
            echo "Matant el grup de processos amb PGID $PGID..."
            kill -TERM -"$PGID"
            sleep 3
            if ps -p "$PID" > /dev/null; then
                echo "$NAME encara viu, forçant kill -9 al grup de processos..."
                kill -9 -"$PGID"
            else
                echo "$NAME aturat correctament."
            fi
        else
            echo "No s'ha trobat PGID, matant només el PID..."
            kill "$PID"
        fi

        rm -f "$PID_FILE"
    else
        echo "No s'ha trobat el fitxer PID per $NAME"
    fi
}

stop_process "/home/ubuntu/labs/sowGenGit/backend/uvicorn.pid" "Backend (uvicorn)"
stop_process "/home/ubuntu/labs/sowGenGit/frontend/frontend.pid" "Frontend (React)"

