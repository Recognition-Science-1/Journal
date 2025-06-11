// Reality Crawler - Layer 4 of Recognition Science Journal
// Autonomous agent that ingests public data streams and validates predictions

class RealityCrawler {
    constructor(truthLedger) {
        this.truthLedger = truthLedger;
        this.dataSources = new Map();
        this.crawlInterval = 30000; // 30 seconds
        this.isRunning = false;
        this.validationQueue = [];
        this.lastCrawlTime = Date.now();
        
        this.initializeDataSources();
    }

    initializeDataSources() {
        // Mock data sources - in production these would be real APIs
        this.dataSources.set('arxiv', {
            url: 'https://export.arxiv.org/api/query',
            type: 'physics_papers',
            lastCheck: Date.now() - 86400000, // 24 hours ago
            parser: this.parseArxivData.bind(this)
        });

        this.dataSources.set('cern', {
            url: 'https://opendata.cern.ch/api/records',
            type: 'particle_data',
            lastCheck: Date.now() - 86400000,
            parser: this.parseCernData.bind(this)
        });

        this.dataSources.set('ligo', {
            url: 'https://www.gw-openscience.org/api',
            type: 'gravitational_waves',
            lastCheck: Date.now() - 86400000,
            parser: this.parseLigoData.bind(this)
        });

        this.dataSources.set('nasa', {
            url: 'https://api.nasa.gov/planetary/apod',
            type: 'cosmological_data',
            lastCheck: Date.now() - 86400000,
            parser: this.parseNasaData.bind(this)
        });

        this.dataSources.set('mock_experiments', {
            url: 'internal://mock',
            type: 'experimental_results',
            lastCheck: Date.now() - 3600000, // 1 hour ago
            parser: this.parseMockExperiments.bind(this)
        });
    }

    start() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        console.log('🤖 Reality Crawler STARTED - Monitoring universe for truth...');
        
        // Start the main crawl loop
        this.crawlLoop();
        
