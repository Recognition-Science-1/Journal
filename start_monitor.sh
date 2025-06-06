#!/bin/bash
# Start the Universal Agent Monitor
# This script provides easy ways to run the monitoring system

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🚀 Recognition Science Agent Monitor"
echo "===================================="
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not found"
    echo "Please install Python 3 and try again"
    exit 1
fi

# Function to show menu
show_menu() {
    echo "Choose monitoring mode:"
    echo ""
    echo "1) 🔄 Continuous monitoring (30 second intervals)"
    echo "2) ⚡ Fast monitoring (10 second intervals)"
    echo "3) 🐌 Slow monitoring (60 second intervals)"
    echo "4) 📊 Show dashboard only"
    echo "5) 🔍 Check once and exit"
    echo "6) 🏃 Run in background (nohup)"
    echo "7) 🛑 Stop background monitor"
    echo "8) 📜 View monitor logs"
    echo "9) ❌ Exit"
    echo ""
}

# Function to start background monitor
start_background() {
    if [ -f "monitor.pid" ]; then
        PID=$(cat monitor.pid)
        if ps -p $PID > /dev/null 2>&1; then
            echo "⚠️  Monitor is already running with PID $PID"
            return
        fi
    fi
    
    echo "🚀 Starting monitor in background..."
    nohup python3 auto_monitor_all_agents.py --interval 30 > monitor.log 2>&1 &
    echo $! > monitor.pid
    echo "✅ Monitor started with PID $(cat monitor.pid)"
    echo "📜 Logs are being written to monitor.log"
    echo ""
    echo "To stop: ./start_monitor.sh and choose option 7"
}

# Function to stop background monitor
stop_background() {
    if [ -f "monitor.pid" ]; then
        PID=$(cat monitor.pid)
        if ps -p $PID > /dev/null 2>&1; then
            echo "🛑 Stopping monitor with PID $PID..."
            kill $PID
            rm monitor.pid
            echo "✅ Monitor stopped"
        else
            echo "⚠️  Monitor with PID $PID is not running"
            rm monitor.pid
        fi
    else
        echo "❌ No monitor PID file found"
    fi
}

# Function to view logs
view_logs() {
    if [ -f "monitor.log" ]; then
        echo "📜 Last 50 lines of monitor.log:"
        echo "================================"
        tail -n 50 monitor.log
        echo ""
        echo "Press Enter to continue..."
        read
    else
        echo "❌ No log file found"
    fi
}

# Main menu loop
while true; do
    show_menu
    read -p "Enter your choice (1-9): " choice
    
    case $choice in
        1)
            echo "🔄 Starting continuous monitoring (30s intervals)..."
            python3 auto_monitor_all_agents.py --interval 30
            ;;
        2)
            echo "⚡ Starting fast monitoring (10s intervals)..."
            python3 auto_monitor_all_agents.py --interval 10
            ;;
        3)
            echo "🐌 Starting slow monitoring (60s intervals)..."
            python3 auto_monitor_all_agents.py --interval 60
            ;;
        4)
            echo "📊 Showing dashboard..."
            python3 auto_monitor_all_agents.py --dashboard
            echo ""
            echo "Press Enter to continue..."
            read
            ;;
        5)
            echo "🔍 Checking once..."
            python3 auto_monitor_all_agents.py --once
            echo ""
            echo "Press Enter to continue..."
            read
            ;;
        6)
            start_background
            echo "Press Enter to continue..."
            read
            ;;
        7)
            stop_background
            echo "Press Enter to continue..."
            read
            ;;
        8)
            view_logs
            ;;
        9)
            echo "👋 Exiting..."
            exit 0
            ;;
        *)
            echo "❌ Invalid choice. Please try again."
            echo ""
            ;;
    esac
done 