#!/usr/bin/env python3
"""
Universal Agent Monitor - Automatically checks for updates from ALL agents
Features:
- Monitors all agent directories
- Real-time notifications
- Message processing and archiving
- Git synchronization
- Status dashboard
"""

import os
import time
import json
import hashlib
import subprocess
from datetime import datetime
from pathlib import Path
import threading
import queue

class AgentMonitor:
    def __init__(self):
        self.base_path = Path(".")
        self.messages_dir = self.base_path / "MESSAGES"
        self.state_file = self.base_path / ".monitor_state.json"
        self.update_queue = queue.Queue()
        self.state = self.load_state()
        
        # Identify all agents
        self.agents = self.discover_agents()
        print(f"🔍 Discovered agents: {', '.join(self.agents)}")
        
    def load_state(self):
        """Load previous monitoring state."""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {
            "last_check": {},
            "message_hashes": {},
            "file_hashes": {},
            "processed_messages": []
        }
    
    def save_state(self):
        """Save current monitoring state."""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def discover_agents(self):
        """Discover all agents from status files and message directories."""
        agents = set()
        
        # Check status files
        for file in self.base_path.glob("AGENT_*_STATUS.md"):
            agent = file.stem.split('_')[1]
            agents.add(agent)
        
        # Check message directories
        if self.messages_dir.exists():
            for dir in self.messages_dir.iterdir():
                if dir.is_dir() and '_TO_' in dir.name:
                    parts = dir.name.split('_TO_')
                    agents.update(parts)
        
        return sorted(list(agents))
    
    def run_command(self, cmd):
        """Run shell command and return output."""
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return None
    
    def send_notification(self, title, message):
        """Send desktop notification (macOS/Linux/Windows)."""
        try:
            if os.uname().sysname == "Darwin":  # macOS
                script = f'display notification "{message}" with title "{title}"'
                subprocess.run(['osascript', '-e', script])
            elif os.uname().sysname == "Linux":
                subprocess.run(['notify-send', title, message])
            else:  # Windows
                # For Windows, you'd need to install plyer: pip install plyer
                print(f"🔔 {title}: {message}")
        except:
            print(f"🔔 {title}: {message}")
    
    def get_file_hash(self, filepath):
        """Get hash of file contents."""
        if not Path(filepath).exists():
            return None
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def check_git_updates(self):
        """Pull latest changes from git."""
        output = self.run_command("git pull origin main")
        if output and "Already up to date" not in output:
            self.update_queue.put({
                "type": "git",
                "message": f"Git updated: {output}",
                "timestamp": datetime.now()
            })
            return True
        return False
    
    def check_agent_messages(self, from_agent, to_agent):
        """Check for new messages between agents."""
        msg_dir = self.messages_dir / f"{from_agent}_TO_{to_agent}"
        if not msg_dir.exists():
            return []
        
        new_messages = []
        for msg_file in msg_dir.glob("*.txt"):
            file_hash = self.get_file_hash(msg_file)
            hash_key = f"{from_agent}_TO_{to_agent}/{msg_file.name}"
            
            if hash_key not in self.state["message_hashes"] or \
               self.state["message_hashes"][hash_key] != file_hash:
                # New or updated message
                with open(msg_file, 'r') as f:
                    content = f.read()
                
                new_messages.append({
                    "from": from_agent,
                    "to": to_agent,
                    "file": msg_file.name,
                    "content": content,
                    "timestamp": datetime.fromtimestamp(msg_file.stat().st_mtime)
                })
                
                self.state["message_hashes"][hash_key] = file_hash
        
        return new_messages
    
    def check_agent_status(self, agent):
        """Check if agent status file was updated."""
        status_file = self.base_path / f"AGENT_{agent}_STATUS.md"
        if not status_file.exists():
            return None
        
        file_hash = self.get_file_hash(status_file)
        hash_key = f"status_{agent}"
        
        if hash_key not in self.state["file_hashes"] or \
           self.state["file_hashes"][hash_key] != file_hash:
            # Status updated
            self.state["file_hashes"][hash_key] = file_hash
            
            # Extract key info
            with open(status_file, 'r') as f:
                content = f.read()
            
            # Find current focus
            focus = "Unknown"
            for line in content.split('\n'):
                if "Current Focus" in line:
                    focus = line.split(':', 1)[1].strip() if ':' in line else "Unknown"
                    break
            
            return {
                "agent": agent,
                "focus": focus,
                "timestamp": datetime.fromtimestamp(status_file.stat().st_mtime)
            }
        
        return None
    
    def check_all_agents(self):
        """Check for updates from all agents."""
        updates = []
        
        # Check git first
        self.check_git_updates()
        
        # Check messages between all agent pairs
        for from_agent in self.agents:
            for to_agent in self.agents:
                if from_agent != to_agent:
                    messages = self.check_agent_messages(from_agent, to_agent)
                    for msg in messages:
                        self.update_queue.put({
                            "type": "message",
                            "data": msg,
                            "timestamp": datetime.now()
                        })
        
        # Check status updates
        for agent in self.agents:
            status_update = self.check_agent_status(agent)
            if status_update:
                self.update_queue.put({
                    "type": "status",
                    "data": status_update,
                    "timestamp": datetime.now()
                })
        
        self.save_state()
    
    def process_updates(self):
        """Process queued updates and send notifications."""
        while not self.update_queue.empty():
            update = self.update_queue.get()
            
            if update["type"] == "message":
                msg = update["data"]
                self.send_notification(
                    f"📨 Message: {msg['from']} → {msg['to']}",
                    f"New message in {msg['file']}"
                )
                print(f"\n{'='*60}")
                print(f"📨 NEW MESSAGE: {msg['from']} → {msg['to']}")
                print(f"📄 File: {msg['file']}")
                print(f"⏰ Time: {msg['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"📝 Content:\n{msg['content']}")
                print(f"{'='*60}\n")
                
            elif update["type"] == "status":
                status = update["data"]
                self.send_notification(
                    f"📋 Agent {status['agent']} Status Update",
                    f"Current focus: {status['focus']}"
                )
                print(f"📋 Agent {status['agent']} updated status: {status['focus']}")
                
            elif update["type"] == "git":
                self.send_notification(
                    "🔄 Git Repository Updated",
                    update["message"]
                )
                print(f"🔄 {update['message']}")
    
    def show_dashboard(self):
        """Display current monitoring status."""
        print(f"\n{'='*60}")
        print(f"🎯 AGENT MONITOR DASHBOARD - {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*60}")
        print(f"👥 Active Agents: {', '.join(self.agents)}")
        
        # Show recent activity
        print(f"\n📊 Recent Activity:")
        for agent in self.agents:
            status_file = self.base_path / f"AGENT_{agent}_STATUS.md"
            if status_file.exists():
                mod_time = datetime.fromtimestamp(status_file.stat().st_mtime)
                print(f"   Agent {agent}: Last active {self.time_ago(mod_time)}")
        
        print(f"\n💬 Message Channels:")
        for from_agent in self.agents:
            for to_agent in self.agents:
                if from_agent != to_agent:
                    msg_dir = self.messages_dir / f"{from_agent}_TO_{to_agent}"
                    if msg_dir.exists():
                        msg_count = len(list(msg_dir.glob("*.txt")))
                        if msg_count > 0:
                            print(f"   {from_agent} → {to_agent}: {msg_count} messages")
        
        print(f"{'='*60}\n")
    
    def time_ago(self, timestamp):
        """Convert timestamp to human-readable time ago."""
        delta = datetime.now() - timestamp
        if delta.seconds < 60:
            return f"{delta.seconds}s ago"
        elif delta.seconds < 3600:
            return f"{delta.seconds // 60}m ago"
        elif delta.days == 0:
            return f"{delta.seconds // 3600}h ago"
        else:
            return f"{delta.days}d ago"
    
    def run_continuous(self, interval=30):
        """Run continuous monitoring."""
        print("🚀 Starting Universal Agent Monitor")
        print(f"⏰ Checking every {interval} seconds")
        print("Press Ctrl+C to stop\n")
        
        self.show_dashboard()
        
        while True:
            try:
                print(f"🔍 Checking for updates... [{datetime.now().strftime('%H:%M:%S')}]")
                self.check_all_agents()
                self.process_updates()
                
                # Show mini status
                update_count = self.update_queue.qsize()
                if update_count == 0:
                    print("💤 No new updates")
                
                print(f"⏳ Next check in {interval} seconds...\n")
                time.sleep(interval)
                
            except KeyboardInterrupt:
                print("\n\n👋 Monitor stopped by user")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(interval)


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Universal Agent Monitor")
    parser.add_argument("--interval", type=int, default=30, 
                       help="Check interval in seconds (default: 30)")
    parser.add_argument("--once", action="store_true", 
                       help="Check once and exit")
    parser.add_argument("--dashboard", action="store_true",
                       help="Show dashboard and exit")
    
    args = parser.parse_args()
    
    monitor = AgentMonitor()
    
    if args.dashboard:
        monitor.show_dashboard()
    elif args.once:
        monitor.check_all_agents()
        monitor.process_updates()
    else:
        monitor.run_continuous(interval=args.interval)


if __name__ == "__main__":
    main() 