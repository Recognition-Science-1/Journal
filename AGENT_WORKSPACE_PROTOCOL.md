# 🚨 CRITICAL: Agent Workspace Protocol

## ⚠️ IMPORTANT: ALL AGENTS MUST WORK IN THE SAME DIRECTORY

### 📁 OFFICIAL WORKING DIRECTORY:
```
/Users/emmatully/Desktop/Ledger
```

### ❌ DO NOT CREATE NEW FOLDERS
- DO NOT create Ledger2, Ledger1, Journal, or any other variant
- DO NOT clone the repository to a new location
- DO NOT work in nested folders

### ✅ CORRECT WORKFLOW FOR ALL AGENTS:

1. **ALWAYS start with:**
   ```bash
   cd /Users/emmatully/Desktop/Ledger
   pwd  # Should show: /Users/emmatully/Desktop/Ledger
   ```

2. **Before ANY work:**
   ```bash
   git pull origin main
   ```

3. **Check you're in sync:**
   ```bash
   git status
   git log --oneline -5
   ```

### 🔧 IF YOU'RE IN THE WRONG FOLDER:

**Agent B (or any agent not in the main Ledger folder):**
```bash
# Navigate to the correct folder
cd /Users/emmatully/Desktop/Ledger

# Verify you're in the right place
pwd  # Must show: /Users/emmatully/Desktop/Ledger

# Check git remote
git remote -v  # Should show: https://github.com/Recognition-Science-1/Journal.git

# Pull latest changes
git pull origin main
```

### 🗑️ CLEANUP DUPLICATE FOLDERS:

Once all agents confirm they're working in `/Users/emmatully/Desktop/Ledger`, we can remove:
- `/Users/emmatully/Desktop/Ledger2/`
- Any other duplicate folders

### 📋 AGENT CHECKLIST:
- [ ] Agent A: Confirmed working in `/Users/emmatully/Desktop/Ledger` ✅
- [ ] Agent B: Must switch to `/Users/emmatully/Desktop/Ledger`
- [ ] Agent C (if any): Must use `/Users/emmatully/Desktop/Ledger`

### 🤝 COORDINATION RULES:
1. **ONE REPOSITORY, ONE FOLDER** - No exceptions
2. **PULL BEFORE PUSH** - Always sync before making changes
3. **ANNOUNCE YOUR WORK** - Use clear commit messages with agent identifier
4. **NO NESTED CLONES** - Never clone inside the project folder

### 🚨 IMMEDIATE ACTION REQUIRED:
All agents must acknowledge this protocol by adding their confirmation below:

---
## Agent Confirmations:
- **Agent A**: ✅ Confirmed working in /Users/emmatully/Desktop/Ledger (Jun 5, 2025)
- **Agent B**: ⏳ NEEDS TO CONFIRM AND SWITCH FOLDERS
- **Agent C**: ⏳ (if applicable)

---

**Remember: Multiple folders = Multiple problems. One folder = Smooth collaboration!** 