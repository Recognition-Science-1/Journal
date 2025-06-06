---
layout: default
title: "Interactive Tools"
---

<div class="tools-hero">
  <div class="container">
    <h1 class="tools-title">Interactive Tools</h1>
    <p class="tools-subtitle">Experience Recognition Science through interactive applications</p>
  </div>
</div>

<section class="tools-section">
  <div class="container">
    <div class="tools-grid">
      <div class="tool-card available">
        <div class="tool-icon">🎵</div>
        <h3 class="tool-name">Golden Ratio Calculator</h3>
        <p class="tool-description">Experience why φ is mathematically inevitable. Interactive audio tool demonstrating harmonic properties of the golden ratio.</p>
        <div class="tool-features">
          <span class="feature-tag">Audio</span>
          <span class="feature-tag">Interactive</span>
          <span class="feature-tag">Mathematical</span>
        </div>
        <a href="phi-calculator" class="tool-launch-btn">Launch Tool</a>
      </div>
      
      <div class="tool-card coming-soon">
        <div class="tool-icon">🔬</div>
        <h3 class="tool-name">Particle Mass Predictor</h3>
        <p class="tool-description">Calculate particle masses using the universal formula E = E_coh × φ^r. Predict masses for all Standard Model particles with 99.877% accuracy.</p>
        <div class="tool-features">
          <span class="feature-tag">Physics</span>
          <span class="feature-tag">Predictions</span>
          <span class="feature-tag">Calculator</span>
        </div>
        <div class="tool-status">Coming Soon</div>
      </div>
      
      <div class="tool-card coming-soon">
        <div class="tool-icon">🧠</div>
        <h3 class="tool-name">Consciousness Threshold</h3>
        <p class="tool-description">Explore consciousness emergence at complexity rung 67. Interactive visualization of how self-awareness emerges from pattern recognition.</p>
        <div class="tool-features">
          <span class="feature-tag">Consciousness</span>
          <span class="feature-tag">Visualization</span>
          <span class="feature-tag">Theory</span>
        </div>
        <div class="tool-status">In Development</div>
      </div>
      
      <div class="tool-card coming-soon">
        <div class="tool-icon">📊</div>
        <h3 class="tool-name">Axiom Visualizer</h3>
        <p class="tool-description">Interactive exploration of the eight foundational axioms. See how discrete recognition, balance, and self-similarity create reality.</p>
        <div class="tool-features">
          <span class="feature-tag">Axioms</span>
          <span class="feature-tag">Educational</span>
          <span class="feature-tag">Interactive</span>
        </div>
        <div class="tool-status">Planned</div>
      </div>
      
      <div class="tool-card coming-soon">
        <div class="tool-icon">🌌</div>
        <h3 class="tool-name">Reality Simulator</h3>
        <p class="tool-description">Simulate the emergence of particles, forces, and consciousness from the eight axioms. Watch the universe unfold from pure mathematics.</p>
        <div class="tool-features">
          <span class="feature-tag">Simulation</span>
          <span class="feature-tag">Universe</span>
          <span class="feature-tag">Advanced</span>
        </div>
        <div class="tool-status">Future Release</div>
      </div>
    </div>
  </div>
</section>

<style>
/* Interactive Tools Page Styling */
.tools-hero {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.tools-title {
  font-size: 3rem;
  font-weight: 600;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
}

.tools-subtitle {
  font-size: 1.25rem;
  opacity: 0.9;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.tools-section {
  padding: 4rem 0;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
}

.tool-card {
  background: white;
  border-radius: 18px;
  padding: 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
}

.tool-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.tool-card.coming-soon {
  opacity: 0.7;
}

.tool-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.tool-name {
  font-size: 1.5rem;
  font-weight: 600;
  margin-bottom: 1rem;
  color: #1d1d1f;
}

.tool-description {
  color: #515154;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.tool-features {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.feature-tag {
  background: #f5f5f7;
  color: #515154;
  padding: 0.25rem 0.75rem;
  border-radius: 12px;
  font-size: 0.875rem;
  font-weight: 500;
}

.tool-launch-btn {
  display: inline-block;
  background: #007aff;
  color: white;
  padding: 12px 24px;
  border-radius: 980px;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.3s ease;
  width: 100%;
  text-align: center;
}

.tool-launch-btn:hover {
  background: #0056cc;
  transform: translateY(-1px);
}

.tool-status {
  background: #86868b;
  color: white;
  padding: 12px 24px;
  border-radius: 980px;
  text-align: center;
  font-weight: 500;
  opacity: 0.8;
}

/* Responsive Design */
@media (max-width: 768px) {
  .tools-grid {
    grid-template-columns: 1fr;
  }
  
  .tools-title {
    font-size: 2rem;
  }
}
</style>
