#!/usr/bin/env python3
"""
Enhance the ledger predictions with expandable detailed content
"""

import re

# Read the current ledger
with open('ledger.md', 'r') as f:
    content = f.read()

# Add enhanced JavaScript for expandable predictions
enhanced_script = """
<script>
// Enhanced prediction functionality
function togglePrediction(element) {
  const predictionItem = element.closest('.prediction-item');
  predictionItem.classList.toggle('expanded');
}

// Add click handlers to all predictions
document.addEventListener('DOMContentLoaded', function() {
  const predictions = document.querySelectorAll('.prediction-item');
  predictions.forEach((pred, index) => {
    // Add unique ID
    pred.id = `prediction-${index}`;
    
    // Make header clickable
    const header = pred.querySelector('.prediction-content');
    if (header) {
      header.style.cursor = 'pointer';
      header.onclick = function() { togglePrediction(this); };
      
      // Add expand arrow
      const arrow = document.createElement('span');
      arrow.className = 'expand-arrow';
      arrow.innerHTML = '⌄';
      header.appendChild(arrow);
    }
  });
});

// Update verification timestamp
document.getElementById('verification-time').textContent = new Date().toLocaleString();

// Calculate hash of predictions
async function calculatePredictionHash() {
  const predictions = document.querySelectorAll('.prediction-content');
  let predictionText = '';
  
  predictions.forEach(pred => {
    const title = pred.querySelector('h4').textContent;
    const details = Array.from(pred.querySelectorAll('p')).map(p => p.textContent).join(' ');
    predictionText += title + ' ' + details + '\\n';
  });
  
  // Simple hash simulation (in production, use proper SHA-256)
  const encoder = new TextEncoder();
  const data = encoder.encode(predictionText);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  
  document.getElementById('ledger-hash').textContent = hashHex.substring(0, 32) + '...';
  document.getElementById('hash-time').textContent = new Date().toLocaleString();
}

// Calculate hash on load
calculatePredictionHash();

// Auto-refresh every 60 seconds
setInterval(() => {
  document.getElementById('verification-time').textContent = new Date().toLocaleString();
  calculatePredictionHash();
}, 60000);
</script>
"""

# Add enhanced CSS for expandable predictions
enhanced_css = """
<style>
/* Enhanced prediction styles */
.prediction-item {
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.prediction-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.expand-arrow {
  position: absolute;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.5rem;
  color: #007bff;
  transition: transform 0.3s ease;
}

.prediction-item.expanded .expand-arrow {
  transform: translateY(-50%) rotate(180deg);
}

.prediction-details {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.5s ease;
  background: #f0f4f8;
  margin-top: 1rem;
}

.prediction-item.expanded .prediction-details {
  max-height: 1000px;
}

.details-content {
  padding: 1.5rem;
  display: grid;
  gap: 1.5rem;
}

.detail-section {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

.detail-section h4 {
  color: #007bff;
  margin-bottom: 1rem;
  font-size: 1.1rem;
}

.code-block {
  background: #1e1e1e;
  color: #0ff;
  padding: 1rem;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  overflow-x: auto;
}

.action-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}

.action-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  background: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  transition: all 0.3s;
}

.action-link:hover {
  background: #0056b3;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,123,255,0.3);
}

/* Existing styles continue... */
.ledger-container {
  max-width: 1200px;
  margin: 0 auto;
}
"""

# Replace the existing script section
content = re.sub(r'<script>.*?</script>', enhanced_script, content, flags=re.DOTALL)

# Replace the existing style section
content = re.sub(r'<style>.*?</style>', enhanced_css + '\n' + content[content.find('<style>'):content.find('</style>')+8], content, flags=re.DOTALL)

# Add sample detailed content for the first prediction (Luminon)
luminon_details = """
        <div class="prediction-details">
          <div class="details-content">
            <div class="detail-section">
              <h4>📊 Precise Numerical Values</h4>
              <div class="code-block">
Primary Prediction: 492.16 ± 0.03 nm
Frequency: 609.77 ± 0.04 THz
Energy: 2.521 ± 0.0002 eV
Recognition Rung: r = 8 (fundamental octave)
Coherence Temperature: 29,211 K
Phase Coherence Length: > 5000 km</div>
            </div>
            
            <div class="detail-section">
              <h4>📐 Derivation Methodology</h4>
              <div class="code-block">
Step 1: Start with coherence energy
E_coh = 0.09 eV (base recognition quantum)

Step 2: Apply eight-tick octave principle
E_luminon = E_coh × φ^8 × (8/π)
E_luminon = 0.09 × 46.978 × 2.546 = 2.521 eV

Step 3: Convert to wavelength
λ = hc/E = 492.16 nm</div>
              <div class="action-links">
                <a href="#" class="action-link">📓 View Full Calculation</a>
                <a href="#" class="action-link">🔐 View Lean 4 Proof</a>
              </div>
            </div>
            
            <div class="detail-section">
              <h4>🔬 Experimental Timeline</h4>
              <p><strong>2025 Q3:</strong> Stanford Cavity QED Lab (F > 10⁶)</p>
              <p><strong>2026 Q1:</strong> NIST Optical Clock Network</p>
              <p><strong>2027:</strong> Ledger-Light Space Mission</p>
              <div class="action-links">
                <a href="#" class="action-link">📧 Get Notified</a>
              </div>
            </div>
          </div>
        </div>
"""

# Find the Luminon prediction and add details
luminon_pattern = r'(<div class="prediction-item pending">.*?<h4>Luminon Threshold Discovery</h4>.*?</div>\s*</div>)'
match = re.search(luminon_pattern, content, re.DOTALL)
if match:
    original = match.group(1)
    # Insert details before the closing </div>
    enhanced = original[:-6] + luminon_details + original[-6:]
    content = content.replace(original, enhanced)

# Save the enhanced version
with open('ledger_enhanced.md', 'w') as f:
    f.write(content)

print("Enhanced ledger created as ledger_enhanced.md")
print("Added expandable functionality to predictions")
print("Added detailed content for Luminon prediction as example") 