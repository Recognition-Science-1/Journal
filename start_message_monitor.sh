#!/bin/bash
# Start the automatic message monitor for Agent A

echo "🚀 Starting Agent A Message Monitor..."
echo "===================================="
echo

# Check if we're in the right directory
if [[ ! "$PWD" == *"/Journal"* ]]; then
    echo "⚠️  Warning: Not in Journal directory!"
    echo "Switching to /Users/emmatully/Desktop/Journal..."
    cd /Users/emmatully/Desktop/Journal
fi

# Make the Python script executable
chmod +x auto_message_checker.py

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

echo "📊 Monitor Options:"
echo "1) Run in foreground (see all messages)"
echo "2) Run in background (silent mode)"
echo "3) Run once and exit"
echo
read -p "Choose option (1-3): " choice

case $choice in
    1)
        echo "Starting monitor in foreground..."
        echo "Press Ctrl+C to stop"
        python3 auto_message_checker.py
        ;;
    2)
        echo "Starting monitor in background..."
        nohup python3 auto_message_checker.py > message_monitor.log 2>&1 &
        PID=$!
        echo "✅ Monitor started with PID: $PID"
        echo "📝 Logs: tail -f message_monitor.log"
        echo "🛑 To stop: kill $PID"
        # Save PID for easy stopping later
        echo $PID > .message_monitor.pid
        ;;
    3)
        echo "Running single check..."
        python3 -c "
import sys
sys.path.append('.')
from auto_message_checker import check_for_new_messages, display_new_message, MESSAGE_DIR
print('🔍 Checking for messages in:', MESSAGE_DIR)
messages = check_for_new_messages()
if messages:
    print(f'📬 Found {len(messages)} new message(s)!')
    for msg in messages:
        display_new_message(msg)
else:
    print('📭 No new messages.')
"
        ;;
    *)
        echo "Invalid option. Exiting."
        exit 1
        ;;
esac 