/**
 * Golden Ratio Audio Engine
 * Phase 1, Step 1.2: Audio Generation
 * 
 * Uses Web Audio API to generate and play phi-based harmonic intervals
 * for Recognition Science musical integration.
 */

class PhiHarmonics {
    constructor() {
        this.audioContext = null;
        this.masterGain = null;
        this.isInitialized = false;
        this.activeOscillators = [];
        
        // Golden ratio - mathematically inevitable!
        this.PHI = (1 + Math.sqrt(5)) / 2;  // 1.618034...
        
        console.log('🎼 PhiHarmonics Audio Engine initialized');
        console.log(`φ = ${this.PHI}`);
    }
    
    /**
     * Initialize the Web Audio API context
     * Must be called after user interaction due to browser autoplay policies
     */
    async initAudio() {
        try {
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            
            // Create master gain node for volume control
            this.masterGain = this.audioContext.createGain();
            this.masterGain.connect(this.audioContext.destination);
            this.masterGain.gain.setValueAtTime(0.3, this.audioContext.currentTime);
            
            this.isInitialized = true;
            console.log('🎵 Audio context initialized successfully');
            return true;
        } catch (error) {
            console.error('❌ Failed to initialize audio context:', error);
            return false;
        }
    }
    
    /**
     * Play a single frequency tone
     * @param {number} frequency - Frequency in Hz
     * @param {number} duration - Duration in milliseconds
     * @param {string} waveType - Oscillator wave type ('sine', 'square', 'sawtooth', 'triangle')
     */
    async playTone(frequency, duration = 1000, waveType = 'sine') {
        if (!this.isInitialized) {
            await this.initAudio();
        }
        
        if (!this.audioContext) {
            console.error('❌ Audio context not available');
            return;
        }
        
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();
        
        // Configure oscillator
        oscillator.type = waveType;
        oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
        
        // Configure envelope (attack, sustain, release)
        const now = this.audioContext.currentTime;
        const attackTime = 0.1;
        const releaseTime = 0.3;
        const sustainTime = (duration / 1000) - attackTime - releaseTime;
        
        gainNode.gain.setValueAtTime(0, now);
        gainNode.gain.linearRampToValueAtTime(0.5, now + attackTime);
        gainNode.gain.setValueAtTime(0.5, now + attackTime + sustainTime);
        gainNode.gain.linearRampToValueAtTime(0, now + attackTime + sustainTime + releaseTime);
        
        // Connect nodes
        oscillator.connect(gainNode);
        gainNode.connect(this.masterGain);
        
        // Start and stop
        oscillator.start(now);
        oscillator.stop(now + (duration / 1000));
        
        // Track active oscillators
        this.activeOscillators.push(oscillator);
        
        // Clean up when done
        oscillator.onended = () => {
            const index = this.activeOscillators.indexOf(oscillator);
            if (index > -1) {
                this.activeOscillators.splice(index, 1);
            }
        };
        
        console.log(`🎵 Playing ${frequency.toFixed(2)} Hz for ${duration}ms`);
    }
    
    /**
     * Calculate phi-based harmonic intervals
     * @param {number} baseFreq - Base frequency in Hz
     * @returns {Array} Array of frequencies
     */
    calculatePhiIntervals(baseFreq = 440) {
        const intervals = [];
        
        // Generate 8 intervals using phi relationships
        for (let i = 0; i < 8; i++) {
            const freq = baseFreq * Math.pow(this.PHI, i / 4);
            intervals.push(freq);
        }
        
        return intervals;
    }
    
    /**
     * Calculate pure phi ratio frequencies
     * @param {number} baseFreq - Base frequency in Hz
     * @returns {Array} Array of frequencies
     */
    calculatePurePhiRatios(baseFreq = 440) {
        const ratios = [];
        
        // Pure phi powers: 1, φ, φ², φ³, etc.
        for (let power = 0; power < 8; power++) {
            const ratio = Math.pow(this.PHI, power);
            const freq = baseFreq * ratio;
            ratios.push(freq);
        }
        
        return ratios;
    }
    
