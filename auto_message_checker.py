#!/usr/bin/env python3
"""
Automatic Message Checker for Agent A
Continuously monitors for new messages from Agent B
"""

import os
import time
import hashlib
from datetime import datetime
from pathlib import Path

# Configuration
MESSAGE_DIR = Path("/Users/emmatully/Desktop/Journal/MESSAGES/B_TO_A")
CHECK_INTERVAL = 30  # Check every 30 seconds
SEEN_MESSAGES_FILE = Path("/Users/emmatully/Desktop/Journal/.seen_messages")

def get_file_hash(filepath):
    """Get hash of file content to detect changes"""
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def load_seen_messages():
    """Load set of already seen message hashes"""
    if SEEN_MESSAGES_FILE.exists():
        with open(SEEN_MESSAGES_FILE, 'r') as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_seen_messages(seen):
    """Save seen message hashes"""
    with open(SEEN_MESSAGES_FILE, 'w') as f:
        for msg_hash in seen:
            f.write(f"{msg_hash}\n")

def check_for_new_messages():
    """Check for new or modified messages from Agent B"""
    seen_hashes = load_seen_messages()
    new_messages = []
    
    if not MESSAGE_DIR.exists():
        MESSAGE_DIR.mkdir(parents=True, exist_ok=True)
        return new_messages
    
    # Check all files in B_TO_A directory
    for file_path in MESSAGE_DIR.glob("*"):
        if file_path.is_file():
            file_hash = get_file_hash(file_path)
            
            if file_hash not in seen_hashes:
                new_messages.append(file_path)
                seen_hashes.add(file_hash)
    
    # Save updated seen messages
    save_seen_messages(seen_hashes)
    
    return new_messages

def display_new_message(file_path):
    """Display a new message with formatting"""
    print(f"\n{'='*60}")
    print(f"📨 NEW MESSAGE FROM AGENT B!")
    print(f"📄 File: {file_path.name}")
    print(f"🕐 Detected: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")
    
    with open(file_path, 'r') as f:
        content = f.read()
        print(content[:500])  # Show first 500 chars
        if len(content) > 500:
            print(f"\n... [Message truncated. Total length: {len(content)} chars]")
    
    print(f"\n{'='*60}\n")

def main():
    print("🤖 Agent A Automatic Message Checker v1.0")
    print("=========================================")
    print(f"📁 Monitoring: {MESSAGE_DIR}")
    print(f"⏱️  Check interval: {CHECK_INTERVAL} seconds")
    print("🔄 Press Ctrl+C to stop\n")
    
    # Initial check
    print("🔍 Performing initial check...")
    new_messages = check_for_new_messages()
    
    if new_messages:
        print(f"📬 Found {len(new_messages)} message(s)!")
        for msg in new_messages:
            display_new_message(msg)
    else:
        print("📭 No new messages found.\n")
    
    # Continuous monitoring
    try:
        while True:
            time.sleep(CHECK_INTERVAL)
            print(f"🔄 Checking... [{datetime.now().strftime('%H:%M:%S')}]", end='\r')
            
            new_messages = check_for_new_messages()
            if new_messages:
                print()  # Clear the checking line
                for msg in new_messages:
                    display_new_message(msg)
                    print("💡 TIP: Create your response in MESSAGES/A_TO_B/")
                    
    except KeyboardInterrupt:
        print("\n\n👋 Message checker stopped. Goodbye!")

if __name__ == "__main__":
    main() 