---
layout: page
title: "Submit Research"
permalink: /submit/
---

# Submit Research to the Journal

> **Upload your axioms, proofs, and predictions to humanity's ledger of reality**

---

## 🚀 Quick Start

Ready to contribute to the Recognition Science ledger? Choose your submission method:

<div class="submission-options">
  <div class="option-card primary">
    <h3>🌐 Web Submission</h3>
    <p>Use our guided web form for easy submission</p>
    <a href="#web-form" class="btn btn-primary">Start Submission</a>
  </div>
  
  <div class="option-card">
    <h3>💻 GitHub Pull Request</h3>
    <p>Submit directly via GitHub for technical users</p>
    <a href="https://github.com/Recognition-Science-1/Journal/pulls" class="btn btn-secondary">Create PR</a>
  </div>
  
  <div class="option-card">
    <h3>🔧 API Submission</h3>
    <p>Programmatic submission for automated systems</p>
    <a href="#api-docs" class="btn btn-secondary">View API</a>
  </div>
</div>

---

## 📋 Submission Requirements

Before submitting, ensure your research meets our **core principles**:

### ✅ **MUST HAVE (Non-negotiable)**

- [ ] **Mathematical Formalization**: All claims formalized in Lean 4 with complete proofs
- [ ] **Zero Free Parameters**: No adjustable constants introduced
- [ ] **Experimental Predictions**: Specific, falsifiable predictions with error bounds
- [ ] **Reproducible Code**: All calculations in executable form
- [ ] **Falsification Criteria**: Clear statement of what would falsify the theory

### 🌟 **SHOULD HAVE (Strongly Recommended)**

- [ ] **Educational Materials**: Intuitive explanations alongside formal proofs
- [ ] **Historical Context**: Connection to existing physics knowledge
- [ ] **Computational Tools**: Interactive calculators or visualizations

---

## 📝 Web Submission Form {#web-form}

