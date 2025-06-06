#!/usr/bin/env python3
"""
Web-based Agent Monitor Dashboard
Provides real-time visualization of all agent activities
"""

from flask import Flask, render_template_string, jsonify
import json
import os
from datetime import datetime
from pathlib import Path
import threading
import time

app = Flask(__name__)

# HTML template for the dashboard
DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Recognition Science - Agent Monitor</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .card h3 {
            margin: 0 0 15px 0;
            color: #667eea;
        }
        .agent-status {
            padding: 10px;
            background: #f8f9fa;
            border-radius: 4px;
            margin-bottom: 10px;
        }
        .agent-name {
            font-weight: bold;
            color: #333;
        }
        .last-active {
            color: #666;
            font-size: 0.9em;
        }
        .message {
            padding: 10px;
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            margin-bottom: 10px;
            border-radius: 4px;
        }
        .message-header {
            font-weight: bold;
            color: #1976d2;
            margin-bottom: 5px;
        }
        .message-time {
            font-size: 0.8em;
            color: #666;
        }
        .refresh-indicator {
            text-align: center;
            color: #666;
            font-size: 0.9em;
            margin-top: 20px;
        }
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 5px;
        }
        .status-active {
            background: #4caf50;
            animation: pulse 2s infinite;
        }
        .status-inactive {
            background: #ff9800;
        }
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        .stats-row {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }
        .stat-item {
            text-align: center;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stat-value {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }
        .stat-label {
            color: #666;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 Recognition Science - Agent Monitor Dashboard</h1>
        
        <div class="stats-row">
            <div class="stat-item">
                <div class="stat-value" id="agent-count">0</div>
                <div class="stat-label">Active Agents</div>
            </div>
            <div class="stat-item">
                <div class="stat-value" id="message-count">0</div>
                <div class="stat-label">Messages Today</div>
            </div>
            <div class="stat-item">
                <div class="stat-value" id="update-count">0</div>
                <div class="stat-label">Updates This Hour</div>
            </div>
        </div>
        
        <div class="status-grid">
            <div class="card">
                <h3>👥 Agent Status</h3>
                <div id="agent-status-list"></div>
            </div>
            
            <div class="card">
                <h3>💬 Recent Messages</h3>
                <div id="message-list"></div>
            </div>
            
            <div class="card">
                <h3>📊 Activity Timeline</h3>
                <div id="activity-timeline"></div>
            </div>
        </div>
        
        <div class="refresh-indicator">
            Auto-refreshing every 5 seconds... Last update: <span id="last-update"></span>
        </div>
    </div>
    
    <script>
        function formatTimeAgo(timestamp) {
            const now = new Date();
            const then = new Date(timestamp);
            const diff = Math.floor((now - then) / 1000);
            
            if (diff < 60) return diff + 's ago';
            if (diff < 3600) return Math.floor(diff / 60) + 'm ago';
            if (diff < 86400) return Math.floor(diff / 3600) + 'h ago';
            return Math.floor(diff / 86400) + 'd ago';
        }
        
        function updateDashboard() {
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {
                    // Update stats
                    document.getElementById('agent-count').textContent = data.agent_count;
                    document.getElementById('message-count').textContent = data.message_count;
                    document.getElementById('update-count').textContent = data.update_count;
                    
                    // Update agent status
                    const agentList = document.getElementById('agent-status-list');
                    agentList.innerHTML = '';
                    data.agents.forEach(agent => {
                        const isActive = agent.last_active_minutes < 5;
                        agentList.innerHTML += `
                            <div class="agent-status">
                                <span class="status-indicator ${isActive ? 'status-active' : 'status-inactive'}"></span>
                                <span class="agent-name">Agent ${agent.name}</span>
                                <div class="last-active">Last active: ${agent.last_active}</div>
                                <div>Focus: ${agent.current_focus || 'Unknown'}</div>
                            </div>
                        `;
                    });
                    
                    // Update messages
                    const messageList = document.getElementById('message-list');
                    messageList.innerHTML = '';
                    data.recent_messages.forEach(msg => {
                        messageList.innerHTML += `
                            <div class="message">
                                <div class="message-header">${msg.from} → ${msg.to}</div>
                                <div>${msg.preview}</div>
                                <div class="message-time">${formatTimeAgo(msg.timestamp)}</div>
                            </div>
                        `;
                    });
                    
                    // Update activity timeline
                    const timeline = document.getElementById('activity-timeline');
                    timeline.innerHTML = '';
                    data.activity_timeline.forEach(activity => {
                        timeline.innerHTML += `
                            <div class="agent-status">
                                <div>${activity.icon} ${activity.description}</div>
                                <div class="message-time">${formatTimeAgo(activity.timestamp)}</div>
                            </div>
                        `;
                    });
                    
                    // Update last refresh time
                    document.getElementById('last-update').textContent = new Date().toLocaleTimeString();
                })
                .catch(error => console.error('Error updating dashboard:', error));
        }
        
        // Update immediately and then every 5 seconds
        updateDashboard();
        setInterval(updateDashboard, 5000);
    </script>
</body>
</html>
"""

class DashboardData:
    """Manages dashboard data collection"""
    
    def __init__(self):
        self.base_path = Path(".")
        self.messages_dir = self.base_path / "MESSAGES"
        
    def get_agents(self):
        """Get all agents and their status"""
        agents = []
        
        # Find all agent status files
        for status_file in self.base_path.glob("AGENT_*_STATUS.md"):
            agent_name = status_file.stem.split('_')[1]
            
            # Get last modified time
            mod_time = datetime.fromtimestamp(status_file.stat().st_mtime)
            minutes_ago = (datetime.now() - mod_time).total_seconds() / 60
            
            # Read current focus
            current_focus = "Unknown"
            try:
                with open(status_file, 'r') as f:
                    content = f.read()
                    for line in content.split('\n'):
                        if "Current Focus" in line and ':' in line:
                            current_focus = line.split(':', 1)[1].strip()
                            break
            except:
                pass
            
            agents.append({
                "name": agent_name,
                "last_active": self.format_time_ago(mod_time),
                "last_active_minutes": minutes_ago,
                "current_focus": current_focus
            })
        
        return sorted(agents, key=lambda x: x["name"])
    
    def get_recent_messages(self, limit=5):
        """Get recent messages between agents"""
        messages = []
        
        if not self.messages_dir.exists():
            return messages
        
        # Collect all messages
        for msg_dir in self.messages_dir.iterdir():
            if msg_dir.is_dir() and '_TO_' in msg_dir.name:
                from_agent, to_agent = msg_dir.name.split('_TO_')
                
                for msg_file in msg_dir.glob("*.txt"):
                    try:
                        with open(msg_file, 'r') as f:
                            content = f.read()
                            preview = content[:100] + "..." if len(content) > 100 else content
                            preview = preview.replace('\n', ' ')
                        
                        messages.append({
                            "from": from_agent,
                            "to": to_agent,
                            "file": msg_file.name,
                            "preview": preview,
                            "timestamp": datetime.fromtimestamp(msg_file.stat().st_mtime).isoformat()
                        })
                    except:
                        pass
        
        # Sort by timestamp and return most recent
        messages.sort(key=lambda x: x["timestamp"], reverse=True)
        return messages[:limit]
    
    def get_activity_timeline(self, hours=1):
        """Get activity timeline for the last N hours"""
        activities = []
        cutoff_time = datetime.now().timestamp() - (hours * 3600)
        
        # Check git log
        try:
            import subprocess
            result = subprocess.run(
                ["git", "log", "--since", f"{hours} hours ago", "--oneline"],
                capture_output=True, text=True
            )
            for line in result.stdout.strip().split('\n')[:5]:
                if line:
                    activities.append({
                        "icon": "📝",
                        "description": f"Git commit: {line[:50]}...",
                        "timestamp": datetime.now().isoformat()  # Approximate
                    })
        except:
            pass
        
        # Check file modifications
        for path in self.base_path.glob("*"):
            if path.stat().st_mtime > cutoff_time:
                activities.append({
                    "icon": "📄",
                    "description": f"File updated: {path.name}",
                    "timestamp": datetime.fromtimestamp(path.stat().st_mtime).isoformat()
                })
        
        # Sort and limit
        activities.sort(key=lambda x: x["timestamp"], reverse=True)
        return activities[:10]
    
    def format_time_ago(self, timestamp):
        """Format timestamp as time ago"""
        if isinstance(timestamp, datetime):
            delta = datetime.now() - timestamp
        else:
            delta = datetime.now() - datetime.fromtimestamp(timestamp)
        
        seconds = delta.total_seconds()
        if seconds < 60:
            return f"{int(seconds)}s ago"
        elif seconds < 3600:
            return f"{int(seconds / 60)}m ago"
        elif seconds < 86400:
            return f"{int(seconds / 3600)}h ago"
        else:
            return f"{int(seconds / 86400)}d ago"
    
    def get_stats(self):
        """Get dashboard statistics"""
        agents = self.get_agents()
        messages = self.get_recent_messages(20)
        activities = self.get_activity_timeline(1)
        
        # Count messages today
        today_count = sum(1 for msg in messages 
                         if datetime.fromisoformat(msg["timestamp"]).date() == datetime.now().date())
        
        return {
            "agent_count": len(agents),
            "message_count": today_count,
            "update_count": len(activities),
            "agents": agents,
            "recent_messages": self.get_recent_messages(5),
            "activity_timeline": activities
        }

# Global dashboard data instance
dashboard = DashboardData()

@app.route('/')
def index():
    """Serve the dashboard HTML"""
    return render_template_string(DASHBOARD_HTML)

@app.route('/api/status')
def api_status():
    """API endpoint for dashboard data"""
    return jsonify(dashboard.get_stats())

def main():
    """Run the dashboard server"""
    print("🌐 Starting Recognition Science Monitor Dashboard")
    print("📍 Open http://localhost:5000 in your browser")
    print("Press Ctrl+C to stop\n")
    
    # Run Flask app
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    main() 