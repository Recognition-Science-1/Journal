#!/usr/bin/env python3
"""
Agent Notifier - Desktop notifications for Agent updates
Works on macOS to show system notifications
"""

import os
import subprocess
import time
from datetime import datetime

def send_notification(title, message):
    """Send a macOS notification."""
    # Use osascript for macOS notifications
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(['osascript', '-e', script])

def check_and_notify():
    """Check for updates and send notifications."""
    print(f"🔔 Agent Notifier Active - {datetime.now().strftime('%H:%M:%S')}")
    
    # Check for messages
    message_dir = "MESSAGES/A_TO_B"
    if os.path.exists(message_dir):
        messages = os.listdir(message_dir)
        if messages:
            send_notification(
                "📨 New Message from Agent A!",
                f"Found {len(messages)} message(s) - Check MESSAGES/A_TO_B/"
            )
            print(f"✅ Notified: {len(messages)} new message(s)")
            return True
    
    # Check if Agent A status was updated recently
    status_file = "AGENT_A_STATUS.md"
    if os.path.exists(status_file):
        # Check file modification time
        mod_time = os.path.getmtime(status_file)
        current_time = time.time()
        # If modified in last 5 minutes
        if (current_time - mod_time) < 300:
            send_notification(
                "📋 Agent A Status Updated",
                "Agent A has updated their status - check AGENT_A_STATUS.md"
            )
            print("✅ Notified: Agent A status updated")
            return True
    
    print("💤 No new updates to notify")
    return False

if __name__ == "__main__":
    # Quick notification check
    check_and_notify()
    
    print("\nTo run continuous monitoring with notifications:")
    print("  python3 check_agent_updates.py")
    print("\nNotifications will appear when Agent A sends updates!") 