// Uncertainty Pruner - Layer 5 of Recognition Science Journal
// Computes minimal axiom subset removal to restore global coherence when contradictions appear

class UncertaintyPruner {
    constructor(truthLedger) {
        this.truthLedger = truthLedger;
        this.contradictions = new Map();
        this.pruningQueue = [];
        this.isRunning = false;
        this.analysisResults = new Map();
        
        console.log('🔍 Uncertainty Pruner initialized');
    }

    start() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        console.log('🔍 Uncertainty Pruner STARTED - Monitoring for contradictions...');
        
        // Start the pruning loop
        this.pruningLoop();
    }

    stop() {
        this.isRunning = false;
        console.log('🔍 Uncertainty Pruner STOPPED');
    }

    async pruningLoop() {
        while (this.isRunning) {
            try {
                await this.detectContradictions();
                await this.processPruningQueue();
                await this.sleep(10000); // Check every 10 seconds
            } catch (error) {
                console.error('Pruning error:', error);
                await this.sleep(5000);
            }
        }
    }

    async detectContradictions() {
        // Check for contradictions between verified predictions
        const predictions = this.truthLedger.getPredictions();
        const verifiedPredictions = predictions.filter(p => p.status === 'VERIFIED');
        
        for (let i = 0; i < verifiedPredictions.length; i++) {
            for (let j = i + 1; j < verifiedPredictions.length; j++) {
                const pred1 = verifiedPredictions[i];
                const pred2 = verifiedPredictions[j];
                
                const contradiction = this.checkForContradiction(pred1, pred2);
                if (contradiction.isContradiction) {
                    await this.flagContradiction(pred1, pred2, contradiction);
                }
            }
        }

        // Check for refuted predictions that contradict axioms
        const refutedPredictions = predictions.filter(p => p.status === 'REFUTED');
        for (const refuted of refutedPredictions) {
            await this.analyzeRefutation(refuted);
        }
    }

    checkForContradiction(pred1, pred2) {
        // Simple contradiction detection - in production this would be much more sophisticated
        const content1 = pred1.content.toLowerCase();
        const content2 = pred2.content.toLowerCase();
        
        // Check for numerical contradictions
        const nums1 = this.extractNumbers(content1);
        const nums2 = this.extractNumbers(content2);
        
        // Check if they're talking about the same thing but with different values
        const commonKeywords = this.findCommonKeywords(content1, content2);
        
        if (commonKeywords.length > 0 && nums1.length > 0 && nums2.length > 0) {
            // Check if the numbers are significantly different
            for (const num1 of nums1) {
                for (const num2 of nums2) {
                    const relativeDiff = Math.abs(num1 - num2) / Math.max(num1, num2);
                    if (relativeDiff > 0.1) { // 10% difference threshold
                        return {
                            isContradiction: true,
                            type: 'numerical_mismatch',
                            confidence: relativeDiff,
                            details: `Values ${num1} and ${num2} differ by ${(relativeDiff * 100).toFixed(1)}%`,
                            commonKeywords: commonKeywords
                        };
                    }
                }
            }
        }

        // Check for logical contradictions
        const logicalContradiction = this.checkLogicalContradiction(content1, content2);
        if (logicalContradiction.isContradiction) {
            return logicalContradiction;
        }

        return { isContradiction: false };
    }

    extractNumbers(text) {
        const matches = text.match(/\d+\.?\d*(?:e[+-]?\d+)?/g);
        return matches ? matches.map(parseFloat) : [];
    }

    findCommonKeywords(text1, text2) {
        const keywords = ['mass', 'energy', 'particle', 'boson', 'electron', 'muon', 'higgs', 'dark', 'constant'];
        return keywords.filter(keyword => text1.includes(keyword) && text2.includes(keyword));
    }

    checkLogicalContradiction(text1, text2) {
        // Check for explicit logical contradictions
        const contradictoryPairs = [
            ['exists', 'does not exist'],
            ['possible', 'impossible'],
            ['stable', 'unstable'],
            ['finite', 'infinite'],
            ['conserved', 'not conserved']
        ];

        for (const [term1, term2] of contradictoryPairs) {
            if (text1.includes(term1) && text2.includes(term2)) {
                return {
                    isContradiction: true,
                    type: 'logical_contradiction',
                    confidence: 0.8,
                    details: `Logical contradiction: "${term1}" vs "${term2}"`
                };
            }
        }

        return { isContradiction: false };
    }

    async flagContradiction(pred1, pred2, contradiction) {
        const contradictionId = `${pred1.id}_${pred2.id}`;
        
        if (this.contradictions.has(contradictionId)) {
            return; // Already flagged
        }

        console.log(`🚨 CONTRADICTION DETECTED: ${contradiction.details}`);
        console.log(`📋 Prediction 1: ${pred1.content}`);
        console.log(`📋 Prediction 2: ${pred2.content}`);

        const contradictionRecord = {
            id: contradictionId,
            predictions: [pred1, pred2],
            type: contradiction.type,
            confidence: contradiction.confidence,
            details: contradiction.details,
            timestamp: Date.now(),
            status: 'FLAGGED',
            analysisResult: null
        };

        this.contradictions.set(contradictionId, contradictionRecord);
        this.pruningQueue.push(contradictionRecord);
    }

    async analyzeRefutation(refutedPrediction) {
        console.log(`🔍 Analyzing refutation: ${refutedPrediction.content}`);
        
        // Find the source proof and its dependencies
        const sourceProof = this.truthLedger.proofEngine.get(refutedPrediction.sourceProof);
        if (!sourceProof) return;

        // Trace back to axioms
        const axiomDependencies = this.traceToAxioms(sourceProof);
        
        const refutationRecord = {
            id: `refutation_${refutedPrediction.id}`,
            refutedPrediction: refutedPrediction,
            sourceProof: sourceProof,
            axiomDependencies: axiomDependencies,
            timestamp: Date.now(),
            status: 'ANALYZING'
        };

        this.pruningQueue.push(refutationRecord);
    }

    traceToAxioms(proof) {
        // Trace proof dependencies back to axioms
        const axioms = [];
        const visited = new Set();
        
        const trace = (dependencies) => {
            for (const dep of dependencies) {
                if (visited.has(dep)) continue;
                visited.add(dep);
                
                if (dep.startsWith('A')) {
                    // This is an axiom
                    axioms.push(dep);
                } else {
                    // This is another proof, trace its dependencies
                    const depProof = this.truthLedger.proofEngine.get(dep);
                    if (depProof && depProof.dependencies) {
                        trace(depProof.dependencies);
                    }
                }
            }
        };

        trace(proof.dependencies || []);
        return axioms;
    }

    async processPruningQueue() {
        while (this.pruningQueue.length > 0) {
            const item = this.pruningQueue.shift();
            await this.analyzeForPruning(item);
        }
    }

    async analyzeForPruning(item) {
        console.log(`🔬 Analyzing for pruning: ${item.id}`);

        if (item.type === 'numerical_mismatch' || item.type === 'logical_contradiction') {
            // Analyze contradiction between two predictions
            const analysis = await this.computeMinimalAxiomRemoval(item);
            item.analysisResult = analysis;
            item.status = 'ANALYZED';
            
            this.analysisResults.set(item.id, analysis);
            
            console.log(`📊 Analysis complete for ${item.id}`);
            console.log(`🎯 Recommended action: ${analysis.recommendation}`);
            
            if (analysis.axiomToRemove) {
                console.log(`⚠️  Suggested axiom removal: ${analysis.axiomToRemove}`);
                await this.flagForCommunityReview(item, analysis);
            }
            
        } else if (item.refutedPrediction) {
            // Analyze refuted prediction
            const analysis = await this.analyzeRefutedPrediction(item);
            item.analysisResult = analysis;
            item.status = 'ANALYZED';
            
            this.analysisResults.set(item.id, analysis);
        }
    }

    async computeMinimalAxiomRemoval(contradiction) {
        // Compute the minimal set of axioms to remove to resolve contradiction
        const pred1 = contradiction.predictions[0];
        const pred2 = contradiction.predictions[1];
        
        // Get axiom dependencies for both predictions
        const proof1 = this.truthLedger.proofEngine.get(pred1.sourceProof);
        const proof2 = this.truthLedger.proofEngine.get(pred2.sourceProof);
        
        const axioms1 = this.traceToAxioms(proof1);
        const axioms2 = this.traceToAxioms(proof2);
        
        // Find common axioms (potential culprits)
        const commonAxioms = axioms1.filter(a => axioms2.includes(a));
        
        // Find unique axioms to each prediction
        const uniqueToFirst = axioms1.filter(a => !axioms2.includes(a));
        const uniqueToSecond = axioms2.filter(a => !axioms1.includes(a));
        
        let recommendation;
        let axiomToRemove = null;
        
        if (commonAxioms.length > 0) {
            // Common axioms might be the issue
            axiomToRemove = commonAxioms[0]; // Choose first common axiom
            recommendation = `Remove common axiom ${axiomToRemove} to resolve contradiction`;
        } else if (uniqueToFirst.length > 0 && uniqueToSecond.length > 0) {
            // Choose the axiom from the less accurate prediction
            const accuracy1 = pred1.accuracy || 0;
            const accuracy2 = pred2.accuracy || 0;
            
            if (accuracy1 < accuracy2) {
                axiomToRemove = uniqueToFirst[0];
                recommendation = `Remove axiom ${axiomToRemove} (from less accurate prediction)`;
            } else {
                axiomToRemove = uniqueToSecond[0];
                recommendation = `Remove axiom ${axiomToRemove} (from less accurate prediction)`;
            }
        } else {
            recommendation = 'Unable to determine minimal axiom removal - requires manual review';
        }

        return {
            contradiction: contradiction,
            axioms1: axioms1,
            axioms2: axioms2,
            commonAxioms: commonAxioms,
            uniqueToFirst: uniqueToFirst,
            uniqueToSecond: uniqueToSecond,
            axiomToRemove: axiomToRemove,
            recommendation: recommendation,
            confidence: this.calculateRemovalConfidence(contradiction, axiomToRemove),
            timestamp: Date.now()
        };
    }

    async analyzeRefutedPrediction(item) {
        const refuted = item.refutedPrediction;
        const axioms = item.axiomDependencies;
        
        return {
            refutedPrediction: refuted,
            axiomDependencies: axioms,
            recommendation: `Review axioms ${axioms.join(', ')} - prediction was refuted by experiment`,
            confidence: 0.7,
            suggestedAction: 'community_review',
            timestamp: Date.now()
        };
    }

    calculateRemovalConfidence(contradiction, axiomToRemove) {
        if (!axiomToRemove) return 0;
        
        let confidence = contradiction.confidence || 0.5;
        
        // Increase confidence for numerical contradictions
        if (contradiction.type === 'numerical_mismatch') {
            confidence += 0.2;
        }
        
        // Decrease confidence for fundamental axioms (A1-A3)
        if (['A1', 'A2', 'A3'].includes(axiomToRemove)) {
            confidence -= 0.3;
        }
        
        return Math.max(0, Math.min(1, confidence));
    }

    async flagForCommunityReview(item, analysis) {
        console.log(`🏛️  FLAGGED FOR COMMUNITY REVIEW: ${item.id}`);
        console.log(`📋 Recommendation: ${analysis.recommendation}`);
        console.log(`🎯 Confidence: ${(analysis.confidence * 100).toFixed(1)}%`);
        
        // In production, this would trigger notifications to the community
        // For now, we'll just log it
        
        item.status = 'COMMUNITY_REVIEW';
        item.reviewTimestamp = Date.now();
    }

    getStatus() {
        return {
            isRunning: this.isRunning,
            contradictionsDetected: this.contradictions.size,
            queueLength: this.pruningQueue.length,
            analysisResults: this.analysisResults.size,
            recentContradictions: this.getRecentContradictions(5)
        };
    }

    getRecentContradictions(limit = 10) {
        const recent = Array.from(this.contradictions.values())
            .sort((a, b) => b.timestamp - a.timestamp)
            .slice(0, limit);
        
        return recent.map(c => ({
            id: c.id,
            type: c.type,
            details: c.details,
            status: c.status,
            timestamp: c.timestamp
        }));
    }

    getAllContradictions() {
        return Array.from(this.contradictions.values());
    }

    getAnalysisResults() {
        return Array.from(this.analysisResults.values());
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = UncertaintyPruner;
} 