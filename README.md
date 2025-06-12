# Ledger Project - Recognition Science Journal

Welcome to the Ledger project! This is a clean, brutalist-designed website that interfaces with Jonathan Washburn's Recognition Science data.

## 🎯 Project Overview

This project features a minimalist web interface for exploring Recognition Science data, including:
- Truth packets and reality crawling
- System dashboard with live data
- Theory and applications pages
- Widget demonstrations
- **NEW: Live integration with Jonathan's GitHub Lean proofs**

## 📁 Project Structure

### HTML Pages
- `index.html` - Main landing page
- `journal.html` - Journal entries and publications
- `theory.html` - Theoretical foundations
- `applications.html` - Practical applications
- `truth-packets.html` - Truth packet viewer with GitHub integration
- `system-dashboard.html` - Live system metrics and monitoring
- `widget-demo.html` - Widget demonstrations
- `test-github-integration.html` - Test page for GitHub connectivity

### JavaScript Components
- `recognition-api-integration.js` - API connection to Jonathan's GitHub
- `truth-ledger.js` - Core truth packet management system
- `reality-crawler.js` - Autonomous data validation
- `uncertainty-pruner.js` - Contradiction detection and resolution

### Configuration
- `CNAME` - Custom domain configuration
- `.github/` - GitHub Pages deployment settings

## 🔗 GitHub Integration

The system automatically pulls Lean 4 proofs from Jonathan Washburn's repository:
- **Repository**: https://github.com/jonwashburn/recognition-ledger
- **Auto-sync**: Proofs are loaded when pages open
- **Live updates**: New proofs are fetched every 5 minutes
- **Manual refresh**: "LOAD GITHUB PROOFS" button for immediate updates

### Features:
1. **Automatic Proof Loading**: Lean proofs from `/formal` and `/formal/proofs` directories
2. **5-Minute Auto-Sync**: System checks for new proofs every 5 minutes
3. **Real-time Validation**: Reality Crawler validates predictions against experimental data
4. **Contradiction Detection**: Uncertainty Pruner identifies and resolves conflicts
5. **Machine Verification**: All proofs are Lean 4 verified

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd Ledger
   ```

2. **Open locally** 
   - Simply open `index.html` in a web browser
   - For full GitHub integration, you may need to:
     - Use a CORS-disabled browser for testing
     - Deploy to GitHub Pages for production
     - Run a local server with CORS proxy

3. **Test GitHub Integration**
   - Open `test-github-integration.html` to verify connectivity
   - Check the system dashboard for live proof loading status

## 📊 System Architecture

The Journal implements a 6-layer verification system:

1. **Axiom Store**: 8 foundational Recognition Science axioms
2. **Proof Engine**: Lean 4 verified proofs (live from GitHub)
3. **Prediction Ledger**: Quantitative predictions tracked automatically
4. **Reality Crawler**: Monitors experimental data for validation
5. **Uncertainty Pruner**: Resolves contradictions in real-time
6. **Policy Firewall**: (Coming soon) Ethics review for sensitive predictions

## 🔬 Recognition Science Framework

This system implements Jonathan Washburn's parameter-free theory where:
- All physical constants emerge from 8 axioms with ZERO free parameters
- The golden ratio φ determines the mass spectrum
- Reality operates as a self-balancing ledger
- Machine-verified proofs ensure mathematical certainty

## 📝 Contributing

To add new content or features:
1. Follow the brutalist design aesthetic
2. Ensure all proofs are Lean 4 verifiable
3. Test GitHub integration before committing
4. Update relevant documentation

## 🌐 Live Demo

Visit the GitHub Pages deployment for the full experience with working API integration.

---

*Building the future of parameter-free physics, one truth packet at a time.*

## 📦 Archived Content

Previous work and legacy files have been moved to the `archived/` folder for reference.

## 🔧 Development

To make changes:
1. Edit the HTML/JS files directly
2. Commit and push to the main branch
3. GitHub Pages will automatically deploy updates

---

*Clean slate for new team members - June 2024* 