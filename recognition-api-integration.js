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

    // Update website elements with latest data
    async updateWebsite() {
        console.log('🔄 Updating website with latest Recognition Science data...');

        // Update axioms section
        const axioms = await this.getAxioms();
        if (axioms) {
            this.updateAxiomsSection(axioms);
        }

        // Update predictions display
        const predictions = await this.getPredictions();
        if (predictions.length > 0) {
            this.updatePredictionsSection(predictions);
        }

        // Update theorem status
        const theorems = await this.getTheorems();
        if (theorems.length > 0) {
            this.updateTheoremsSection(theorems);
        }

        // Update validation results
        const validations = await this.getValidationResults();
        if (validations.length > 0) {
            this.updateValidationSection(validations);
        }

        // Update project status
        const status = await this.getProjectStatus();
        if (status) {
            this.updateStatusSection(status);
        }

        console.log('✅ Website updated successfully!');
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

    // Update predictions section
    updatePredictionsSection(predictions) {
        const predictionsContainer = document.getElementById('live-predictions');
        if (predictionsContainer) {
            let html = '<h3>Latest Verified Predictions</h3>';
            predictions.forEach(prediction => {
                html += `
                    <div class="prediction-item">
                        <h4>${prediction.name || 'Prediction'}</h4>
                        <p><strong>Status:</strong> ${prediction.status || 'Unknown'}</p>
                        <p><strong>Value:</strong> ${prediction.predicted_value || 'N/A'}</p>
                        <p><strong>Measured:</strong> ${prediction.measured_value || 'N/A'}</p>
                        <p><strong>Accuracy:</strong> ${prediction.accuracy || 'N/A'}</p>
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