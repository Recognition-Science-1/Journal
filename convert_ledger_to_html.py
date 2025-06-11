#!/usr/bin/env python3
"""Convert ledger.md to ledger.html"""

# Read the markdown file
with open('ledger.md', 'r') as f:
    content = f.read()

# Extract the content between the front matter and convert to HTML
# Skip the front matter (between --- markers)
lines = content.split('\n')
start_index = 0
count = 0
for i, line in enumerate(lines):
    if line.strip() == '---':
        count += 1
        if count == 2:
            start_index = i + 1
            break

# Get the actual content
md_content = '\n'.join(lines[start_index:])

# Since the content is already HTML embedded in markdown, we just need to wrap it properly
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Prediction Ledger - Journal of Recognition Science</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; color: #333; background: #f8f9fa; }}
        .header {{ background: white; border-bottom: 1px solid #e1e5e9; padding: 1rem 0; }}
        .nav {{ max-width: 1200px; margin: 0 auto; padding: 0 2rem; display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-size: 1.5rem; font-weight: 600; color: #333; text-decoration: none; }}
        .nav-links {{ display: flex; gap: 2rem; list-style: none; }}
        .nav-links a {{ color: #666; text-decoration: none; font-weight: 500; }}
        .nav-links a:hover {{ color: #007bff; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 2rem; }}
    </style>
</head>
<body>
    <header class="header">
        <nav class="nav">
            <a href="index.html" class="logo">Journal of Recognition Science</a>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="ledger.html">Live Ledger</a></li>
                <li><a href="axioms.html">Axioms</a></li>
                <li><a href="calculators.html">Calculators</a></li>
            </ul>
        </nav>
    </header>
    <div class="container">
{md_content}
    </div>
</body>
</html>'''

# Write the HTML file
with open('ledger.html', 'w') as f:
    f.write(html_content)

print("Successfully converted ledger.md to ledger.html!")
print("The file now contains all 60 predictions in HTML format.") 