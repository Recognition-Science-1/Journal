#!/bin/bash
# Agent A Update Monitor - Automatic checker for Agent B

echo "🤖 AGENT A UPDATE MONITOR"
echo "========================"
echo ""

# Function to check for updates
check_updates() {
    echo "🔍 Checking for Agent A updates... [$(date +%H:%M:%S)]"
    
    # Pull latest changes
    echo "📥 Pulling from git..."
    git pull origin main | grep -v "Already up to date" && echo "✅ New changes pulled!"
    
    # Check for messages
    if [ -d "MESSAGES/A_TO_B" ]; then
        message_count=$(ls MESSAGES/A_TO_B/ 2>/dev/null | wc -l)
        if [ $message_count -gt 0 ]; then
            echo "📨 Found $message_count message(s) from Agent A:"
            ls -la MESSAGES/A_TO_B/
            echo ""
            # Show latest message
            latest_msg=$(ls -t MESSAGES/A_TO_B/ | head -1)
            if [ ! -z "$latest_msg" ]; then
                echo "📄 Latest message:"
                echo "---"
                cat "MESSAGES/A_TO_B/$latest_msg"
                echo "---"
            fi
        fi
    fi
    
    # Check Agent A status
    if [ -f "AGENT_A_STATUS.md" ]; then
        echo ""
        echo "📋 Agent A Status:"
        grep -E "(Last Updated|Current Focus)" AGENT_A_STATUS.md | head -2
    fi
    
    echo ""
}

# Single check mode
if [ "$1" == "--once" ]; then
    check_updates
    exit 0
fi

# Continuous monitoring mode
echo "⏰ Monitoring every 30 seconds (Press Ctrl+C to stop)"
echo ""

while true; do
    check_updates
    echo "⏳ Next check in 30 seconds..."
    echo "================================"
    sleep 30
done 