        // Start validation processing
        this.processValidationQueue();
    }

    stop() {
        this.isRunning = false;
        console.log('🤖 Reality Crawler STOPPED');
    }

    async crawlLoop() {
        while (this.isRunning) {
            try {
                await this.crawlAllSources();
                await this.validatePendingPredictions();
                this.lastCrawlTime = Date.now();
                
                // Wait for next crawl
                await this.sleep(this.crawlInterval);
            } catch (error) {
                console.error('Crawl error:', error);
                await this.sleep(5000); // Wait 5 seconds on error
            }
        }
    }

    async crawlAllSources() {
        const crawlPromises = Array.from(this.dataSources.entries()).map(
            ([name, source]) => this.crawlSource(name, source)
        );
        
        await Promise.all(crawlPromises);
    }

    async crawlSource(name, source) {
        try {
            console.log(`🔍 Crawling ${name}...`);
            
            let data;
            if (source.url.startsWith('internal://')) {
                data = await this.generateMockData(source.type);
            } else {
                // In production, this would make real HTTP requests
                data = await this.mockHttpRequest(source.url);
            }
            
            const parsedData = source.parser(data);
            await this.processNewData(name, parsedData);
            
            source.lastCheck = Date.now();
        } catch (error) {
            console.error(`Error crawling ${name}:`, error);
        }
    }

    async generateMockData(type) {
        // Generate realistic mock experimental data
        switch (type) {
            case 'experimental_results':
                return {
                    experiments: [
                        {
                            title: 'Higgs Boson Mass Measurement',
                            value: 125.1,
                            unit: 'GeV',
                            uncertainty: 0.14,
                            confidence: 0.999,
                            timestamp: Date.now(),
                            source: 'LHC-CMS'
                        },
                        {
                            title: 'Muon Magnetic Moment',
                            value: 2.0023318418,
                            unit: 'dimensionless',
                            uncertainty: 0.0000000013,
                            confidence: 0.995,
                            timestamp: Date.now(),
                            source: 'Fermilab-E989'
                        },
                        {
                            title: 'Dark Energy Density',
                            value: 6.91e-30,
                            unit: 'g/cm³',
                            uncertainty: 0.5e-30,
                            confidence: 0.68,
                            timestamp: Date.now(),
                            source: 'Planck-2018'
                        }
                    ]
                };
            default:
                return { data: [] };
        }
    }

    async mockHttpRequest(url) {
        // Mock HTTP request - in production use fetch()
        await this.sleep(100 + Math.random() * 200); // Simulate network delay
        return { status: 'success', data: [] };
    }

    parseArxivData(data) {
        // Parse arXiv papers for relevant physics results
        return {
            type: 'physics_papers',
            count: Math.floor(Math.random() * 50),
            relevantPapers: []
        };
    }

    parseCernData(data) {
        // Parse CERN experimental data
        return {
            type: 'particle_measurements',
            measurements: []
        };
    }

    parseLigoData(data) {
        // Parse LIGO gravitational wave data
        return {
            type: 'gravitational_waves',
            detections: []
        };
    }

    parseNasaData(data) {
        // Parse NASA cosmological data
        return {
            type: 'cosmological_observations',
            observations: []
        };
    }

    parseMockExperiments(data) {
        return {
            type: 'experimental_results',
            experiments: data.experiments || []
        };
    }

    async processNewData(sourceName, parsedData) {
        if (parsedData.type === 'experimental_results') {
            for (const experiment of parsedData.experiments) {
                await this.checkAgainstPredictions(experiment);
            }
        }
    }

    async checkAgainstPredictions(experimentalResult) {
        const predictions = this.truthLedger.getPredictions();
        
        for (const prediction of predictions) {
            if (prediction.status !== 'PENDING') continue;
            
            const match = this.matchExperimentToPrediction(experimentalResult, prediction);
            if (match.isMatch) {
                this.validationQueue.push({
                    prediction: prediction,
                    experiment: experimentalResult,
                    matchScore: match.score,
                    timestamp: Date.now()
                });
            }
        }
    }

    matchExperimentToPrediction(experiment, prediction) {
        // Intelligent matching of experimental results to predictions
        const expTitle = experiment.title.toLowerCase();
        const predContent = prediction.content.toLowerCase();
        
        // Simple keyword matching - in production this would be much more sophisticated
        const keywords = ['higgs', 'muon', 'dark energy', 'mass', 'boson', 'particle'];
        let matchScore = 0;
        
        for (const keyword of keywords) {
            if (expTitle.includes(keyword) && predContent.includes(keyword)) {
                matchScore += 0.2;
            }
        }
        
        // Check for numerical matches
        if (this.hasNumericalMatch(experiment, prediction)) {
            matchScore += 0.5;
        }
        
        return {
            isMatch: matchScore > 0.3,
            score: matchScore
        };
    }

    hasNumericalMatch(experiment, prediction) {
        // Extract numbers from prediction content and compare with experimental value
        const predNumbers = prediction.content.match(/\d+\.?\d*/g);
        if (!predNumbers) return false;
        
        const expValue = experiment.value;
        const expUncertainty = experiment.uncertainty || expValue * 0.01;
        
        for (const numStr of predNumbers) {
            const predValue = parseFloat(numStr);
            if (Math.abs(predValue - expValue) <= expUncertainty * 3) {
                return true;
            }
        }
        
        return false;
    }

    async processValidationQueue() {
        while (this.isRunning) {
            if (this.validationQueue.length > 0) {
                const validation = this.validationQueue.shift();
                await this.validatePrediction(validation);
            }
            await this.sleep(1000); // Check queue every second
        }
    }

    async validatePrediction(validation) {
        const { prediction, experiment, matchScore } = validation;
        
        console.log(`🔬 Validating prediction: ${prediction.content}`);
        console.log(`📊 Against experiment: ${experiment.title} = ${experiment.value} ± ${experiment.uncertainty}`);
        
        // Determine if prediction is verified or refuted
        const isVerified = this.hasNumericalMatch(experiment, prediction) && experiment.confidence > 0.95;
        
        if (isVerified) {
            prediction.status = 'VERIFIED';
            prediction.experimentalData = experiment;
            prediction.accuracy = this.calculateAccuracy(prediction, experiment);
            
            console.log(`✅ VERIFIED: ${prediction.content}`);
            console.log(`📈 Accuracy: ${(prediction.accuracy * 100).toFixed(2)}%`);
            
            // Update in truth ledger
            this.truthLedger.predictionLedger.set(prediction.id, prediction);
            
            // Check if this enables canonization
            this.checkForCanonization(prediction);
            
        } else if (matchScore > 0.5) {
            prediction.status = 'REFUTED';
            prediction.experimentalData = experiment;
            
            console.log(`❌ REFUTED: ${prediction.content}`);
            console.log(`🔍 Experimental result: ${experiment.value} ± ${experiment.uncertainty}`);
            
            // Update in truth ledger
            this.truthLedger.predictionLedger.set(prediction.id, prediction);
            
            // Flag for uncertainty pruning
            this.flagForUncertaintyPruning(prediction);
        }
    }

    calculateAccuracy(prediction, experiment) {
        // Extract predicted value and compare with experimental
        const predNumbers = prediction.content.match(/\d+\.?\d*/g);
        if (!predNumbers) return 0;
        
        let bestAccuracy = 0;
        for (const numStr of predNumbers) {
            const predValue = parseFloat(numStr);
            const error = Math.abs(predValue - experiment.value) / experiment.value;
            const accuracy = Math.max(0, 1 - error);
            bestAccuracy = Math.max(bestAccuracy, accuracy);
        }
        
        return bestAccuracy;
    }

    checkForCanonization(prediction) {
        // Check if prediction has enough verifications for canonization
        const sourceProof = this.truthLedger.proofEngine.get(prediction.sourceProof);
        if (!sourceProof) return;
        
        // Count verified predictions from this proof
        const relatedPredictions = this.truthLedger.getPredictions()
            .filter(p => p.sourceProof === prediction.sourceProof && p.status === 'VERIFIED');
        
        if (relatedPredictions.length >= 3) { // Simplified canonization threshold
            sourceProof.status = 'CANONICAL';
            console.log(`👑 CANONIZED: ${sourceProof.title}`);
        }
    }

    flagForUncertaintyPruning(prediction) {
        // Flag contradictory predictions for uncertainty pruner
        console.log(`🚨 Flagged for uncertainty pruning: ${prediction.content}`);
        // In full implementation, this would trigger Layer 5: Uncertainty Pruner
    }

    getStatus() {
        return {
            isRunning: this.isRunning,
            lastCrawlTime: this.lastCrawlTime,
            dataSources: Array.from(this.dataSources.keys()),
            validationQueueLength: this.validationQueue.length,
            totalValidations: this.getTotalValidations()
        };
    }

    getTotalValidations() {
        const predictions = this.truthLedger.getPredictions();
        return {
            verified: predictions.filter(p => p.status === 'VERIFIED').length,
            refuted: predictions.filter(p => p.status === 'REFUTED').length,
            pending: predictions.filter(p => p.status === 'PENDING').length
        };
    }

    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = RealityCrawler;
} 