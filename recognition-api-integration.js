// Recognition Science API Integration
// Automatically pulls data from Jonathan's recognition-ledger repository

class RecognitionAPI {
    constructor() {
        this.baseURL = 'https://api.github.com/repos/jonwashburn/recognition-ledger/contents';
        this.rawURL = 'https://raw.githubusercontent.com/jonwashburn/recognition-ledger/main';
        this.updateInterval = 300000; // 5 minutes
        this.cache = new Map();
    }

    // Fetch data from GitHub API
    async fetchFromRepo(path) {
        try {
            const response = await fetch(`${this.rawURL}/${path}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.text();
        } catch (error) {
            console.error(`Error fetching ${path}:`, error);
            return null;
        }
    }

    // Fetch JSON data (for predictions, validation results)
    async fetchJSON(path) {
        try {
            const response = await fetch(`${this.rawURL}/${path}`);
            if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
            return await response.json();
        } catch (error) {
            console.error(`Error fetching JSON ${path}:`, error);
            return null;
        }
    }

    // Get the 8 foundational axioms
    async getAxioms() {
        const cacheKey = 'axioms';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        const axiomsText = await this.fetchFromRepo('AXIOMS.md');
        if (axiomsText) {
            this.cache.set(cacheKey, axiomsText);
            return axiomsText;
        }
        return null;
    }

    // Get current development roadmap
    async getRoadmap() {
        const cacheKey = 'roadmap';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        const roadmapText = await this.fetchFromRepo('ROADMAP.md');
        if (roadmapText) {
            this.cache.set(cacheKey, roadmapText);
            return roadmapText;
        }
        return null;
    }

    // Get latest predictions and verification status
    async getPredictions() {
        const cacheKey = 'predictions';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        // Try to fetch predictions directory listing
        try {
            const response = await fetch(`${this.baseURL}/predictions`);
            const files = await response.json();
            
            const predictions = [];
            for (const file of files) {
                if (file.name.endsWith('.json')) {
                    const predictionData = await this.fetchJSON(`predictions/${file.name}`);
                    if (predictionData) {
                        predictions.push(predictionData);
                    }
                }
            }
            
            this.cache.set(cacheKey, predictions);
            return predictions;
        } catch (error) {
            console.error('Error fetching predictions:', error);
            return [];
        }
    }

    // Get theorem proofs status
    async getTheorems() {
        const cacheKey = 'theorems';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        try {
            const response = await fetch(`${this.baseURL}/formal`);
            const files = await response.json();
            
            const theorems = [];
            for (const file of files) {
                if (file.name.endsWith('.lean')) {
                    const theoremData = await this.fetchFromRepo(`formal/${file.name}`);
                    if (theoremData) {
                        theorems.push({
                            name: file.name,
                            content: theoremData,
                            lastModified: file.sha
                        });
                    }
                }
            }
            
            this.cache.set(cacheKey, theorems);
            return theorems;
        } catch (error) {
            console.error('Error fetching theorems:', error);
            return [];
        }
    }

    // Get validation results from reality crawler
    async getValidationResults() {
        const cacheKey = 'validation';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        try {
            const response = await fetch(`${this.baseURL}/validation`);
            const files = await response.json();
            
            const validations = [];
            for (const file of files) {
                if (file.name.endsWith('.json')) {
                    const validationData = await this.fetchJSON(`validation/${file.name}`);
                    if (validationData) {
                        validations.push(validationData);
                    }
                }
            }
            
            this.cache.set(cacheKey, validations);
            return validations;
        } catch (error) {
            console.error('Error fetching validation results:', error);
            return [];
        }
    }

    // Get current project status
    async getProjectStatus() {
        const readmeText = await this.fetchFromRepo('README.md');
        if (!readmeText) return null;

        // Parse status from README
        const statusMatch = readmeText.match(/## Current Status\s*([\s\S]*?)(?=##|$)/);
        if (statusMatch) {
            return statusMatch[1].trim();
        }
        return null;
    }

    // Get breakthrough data from new completion files
    async getBreakthroughData() {
        const cacheKey = 'breakthroughs';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        const breakthroughs = {};
        
        // Fetch all the breakthrough status files
        const files = [
            'PROOF_AUTOMATION_COMPLETE.md',
            'SCAFFOLDING_COMPLETE.md', 
            'SETUP_COMPLETE.md',
            'READY_FOR_SOLVERS.md'
        ];

        for (const file of files) {
            const content = await this.fetchFromRepo(file);
            if (content) {
                breakthroughs[file.replace('.md', '')] = content;
            }
        }

        this.cache.set(cacheKey, breakthroughs);
        return breakthroughs;
    }

    // Get solver status and progress
    async getSolverStatus() {
        const cacheKey = 'solver_status';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        try {
            // Try to get recognition progress JSON
            const progressData = await this.fetchJSON('formal/recognition_progress.json');
            if (progressData) {
                this.cache.set(cacheKey, progressData);
                return progressData;
            }
        } catch (error) {
            console.log('No solver progress data yet:', error);
        }

        return null;
    }

    // Get formal proofs (updated to handle new structure)
    async getFormalProofs() {
        const cacheKey = 'formal_proofs';
        if (this.cache.has(cacheKey)) {
            return this.cache.get(cacheKey);
        }

        try {
            const response = await fetch(`${this.baseURL}/formal/proofs`);
            const files = await response.json();
            
            const proofs = [];
            for (const file of files) {
                if (file.name.endsWith('.lean')) {
                    const proofData = await this.fetchFromRepo(`formal/proofs/${file.name}`);
                    if (proofData) {
                        proofs.push({
                            name: file.name,
                            content: proofData,
                            lastModified: file.sha
                        });
                    }
                }
            }
            
            this.cache.set(cacheKey, proofs);
            return proofs;
        } catch (error) {
            console.error('Error fetching formal proofs:', error);
            return [];
        }
    }

    // Update website elements with latest data
    async updateWebsite() {
        console.log('🔄 Updating website with latest Recognition Science data...');

        try {
            // Update breakthrough section first
            const breakthroughs = await this.getBreakthroughData();
            this.updateBreakthroughSection(breakthroughs);

            // Update predictions display
            const predictions = await this.getPredictions();
            this.updatePredictionsSection(predictions);

            // Update theorem status
            const theorems = await this.getTheorems();
            this.updateTheoremsSection(theorems);

            // Update solver section
            const solverStatus = await this.getSolverStatus();
            this.updateSolverSection(solverStatus);

            // Update validation results
            const validations = await this.getValidationResults();
            this.updateValidationSection(validations);

            // Update project status
            const status = await this.getProjectStatus();
            this.updateStatusSection(status);

            // Update axioms section
            const axioms = await this.getAxioms();
            this.updateAxiomsSection(axioms);

            console.log('✅ Website updated successfully!');
        } catch (error) {
            console.error('❌ Error updating website:', error);
            this.showErrorMessage('Unable to load live data from repository');
        }
    }

    // Show error message when API fails
    showErrorMessage(message) {
        const containers = ['live-predictions', 'live-breakthroughs', 'live-solver', 'live-theorems'];
        containers.forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.innerHTML = `<p style="color: #ff6b6b;">⚠️ ${message}</p>`;
            }
        });
    }

    // Update axioms section in the website
    updateAxiomsSection(axiomsText) {
        const axiomsContainer = document.getElementById('live-axioms');
        if (axiomsContainer) {
            // Convert markdown to HTML (basic conversion)
            const htmlContent = this.markdownToHTML(axiomsText);
            axiomsContainer.innerHTML = htmlContent;
        }
    }

    // Update predictions section with new data structure
    updatePredictionsSection(predictions) {
        const predictionsContainer = document.getElementById('live-predictions');
        if (predictionsContainer) {
            if (!predictions || predictions.length === 0) {
                predictionsContainer.innerHTML = `
                    <h3>🎯 VERIFIED PREDICTIONS</h3>
                    <div class="prediction-item" style="border: 2px solid #00ff00; margin: 10px 0; padding: 10px; background: #001a00; color: white;">
                        <h4>Fine Structure Constant (α⁻¹)</h4>
                        <p><strong>Status:</strong> Fetching from repository...</p>
                        <p><strong>Expected:</strong> 137.036 (dimensionless)</p>
                        <p><strong>Repository:</strong> <a href="https://github.com/jonwashburn/recognition-ledger/tree/main/predictions" target="_blank" style="color: #00ff00;">predictions/*.json</a></p>
                    </div>
                    <div class="prediction-item" style="border: 2px solid #00ff00; margin: 10px 0; padding: 10px; background: #001a00; color: white;">
                        <h4>Dark Energy Density</h4>
                        <p><strong>Status:</strong> Loading verification data...</p>
                        <p><strong>Expected:</strong> 2.26 meV</p>
                    </div>
                `;
                return;
            }

            let html = `
                <h3>🎯 VERIFIED PREDICTIONS</h3>
                <p style="color: white;"><strong>Total Verified:</strong> ${predictions.length}</p>
            `;
            
            predictions.forEach(prediction => {
                const verification = prediction.verification || {};
                const pred = prediction.prediction || {};
                
                html += `
                    <div class="prediction-item" style="border: 2px solid #00ff00; margin: 10px 0; padding: 10px; background: #001a00; color: white;">
                        <h4>${pred.observable || prediction.name || 'Prediction'}</h4>
                        <p><strong>Predicted:</strong> ${pred.value || 'N/A'} ${pred.unit || ''}</p>
                        <p><strong>Measured:</strong> ${verification.measurement?.value || 'N/A'} ± ${verification.measurement?.uncertainty || 'N/A'}</p>
                        <p><strong>Accuracy:</strong> ${verification.deviation_percent ? (100 - Math.abs(verification.deviation_percent)).toFixed(4) + '%' : 'N/A'}</p>
                        <p><strong>Status:</strong> <span style="color: #00ff00;">${verification.status || 'Pending'}</span></p>
                        <p><strong>Source:</strong> ${verification.measurement?.source || 'Unknown'}</p>
                    </div>
                `;
            });
            predictionsContainer.innerHTML = html;
        }
    }

    // Update theorems section
    updateTheoremsSection(theorems) {
        const theoremsContainer = document.getElementById('live-theorems');
        if (theoremsContainer) {
            let html = '<h3>Theorem Proofs Status</h3>';
            html += `<p>Total theorems: ${theorems.length}</p>`;
            theorems.forEach(theorem => {
                html += `
                    <div class="theorem-item">
                        <h4>${theorem.name}</h4>
                        <p>Status: Formalized in Lean4</p>
                    </div>
                `;
            });
            theoremsContainer.innerHTML = html;
        }
    }

    // Update validation section
    updateValidationSection(validations) {
        const validationContainer = document.getElementById('live-validation');
        if (validationContainer) {
            let html = '<h3>Reality Crawler Results</h3>';
            validations.forEach(validation => {
                html += `
                    <div class="validation-item">
                        <h4>${validation.source || 'Data Source'}</h4>
                        <p><strong>Last Updated:</strong> ${validation.timestamp || 'Unknown'}</p>
                        <p><strong>Status:</strong> ${validation.status || 'Unknown'}</p>
                    </div>
                `;
            });
            validationContainer.innerHTML = html;
        }
    }

    // Update project status
    updateStatusSection(status) {
        const statusContainer = document.getElementById('live-status');
        if (statusContainer) {
            statusContainer.innerHTML = this.markdownToHTML(status);
        }
    }

    // Update breakthrough section
    updateBreakthroughSection(breakthroughs) {
        const breakthroughContainer = document.getElementById('live-breakthroughs');
        if (breakthroughContainer) {
            if (!breakthroughs || Object.keys(breakthroughs).length === 0) {
                breakthroughContainer.innerHTML = `
                    <h3>🚀 MAJOR BREAKTHROUGHS</h3>
                    <div class="breakthrough-item" style="border: 2px solid #ffff00; margin: 10px 0; padding: 10px; background: #1a1a00; color: white;">
                        <h4>✅ Recognition Science Achievements</h4>
                        <p><strong>Status:</strong> Loading breakthrough data...</p>
                        <p><strong>Repository:</strong> <a href="https://github.com/jonwashburn/recognition-ledger" target="_blank" style="color: #ffff00;">Jonathan's recognition-ledger</a></p>
                        <p>Checking for: PROOF_AUTOMATION_COMPLETE.md, SCAFFOLDING_COMPLETE.md, READY_FOR_SOLVERS.md</p>
                    </div>
                `;
                return;
            }

            let html = '<h3>🚀 MAJOR BREAKTHROUGHS</h3>';
            
            Object.entries(breakthroughs).forEach(([key, content]) => {
                const title = key.replace(/_/g, ' ').toLowerCase().replace(/\b\w/g, l => l.toUpperCase());
                html += `
                    <div class="breakthrough-item" style="border: 2px solid #ffff00; margin: 10px 0; padding: 10px; background: #1a1a00; color: white;">
                        <h4>✅ ${title}</h4>
                        <div style="max-height: 200px; overflow-y: auto;">
                            ${this.markdownToHTML(content.substring(0, 500))}...
                        </div>
                    </div>
                `;
            });
            
            breakthroughContainer.innerHTML = html;
        }
    }

    // Update solver section  
    updateSolverSection(solverStatus) {
        const solverContainer = document.getElementById('live-solver');
        if (solverContainer) {
            let html = '<h3>🤖 AUTONOMOUS SOLVERS</h3>';
            
            if (solverStatus && solverStatus.theorems_proven) {
                html += `
                    <div style="border: 2px solid #ff00ff; margin: 10px 0; padding: 10px; background: #1a001a; color: white;">
                        <p><strong>Theorems Proven:</strong> ${solverStatus.theorems_proven}</p>
                        <p><strong>Success Rate:</strong> ${solverStatus.success_rate || 'N/A'}</p>
                        <p><strong>Last Update:</strong> ${solverStatus.last_updated || 'Unknown'}</p>
                    </div>
                `;
            } else {
                html += `
                    <div style="border: 2px solid #ff00ff; margin: 10px 0; padding: 10px; background: #1a001a; color: white;">
                        <h4>🔍 Solver Status</h4>
                        <p><strong>Repository:</strong> <a href="https://github.com/jonwashburn/recognition-ledger/tree/main/formal" target="_blank" style="color: #ff00ff;">formal/*.py</a></p>
                        <p><strong>Available Solvers:</strong></p>
                        <ul style="margin: 5px 0; padding-left: 20px;">
                            <li>autonomous_recognition_solver.py</li>
                            <li>parallel_five_agent_solver.py</li>
                            <li>ultimate_autonomous_solver.py</li>
                        </ul>
                        <p><strong>Status:</strong> Checking solver progress...</p>
                    </div>
                `;
            }
            
            solverContainer.innerHTML = html;
        }
    }

    // Basic markdown to HTML conversion
    markdownToHTML(markdown) {
        return markdown
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/^## (.*$)/gim, '<h2>$1</h2>')
            .replace(/^# (.*$)/gim, '<h1>$1</h1>')
            .replace(/\*\*(.*)\*\*/gim, '<strong>$1</strong>')
            .replace(/\*(.*)\*/gim, '<em>$1</em>')
            .replace(/\n/gim, '<br>');
    }

    // Start automatic updates
    startAutoUpdate() {
        // Initial update
        this.updateWebsite();
        
        // Set up periodic updates
        setInterval(() => {
            this.cache.clear(); // Clear cache to get fresh data
            this.updateWebsite();
        }, this.updateInterval);
        
        console.log(`🚀 Recognition Science API integration started. Updates every ${this.updateInterval/1000} seconds.`);
    }

    // Clear cache manually
    clearCache() {
        this.cache.clear();
        console.log('🗑️ Cache cleared');
    }
}

// Initialize and export
const recognitionAPI = new RecognitionAPI();

// Auto-start when DOM is loaded
if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => {
        recognitionAPI.startAutoUpdate();
    });
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RecognitionAPI;
}

// Global access
if (typeof window !== 'undefined') {
    window.RecognitionAPI = RecognitionAPI;
    window.recognitionAPI = recognitionAPI;
} 