#!/usr/bin/env python3
"""
Agent C Monitoring System
Watches for updates from Agent A and Agent B
Focuses on musical/sonic integration opportunities
"""

import os
import time
import subprocess
import json
from datetime import datetime
from pathlib import Path

class AgentCMonitor:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.last_check = {}
        self.state_file = "agent_c_monitor_state.json"
        self.load_state()
        
    def load_state(self):
        """Load previous monitoring state"""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r') as f:
                    self.last_check = json.load(f)
            except:
                self.last_check = {}
    
    def save_state(self):
        """Save current monitoring state"""
        with open(self.state_file, 'w') as f:
            json.dump(self.last_check, f, indent=2)
    
    def check_messages_from_a(self):
        """Check for new messages from Agent A"""
        msg_dir = self.base_dir / "MESSAGES" / "A_TO_C"
        if not msg_dir.exists():
            return []
        
        new_messages = []
        for msg_file in msg_dir.glob("*.txt"):
            file_time = msg_file.stat().st_mtime
            last_time = self.last_check.get(f"A_TO_C_{msg_file.name}", 0)
            
            if file_time > last_time:
                new_messages.append({
                    'from': 'A',
                    'to': 'C', 
                    'file': msg_file.name,
                    'path': str(msg_file),
                    'time': datetime.fromtimestamp(file_time)
                })
                self.last_check[f"A_TO_C_{msg_file.name}"] = file_time
        
        return new_messages
    
    def check_messages_from_b(self):
        """Check for new messages from Agent B"""
        msg_dir = self.base_dir / "MESSAGES" / "B_TO_C"
        if not msg_dir.exists():
            return []
        
        new_messages = []
        for msg_file in msg_dir.glob("*.txt"):
            file_time = msg_file.stat().st_mtime
            last_time = self.last_check.get(f"B_TO_C_{msg_file.name}", 0)
            
            if file_time > last_time:
                new_messages.append({
                    'from': 'B',
                    'to': 'C',
                    'file': msg_file.name, 
                    'path': str(msg_file),
                    'time': datetime.fromtimestamp(file_time)
                })
                self.last_check[f"B_TO_C_{msg_file.name}"] = file_time
        
        return new_messages
    
    def check_status_updates(self):
        """Check for status file updates"""
        updates = []
        
        for agent in ['A', 'B']:
            status_file = self.base_dir / f"AGENT_{agent}_STATUS.md"
            if status_file.exists():
                file_time = status_file.stat().st_mtime
                last_time = self.last_check.get(f"STATUS_{agent}", 0)
                
                if file_time > last_time:
                    updates.append({
                        'agent': agent,
                        'file': f"AGENT_{agent}_STATUS.md",
                        'time': datetime.fromtimestamp(file_time)
                    })
                    self.last_check[f"STATUS_{agent}"] = file_time
        
        return updates
    
    def notify(self, message):
        """Send notification (macOS/Linux/Windows compatible)"""
        print(f"🎵 Agent C Notification: {message}")
        
        # Try macOS notification
        try:
            subprocess.run([
                'osascript', '-e', 
                f'display notification "{message}" with title "Agent C Monitor" sound name "Glass"'
            ], check=False, capture_output=True)
        except:
            pass
    
    def process_message(self, msg):
        """Process a new message with musical context"""
        print(f"\n🎸 NEW MESSAGE: {msg['from']} → C")
        print(f"📄 File: {msg['file']}")
        print(f"⏰ Time: {msg['time']}")
        
        # Read and display message content
        try:
            with open(msg['path'], 'r') as f:
                content = f.read()
                print(f"📝 Content:\n{content[:500]}...")
                
                # Look for musical integration opportunities
                if any(keyword in content.lower() for keyword in 
                       ['golden ratio', 'φ', 'phi', '8-beat', 'frequency', 'harmonic']):
                    print("🎵 MUSICAL INTEGRATION OPPORTUNITY DETECTED!")
                    
        except Exception as e:
            print(f"Error reading message: {e}")
        
        print("=" * 60)
    
    def check_all_updates(self):
        """Check for all types of updates"""
        updates_found = False
        
        # Check messages from Agent A
        a_messages = self.check_messages_from_a()
        for msg in a_messages:
            self.process_message(msg)
            self.notify(f"New message from Agent A: {msg['file']}")
            updates_found = True
        
        # Check messages from Agent B  
        b_messages = self.check_messages_from_b()
        for msg in b_messages:
            self.process_message(msg)
            self.notify(f"New message from Agent B: {msg['file']}")
            updates_found = True
        
        # Check status updates
        status_updates = self.check_status_updates()
        for update in status_updates:
            print(f"📋 Agent {update['agent']} updated status: {update['time']}")
            self.notify(f"Agent {update['agent']} status updated")
            updates_found = True
        
        if updates_found:
            self.save_state()
        
        return updates_found
    
    def run_continuous(self, interval=30):
        """Run continuous monitoring"""
        print("🎵 Agent C Monitor starting...")
        print(f"🔄 Checking every {interval} seconds for updates from Agents A & B")
        print("🎸 Focus: Musical integration opportunities")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                self.check_all_updates()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n🎵 Agent C Monitor stopped. Rock on! 🤘")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Agent C Monitoring System')
    parser.add_argument('--once', action='store_true', help='Check once and exit')
    parser.add_argument('--interval', type=int, default=30, help='Check interval in seconds')
    
    args = parser.parse_args()
    
    monitor = AgentCMonitor()
    
    if args.once:
        monitor.check_all_updates()
    else:
        monitor.run_continuous(args.interval)

if __name__ == "__main__":
    main() 