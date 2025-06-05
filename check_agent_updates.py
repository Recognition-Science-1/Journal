#!/usr/bin/env python3
"""
Agent Update Checker - Monitors for updates from Agent A
Runs continuously and checks for:
- New messages in MESSAGES/A_TO_B/
- Updates to AGENT_A_STATUS.md
- New git commits from Agent A
"""

import os
import time
import subprocess
from datetime import datetime
import hashlib

def run_command(cmd):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except:
        return None

def get_file_hash(filepath):
    """Get MD5 hash of a file to detect changes."""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def check_for_updates():
    """Check for any updates from Agent A."""
    updates = []
    
    # 1. Pull latest from git
    print("📥 Pulling latest changes...")
    git_output = run_command("git pull origin main")
    if git_output and "Already up to date" not in git_output:
        updates.append(f"🔄 Git updated: {git_output}")
    
    # 2. Check for new messages from Agent A
    message_dir = "MESSAGES/A_TO_B"
    if os.path.exists(message_dir):
        messages = os.listdir(message_dir)
        if messages:
            updates.append(f"📨 Found {len(messages)} message(s) from Agent A!")
            for msg in messages:
                print(f"   - {msg}")
                # Read and display the message
                with open(os.path.join(message_dir, msg), 'r') as f:
                    content = f.read()
                    print(f"\n--- Message Content ---\n{content}\n--- End Message ---\n")
    
    # 3. Check Agent A's status
    status_file = "AGENT_A_STATUS.md"
    if os.path.exists(status_file):
        with open(status_file, 'r') as f:
            status_content = f.read()
            if "Last Updated" in status_content:
                # Extract last update time
                for line in status_content.split('\n'):
                    if "Last Updated" in line:
                        updates.append(f"📋 Agent A Status: {line}")
                        break
    
    # 4. Check recent commits
    recent_commits = run_command("git log --oneline -5 --grep='Agent A'")
    if recent_commits:
        updates.append("📝 Recent Agent A commits:")
        print(recent_commits)
    
    return updates

def monitor_continuously(check_interval=60):
    """Monitor for updates continuously."""
    print("🤖 Agent B Update Monitor Started")
    print(f"⏰ Checking every {check_interval} seconds")
    print("Press Ctrl+C to stop\n")
    
    # Store hashes to detect changes
    last_status_hash = get_file_hash("AGENT_A_STATUS.md")
    last_message_count = len(os.listdir("MESSAGES/A_TO_B")) if os.path.exists("MESSAGES/A_TO_B") else 0
    
    while True:
        try:
            print(f"\n🔍 Checking for updates... [{datetime.now().strftime('%H:%M:%S')}]")
            
            # Check for updates
            updates = check_for_updates()
            
            # Check if Agent A status changed
            current_status_hash = get_file_hash("AGENT_A_STATUS.md")
            if current_status_hash != last_status_hash:
                print("🆕 Agent A status file updated!")
                last_status_hash = current_status_hash
            
            # Check for new messages
            current_message_count = len(os.listdir("MESSAGES/A_TO_B")) if os.path.exists("MESSAGES/A_TO_B") else 0
            if current_message_count > last_message_count:
                print(f"🎉 {current_message_count - last_message_count} new message(s) from Agent A!")
                last_message_count = current_message_count
            
            if updates:
                print("\n✅ Updates found:")
                for update in updates:
                    print(f"  {update}")
            else:
                print("💤 No new updates")
            
            # Wait before next check
            print(f"\n⏳ Next check in {check_interval} seconds...")
            time.sleep(check_interval)
            
        except KeyboardInterrupt:
            print("\n\n👋 Update monitor stopped by user")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(check_interval)

def quick_check():
    """Do a single check for updates."""
    print("🔍 Quick check for Agent A updates...\n")
    updates = check_for_updates()
    
    if updates:
        print("✅ Found updates:")
        for update in updates:
            print(f"  {update}")
    else:
        print("💤 No new updates from Agent A")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--once":
        # Just check once
        quick_check()
    else:
        # Monitor continuously
        monitor_continuously(check_interval=30)  # Check every 30 seconds 