#!/bin/bash
# Workspace Verification Script for Recognition Science Journal Agents

echo "🔍 Recognition Science Journal - Workspace Checker"
echo "================================================="
echo

# Check current directory
CURRENT_DIR=$(pwd)
EXPECTED_DIR="/Users/emmatully/Desktop/Journal"

echo "📁 Current directory: $CURRENT_DIR"
echo "✅ Expected directory: $EXPECTED_DIR"
echo

if [ "$CURRENT_DIR" = "$EXPECTED_DIR" ]; then
    echo "✅ SUCCESS: You are in the correct working directory!"
else
    echo "❌ ERROR: You are NOT in the correct directory!"
    echo "   Please run: cd $EXPECTED_DIR"
    echo
    
    # Check if we can navigate to the correct directory
    if [ -d "$EXPECTED_DIR" ]; then
        echo "📂 The correct directory exists. Switching now..."
        cd "$EXPECTED_DIR"
        echo "✅ Switched to: $(pwd)"
    else
        echo "⚠️  WARNING: The expected directory doesn't exist!"
        echo "   This might mean you need to clone the repository first."
    fi
fi

echo
echo "🔍 Checking for duplicate folders on Desktop..."
echo "-----------------------------------------------"
DESKTOP_DIR="/Users/emmatully/Desktop"
cd "$DESKTOP_DIR"

# Find all Ledger-related folders
LEDGER_FOLDERS=$(find . -maxdepth 3 -type d -name "*[Ll]edger*" -o -name "*[Jj]ournal*" 2>/dev/null | grep -v "^./Ledger$" | grep -v ".git")

if [ -z "$LEDGER_FOLDERS" ]; then
    echo "✅ No duplicate folders found!"
else
    echo "⚠️  Found potential duplicate folders:"
    echo "$LEDGER_FOLDERS"
    echo
    echo "These folders might cause confusion and should be removed after ensuring"
    echo "all agents are working in: $EXPECTED_DIR"
fi

# Navigate back to expected directory
cd "$EXPECTED_DIR" 2>/dev/null

echo
echo "📊 Git Repository Status:"
echo "------------------------"
if [ -d ".git" ]; then
    echo "✅ Git repository found"
    echo "📍 Remote URL:"
    git remote -v | head -1
    echo
    echo "📝 Latest commits:"
    git log --oneline -3
    echo
    echo "🔄 Current status:"
    git status -s
else
    echo "❌ No git repository found in current directory!"
fi

echo
echo "========================================="
echo "🎯 REMEMBER: All agents must work in:"
echo "   $EXPECTED_DIR"
echo "=========================================" 