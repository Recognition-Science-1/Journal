#!/bin/bash
# Agent Communication Monitor - Automatic Message Checking System
# Run this to check for new messages between agents

echo "🤖 Starting 3-Agent Communication Monitor..."
echo "📍 Working directory: $(pwd)"
echo ""

# Color codes for better visibility
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Check if MESSAGES directory exists
if [ ! -d "MESSAGES" ]; then
    echo -e "${RED}ERROR: MESSAGES directory not found!${NC}"
    echo "Please run this from /Users/emmatully/Desktop/Journal/"
    exit 1
fi

echo -e "${GREEN}✅ Communication system active with 3 agents!${NC}"
echo ""
echo "📬 Monitoring message directories:"
echo "   A→B: MESSAGES/A_TO_B/"
echo "   A→C: MESSAGES/A_TO_C/"
echo "   B→A: MESSAGES/B_TO_A/"
echo "   B→C: MESSAGES/B_TO_C/"
echo "   C→A: MESSAGES/C_TO_A/"
echo "   C→B: MESSAGES/C_TO_B/"
echo ""
echo "Press Ctrl+C to stop monitoring"
echo "---"

# Function to check for new messages
check_messages() {
    # Check A to B
    if [ -n "$(ls -A MESSAGES/A_TO_B/ 2>/dev/null)" ]; then
        echo -e "${BLUE}📨 [A→B] Messages waiting for Agent B:${NC}"
        ls -la MESSAGES/A_TO_B/
        echo ""
    fi
    
    # Check A to C
    if [ -n "$(ls -A MESSAGES/A_TO_C/ 2>/dev/null)" ]; then
        echo -e "${PURPLE}📨 [A→C] Messages waiting for Agent C:${NC}"
        ls -la MESSAGES/A_TO_C/
        echo ""
    fi
    
    # Check B to A
    if [ -n "$(ls -A MESSAGES/B_TO_A/ 2>/dev/null)" ]; then
        echo -e "${GREEN}📨 [B→A] Messages waiting for Agent A:${NC}"
        ls -la MESSAGES/B_TO_A/
        echo ""
    fi
    
    # Check B to C
    if [ -n "$(ls -A MESSAGES/B_TO_C/ 2>/dev/null)" ]; then
        echo -e "${YELLOW}📨 [B→C] Messages waiting for Agent C:${NC}"
        ls -la MESSAGES/B_TO_C/
        echo ""
    fi
    
    # Check C to A
    if [ -n "$(ls -A MESSAGES/C_TO_A/ 2>/dev/null)" ]; then
        echo -e "${PURPLE}📨 [C→A] Messages waiting for Agent A:${NC}"
        ls -la MESSAGES/C_TO_A/
        echo ""
    fi
    
    # Check C to B
    if [ -n "$(ls -A MESSAGES/C_TO_B/ 2>/dev/null)" ]; then
        echo -e "${YELLOW}📨 [C→B] Messages waiting for Agent B:${NC}"
        ls -la MESSAGES/C_TO_B/
        echo ""
    fi
}

# Main monitoring loop
while true; do
    clear
    echo -e "${GREEN}🤖 3-Agent Communication Monitor${NC} - $(date)"
    echo "====================================="
    echo ""
    
    check_messages
    
    # Show summary
    echo "---"
    echo -e "📊 Message Count Summary:"
    echo -e "   A→B: $(ls -1 MESSAGES/A_TO_B/ 2>/dev/null | wc -l) messages"
    echo -e "   A→C: $(ls -1 MESSAGES/A_TO_C/ 2>/dev/null | wc -l) messages"
    echo -e "   B→A: $(ls -1 MESSAGES/B_TO_A/ 2>/dev/null | wc -l) messages"
    echo -e "   B→C: $(ls -1 MESSAGES/B_TO_C/ 2>/dev/null | wc -l) messages"
    echo -e "   C→A: $(ls -1 MESSAGES/C_TO_A/ 2>/dev/null | wc -l) messages"
    echo -e "   C→B: $(ls -1 MESSAGES/C_TO_B/ 2>/dev/null | wc -l) messages"
    echo ""
    echo "Next check in 30 seconds... (Ctrl+C to stop)"
    
    sleep 30
done 