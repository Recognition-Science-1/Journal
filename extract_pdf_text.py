#!/usr/bin/env python3
"""Extract text from peer review PDF"""

# Try basic approach - PDFs often have text embedded
try:
    with open('peer_review_golden_ratio.pdf', 'rb') as f:
        pdf_content = f.read()
        
    # Convert bytes to string and look for readable text
    text = pdf_content.decode('latin-1', errors='ignore')
    
    # Find text between common PDF markers
    print("Searching for readable text in PDF...")
    print("=" * 80)
    
    # Look for text patterns
    lines = text.split('\n')
    readable_lines = []
    
    for line in lines:
        # Filter for lines with mostly printable characters
        if len(line) > 10:
            printable = sum(1 for c in line if 32 <= ord(c) <= 126)
            if printable / len(line) > 0.8:
                readable_lines.append(line)
    
    if readable_lines:
        print("Found readable content:")
        print("-" * 80)
        for line in readable_lines[:50]:  # First 50 lines
            print(line.strip())
    else:
        print("No easily readable text found in PDF")
        print("This PDF may need specialized tools to extract content")
        
except Exception as e:
    print(f"Error reading PDF: {e}") 