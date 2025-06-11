#!/bin/bash

echo "🔧 Fixing recognitionjournal.com domain configuration..."

# Check if CNAME file exists
if [ ! -f "CNAME" ]; then
    echo "recognitionjournal.com" > CNAME
    echo "✅ Created CNAME file"
fi

# Add, commit and push CNAME file
git add CNAME
git commit -m "Fix: Re-add CNAME for recognitionjournal.com domain" || echo "CNAME already committed"
git push origin main

echo "🚀 Domain fix deployed!"
echo "⏳ Wait 2-3 minutes for GitHub Pages to detect the CNAME file"
echo "🌐 Then visit: https://recognitionjournal.com" 