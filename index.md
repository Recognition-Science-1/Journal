---
layout: default
title: "Home"
---

<div class="hero-section fade-in">
  <h1 class="hero-title">The Journal of Recognition Science</h1>
  <p class="hero-subtitle">A machine-verifiable ledger where every observable phenomenon is traced—without adjustable constants—to a finite graph of bidirectional recognition axioms.</p>
  <p class="hero-date"><em>May 11, 2025</em></p>
</div>

---


## 🧪 The Eight Foundational Axioms

A1: Discrete Recognition
A2: Dual-Recognition Balance
A3: Positivity of Cost
A4: Unitary Evolution
A5: Irreducible Tick
A6: Irreducible Voxel
A7: Eight-Beat Closure
A8: Self-Similarity

---

## 🚀 Live System Status

<div class="status-grid grid-4">
  <div class="status-card card">
    <h3>🧪 Active Axioms</h3>
    <div class="metric">8</div>
    <div class="sub-metric">+0 this month</div>
  </div>
  
  <div class="status-card card">
    <h3>📊 Truth Packets</h3>
    <div class="metric">42</div>
    <div class="sub-metric">+7 this week</div>
  </div>
  
  <div class="status-card card">
    <h3>🎯 Predictions</h3>
    <div class="metric">156</div>
    <div class="sub-metric">+23 pending</div>
  </div>
  
  <div class="status-card card">
    <h3>✅ Verified</h3>
    <div class="metric">12</div>
    <div class="sub-metric">92% accuracy</div>
  </div>
</div>

<style>
.hero-section {
  text-align: center;
  padding: 3rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 12px;
  margin-bottom: 2rem;
}

.hero-title {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.hero-subtitle {
  font-size: 1.2rem;
  margin-bottom: 1rem;
  opacity: 0.9;
}

.hero-date {
  opacity: 0.8;
}

.status-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin: 2rem 0 3rem 0;
}

.status-card {
  text-align: center;
  transition: transform 0.3s ease;
  background: white;
  border-radius: 12px;
  padding: 2.5rem 2rem;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  border: 1px solid #f0f0f0;
}

.status-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.status-card h3 {
  margin: 0 0 1.5rem 0;
  color: #6c757d;
  font-size: 1rem;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.metric {
  font-size: 3.5rem;
  font-weight: 700;
  color: #007bff;
  margin-bottom: 0.5rem;
  line-height: 1;
}

.sub-metric {
  font-size: 0.9rem;
  color: #28a745;
  font-weight: 500;
}

/* Different colors for different metrics */
.status-card:nth-child(1) .metric { color: #6f42c1; }
.status-card:nth-child(2) .metric { color: #007bff; }
.status-card:nth-child(3) .metric { color: #dc3545; }
.status-card:nth-child(4) .metric { color: #28a745; }

.status-card:nth-child(1) .sub-metric { color: #6c757d; }
.status-card:nth-child(3) .sub-metric { color: #ffc107; }

@media (max-width: 768px) {
  .hero-title {
    font-size: 2rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
  }
  
  .metric {
    font-size: 2.5rem;
  }
  
  .status-grid {
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }
  
  .status-card {
    padding: 2rem 1.5rem;
  }
}

@media (max-width: 480px) {
  .status-grid {
    grid-template-columns: 1fr;
  }
}
</style>