    /**
     * Play a sequence of phi-based intervals
     * @param {number} baseFreq - Base frequency in Hz
     * @param {string} mode - 'intervals', 'pure', or 'equal'
     * @param {number} noteDuration - Duration of each note in ms
     */
    async playPhiScale(baseFreq = 440, mode = 'intervals', noteDuration = 800) {
        let frequencies;
        
        switch (mode) {
            case 'pure':
                frequencies = this.calculatePurePhiRatios(baseFreq);
                console.log('🎼 Playing Pure Phi Ratios');
                break;
            case 'equal':
                frequencies = this.calculateEqualTemperamentMapping(baseFreq);
                console.log('🎼 Playing Equal Temperament Mapping');
                break;
            default:
                frequencies = this.calculatePhiIntervals(baseFreq);
                console.log('🎼 Playing Phi Intervals');
        }
        
        console.log(`🎵 Base frequency: ${baseFreq} Hz`);
        console.log(`🎵 Scale frequencies:`, frequencies.map(f => f.toFixed(2)));
        
        // Play each note in sequence
        for (let i = 0; i < frequencies.length; i++) {
            setTimeout(() => {
                this.playTone(frequencies[i], noteDuration * 0.8, 'sine');
            }, i * noteDuration);
        }
    }
    
    /**
     * Play a phi-based chord (multiple frequencies simultaneously)
     * @param {number} baseFreq - Base frequency in Hz
     * @param {Array} intervals - Array of interval indices to play
     * @param {number} duration - Duration in ms
     */
    async playPhiChord(baseFreq = 440, intervals = [0, 2, 4], duration = 2000) {
        const frequencies = this.calculatePhiIntervals(baseFreq);
        
        console.log('🎼 Playing Phi Chord');
        console.log(`🎵 Frequencies:`, intervals.map(i => frequencies[i].toFixed(2)));
        
        // Play all notes simultaneously
        intervals.forEach(i => {
            if (i < frequencies.length) {
                this.playTone(frequencies[i], duration, 'sine');
            }
        });
    }
    
    /**
     * Calculate equal temperament mapping for phi relationships
     * @param {number} baseFreq - Base frequency in Hz
     * @returns {Array} Array of frequencies
     */
    calculateEqualTemperamentMapping(baseFreq = 440) {
        const intervals = [];
        
        // Map phi ratios to semitone steps
        const phiSemitones = [0, 2, 4, 7, 9, 11, 12, 14];
        
        phiSemitones.forEach(semitones => {
            const freq = baseFreq * Math.pow(2, semitones / 12);
            intervals.push(freq);
        });
        
        return intervals;
    }
    
    /**
     * Stop all currently playing oscillators
     */
    stopAll() {
        this.activeOscillators.forEach(osc => {
            try {
                osc.stop();
            } catch (e) {
                // Oscillator might already be stopped
            }
        });
        this.activeOscillators = [];
        console.log('🔇 All audio stopped');
    }
    
    /**
     * Set master volume
     * @param {number} volume - Volume level (0.0 to 1.0)
     */
    setVolume(volume) {
        if (this.masterGain) {
            this.masterGain.gain.setValueAtTime(volume, this.audioContext.currentTime);
            console.log(`🔊 Volume set to ${(volume * 100).toFixed(0)}%`);
        }
    }
    
    /**
     * Get frequency info for display
     * @param {number} frequency - Frequency in Hz
     * @returns {Object} Frequency info with note name
     */
    getFrequencyInfo(frequency) {
        const A4 = 440;
        const noteNames = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
        
        // Calculate semitones from A4
        const semitonesFromA4 = 12 * Math.log2(frequency / A4);
        
        // A4 is 9 semitones above C4
        const semitonesFromC = semitonesFromA4 + 9;
        
        // Calculate octave and note
        const octave = Math.floor(semitonesFromC / 12) + 4;
        const noteIndex = Math.floor(semitonesFromC % 12);
        
        return {
            frequency: frequency.toFixed(2),
            note: `${noteNames[noteIndex]}${octave}`,
            cents: ((semitonesFromC % 1) * 100).toFixed(0)
        };
    }
}

// Global instance for easy access
window.phiHarmonics = new PhiHarmonics();

console.log('🎸 Golden Ratio Audio Engine loaded! Ready to make φ sing!');
console.log('🎵 Usage: phiHarmonics.playPhiScale() or phiHarmonics.playTone(440)'); 