<form class="submission-form" action="/api/v1/submissions" method="POST">
  
  ### **Submission Details**
  
  <div class="form-group">
    <label for="title">**Title**</label>
    <input type="text" id="title" name="title" placeholder="Your Discovery/Theorem Title" required>
  </div>
  
  <div class="form-group">
    <label for="authors">**Authors**</label>
    <textarea id="authors" name="authors" placeholder="Primary Author: Name, Affiliation, Email&#10;Contributors: Names, Affiliations" required></textarea>
  </div>
  
  <div class="form-group">
    <label for="submission_type">**Submission Type**</label>
    <select id="submission_type" name="submission_type" required>
      <option value="">Select submission type...</option>
      <option value="particle_prediction">🔬 New Particle Prediction</option>
      <option value="coupling_constant">⚡ Coupling Constant Derivation</option>
      <option value="cosmological_parameter">🌌 Cosmological Parameter</option>
      <option value="mathematical_theorem">📐 Mathematical Theorem</option>
      <option value="experimental_validation">🧪 Experimental Validation</option>
      <option value="other">Other</option>
    </select>
  </div>
  
  ### **Core Contribution**
  
  <div class="form-group">
    <label for="abstract">**Abstract** (150 words max)</label>
    <textarea id="abstract" name="abstract" placeholder="Concise summary of what you've discovered/proved" maxlength="750" required></textarea>
  </div>
  
  <div class="form-group">
    <label for="main_claim">**Main Claim**</label>
    <input type="text" id="main_claim" name="main_claim" placeholder="One sentence statement of your primary result" required>
  </div>
  
  <div class="form-group">
    <label for="numerical_prediction">**Numerical Prediction**</label>
    <input type="text" id="numerical_prediction" name="numerical_prediction" placeholder="Specific value with error bounds">
  </div>
  
  ### **Mathematical Formalization**
  
  <div class="form-group">
    <label for="lean_files">**Lean 4 Files**</label>
    <input type="file" id="lean_files" name="lean_files" multiple accept=".lean" required>
    <small>Upload your .lean formalization files</small>
  </div>
  
  <div class="form-group">
    <label for="axiom_dependencies">**Axiom Dependencies**</label>
    <div class="checkbox-group">
      <label><input type="checkbox" name="axioms" value="A1"> A1: Discrete Recognition</label>
      <label><input type="checkbox" name="axioms" value="A2"> A2: Dual-Recognition Balance</label>
      <label><input type="checkbox" name="axioms" value="A3"> A3: Positivity of Recognition Cost</label>
      <label><input type="checkbox" name="axioms" value="A4"> A4: Unitary Ledger Evolution</label>
      <label><input type="checkbox" name="axioms" value="A5"> A5: Irreducible Tick Interval</label>
      <label><input type="checkbox" name="axioms" value="A6"> A6: Irreducible Spatial Voxel</label>
      <label><input type="checkbox" name="axioms" value="A7"> A7: Eight-Beat Closure</label>
      <label><input type="checkbox" name="axioms" value="A8"> A8: Self-Similarity of Recognition</label>
    </div>
  </div>
  
  ### **Computational Verification**
  
  <div class="form-group">
    <label for="code_files">**Code Files**</label>
    <input type="file" id="code_files" name="code_files" multiple accept=".py,.lean,.ipynb">
    <small>Upload calculation and verification scripts</small>
  </div>
  
  <div class="form-group">
    <label for="dependencies">**Dependencies**</label>
    <textarea id="dependencies" name="dependencies" placeholder="List all required packages/versions"></textarea>
  </div>
  
  ### **Experimental Validation**
  
  <div class="form-group">
    <label for="experimental_status">**Current Status**</label>
    <select id="experimental_status" name="experimental_status">
      <option value="measured">Measured: Has experimental value</option>
      <option value="unmeasured">Unmeasured: Prediction awaiting test</option>
      <option value="partial">Partially measured: Explain status</option>
    </select>
  </div>
  
  <div class="form-group">
    <label for="falsification_criteria">**Falsification Criteria**</label>
    <textarea id="falsification_criteria" name="falsification_criteria" placeholder="This result would be falsified if..." required></textarea>
  </div>
  
  ### **Submission Statement**
  
  <div class="form-group">
    <div class="checkbox-group">
      <label><input type="checkbox" name="certifications" value="no_parameters" required> This work contains no adjustable parameters</label>
      <label><input type="checkbox" name="certifications" value="reproducible" required> All numerical results are reproducible</label>
      <label><input type="checkbox" name="certifications" value="complete" required> The mathematical formalization is complete</label>
      <label><input type="checkbox" name="certifications" value="falsifiable" required> Experimental predictions are falsifiable</label>
      <label><input type="checkbox" name="certifications" value="limitations" required> I have disclosed all known limitations</label>
      <label><input type="checkbox" name="certifications" value="original" required> This represents original work</label>
    </div>
  </div>
  
  <div class="form-group">
    <button type="submit" class="btn btn-primary btn-large">Submit to Recognition Science Ledger</button>
  </div>
  
</form>

---

## 🔧 API Documentation {#api-docs}

For programmatic submissions, use our REST API:

### **Authentication**
```bash
# Get API token
curl -X POST https://api.recognitionscience.org/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

### **Submit Truth Packet**
```bash
curl -X POST https://api.recognitionscience.org/v1/submissions \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Electron Mass from Golden Cascade",
    "authors": [{"name": "Your Name", "email": "you@example.com"}],
    "type": "particle_prediction",
    "abstract": "We derive the electron mass...",
    "main_claim": "Electron mass = E_coh × φ^32",
    "axiom_dependencies": ["A1", "A2", "A3"],
    "lean_files": ["base64_encoded_content"],
    "predictions": [{
      "value": 0.51099895,
      "uncertainty": 0.00000015,
      "units": "MeV",
      "description": "Electron rest mass"
    }]
  }'
```

### **Check Submission Status**
```bash
curl -X GET https://api.recognitionscience.org/v1/submissions/{submission_id} \
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

## 🔄 Review Process

Once submitted, your research enters our **4-stage review process**:

### **Stage 1: Automated Checks** (< 5 minutes)
- ✅ Lean 4 compilation verification
- ✅ Code execution testing  
- ✅ Dimensional analysis
- ✅ Numerical precision validation

### **Stage 2: Mathematical Review** (1-2 weeks)
- 🔍 Proof correctness verification
- 🔍 Axiom consistency checking
- 🔍 Logical flow validation
- 🔍 Completeness assessment

### **Stage 3: Physics Review** (2-4 weeks)
- 🔬 Experimental comparison
- 🔬 Physical reasonableness
- 🔬 Testability evaluation
- 🔬 Impact assessment

### **Stage 4: Community Review** (30 days)
- 💬 Public comment period
- 💬 Response to criticisms
- 💬 Revision if necessary
- 💬 Final approval vote

---

## 📊 Submission Statistics

<div class="stats-grid">
  <div class="stat-card">
    <h4>📝 Total Submissions</h4>
    <div class="stat-value">127</div>
    <div class="stat-detail">+15 this month</div>
  </div>
  
  <div class="stat-card">
    <h4>✅ Accepted</h4>
    <div class="stat-value">42</div>
    <div class="stat-detail">33% acceptance rate</div>
  </div>
  
  <div class="stat-card">
    <h4>⏱️ Avg Review Time</h4>
    <div class="stat-value">18 days</div>
    <div class="stat-detail">Getting faster</div>
  </div>
  
  <div class="stat-card">
    <h4>🎯 Verified Predictions</h4>
    <div class="stat-value">12</div>
    <div class="stat-detail">92% accuracy</div>
  </div>
</div>

---

## 💡 Submission Tips

### **For First-Time Contributors**
1. Start with our [submission template](/Journal/SUBMISSION_TEMPLATE.md)
2. Review [best practices](/Journal/JOURNAL_BEST_PRACTICES.md)
3. Check existing submissions for examples
4. Join our community Discord for help

### **For Experienced Users**
1. Use the GitHub API for batch submissions
2. Set up automated testing pipelines
3. Contribute to review process
4. Help mentor new contributors

---

## 🤝 Need Help?

- 📚 **Documentation**: [Best Practices Guide](/Journal/JOURNAL_BEST_PRACTICES.md)
- 💬 **Community**: [Discord Server](https://discord.gg/recognitionscience)
- 📧 **Support**: submit@recognitionscience.org
- 🐛 **Issues**: [GitHub Issues](https://github.com/Recognition-Science-1/Journal/issues)

---

**Ready to contribute to humanity's ledger of reality?**

[Start Your Submission](#web-form){: .btn .btn-primary .btn-large}

<style>
.submission-options {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.option-card {
  background: #f8f9fa;
  border: 2px solid #e9ecef;
  border-radius: 12px;
  padding: 2rem;
  text-align: center;
  transition: all 0.3s ease;
}

.option-card.primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: #667eea;
}

.option-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
}

.option-card h3 {
  margin: 0 0 1rem 0;
}

.option-card p {
  margin: 0 0 1.5rem 0;
  opacity: 0.8;
}

.submission-form {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 12px;
  margin: 2rem 0;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.form-group input,
.form-group textarea,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
}

.form-group textarea {
  min-height: 100px;
  resize: vertical;
}

.form-group small {
  display: block;
  margin-top: 0.25rem;
  color: #666;
  font-size: 0.875rem;
}

.checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.checkbox-group label {
  display: flex;
  align-items: center;
  font-weight: normal;
  margin-bottom: 0;
}

.checkbox-group input[type="checkbox"] {
  width: auto;
  margin-right: 0.5rem;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s;
}

.btn:hover {
  background: #0056b3;
  color: white;
  text-decoration: none;
}

.btn-primary {
  background: #007bff;
}

.btn-secondary {
  background: #6c757d;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.1rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}

.stat-card {
  background: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
}

.stat-card h4 {
  margin: 0 0 1rem 0;
  color: #495057;
  font-size: 1rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #007bff;
  margin-bottom: 0.5rem;
}

.stat-detail {
  font-size: 0.8rem;
  color: #28a745;
}
</style> 