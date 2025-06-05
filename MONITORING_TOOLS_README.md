# 🤖 Agent Monitoring Tools

Automatic update checking tools for Agent B to monitor Agent A's updates.

## 🛠️ Available Tools

### 1. `check_agent_updates.py` - Full-Featured Monitor
Python script with comprehensive monitoring:
- Pulls git updates automatically
- Checks for new messages in MESSAGES/A_TO_B/
- Monitors AGENT_A_STATUS.md for changes
- Shows recent commits from Agent A

**Usage:**
```bash
# Continuous monitoring (checks every 30 seconds)
python3 check_agent_updates.py

# Single check only
python3 check_agent_updates.py --once
```

### 2. `monitor_agent_a.sh` - Simple Shell Monitor
Lightweight bash script for quick monitoring:
- Git pull and status check
- Message detection
- Status file monitoring

**Usage:**
```bash
# Continuous monitoring
./monitor_agent_a.sh

# Single check
./monitor_agent_a.sh --once
```

### 3. `agent_notifier.py` - Desktop Notifications
macOS desktop notifications for updates:
- System notifications when messages arrive
- Alerts for recent status updates

**Usage:**
```bash
python3 agent_notifier.py
```

## 🚀 Quick Start

1. **Start continuous monitoring:**
   ```bash
   python3 check_agent_updates.py
   ```

2. **Run in background:**
   ```bash
   nohup python3 check_agent_updates.py > monitor.log 2>&1 &
   ```

3. **Check monitoring log:**
   ```bash
   tail -f monitor.log
   ```

## 🎯 Features

- **Automatic Git Sync**: Pulls updates every check cycle
- **Message Detection**: Instantly shows new messages from Agent A
- **Status Tracking**: Monitors Agent A's status file for changes
- **Commit History**: Shows recent Agent A commits
- **Desktop Alerts**: Optional system notifications (macOS)

## 📊 Example Output

```
🔍 Checking for updates... [18:35:22]
📥 Pulling latest changes...
📨 Found 1 message(s) from Agent A!
   - integration_ready.txt

--- Message Content ---
FROM: Agent A
TO: Agent B
MESSAGE: Website ready for particle calculator!
--- End Message ---

📋 Agent A Status: **Last Updated**: Current Session
✅ Updates found!
```

## 💡 Tips

- Run monitor in a separate terminal window
- Check every 30-60 seconds for best balance
- Use `--once` flag for manual checks
- Desktop notifications work best on macOS

---

*Created by Agent B for automatic Agent A update monitoring* 