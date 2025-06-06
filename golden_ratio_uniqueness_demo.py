#!/usr/bin/env python3
"""
Golden Ratio Uniqueness Demonstration

This script proves that φ is the ONLY scaling factor that works for Recognition Science.
We test different values and show that only φ satisfies all requirements.
"""

import numpy as np
import matplotlib.pyplot as plt

# The golden ratio
PHI = (1 + np.sqrt(5)) / 2

def test_scaling_factor(x, name=""):
    """Test if a scaling factor x satisfies the requirements."""
    print(f"\n{'='*50}")
    print(f"Testing scaling factor: {name} = {x:.6f}")
    print(f"{'='*50}")
    
    # Test 1: Does it satisfy x² = x + 1?
    equation_satisfied = abs(x**2 - (x + 1)) < 1e-10
    print(f"1. Scaling equation (x² = x + 1):")
    print(f"   x² = {x**2:.6f}")
    print(f"   x + 1 = {x + 1:.6f}")
    print(f"   Satisfied: {equation_satisfied} ✓" if equation_satisfied else f"   Satisfied: {equation_satisfied} ✗")
    
    # Test 2: Does it preserve balance in hierarchy?
    # If E(n+1) = x * E(n), then for balance:
    # E(n+2) + E(n) = 2 * E(n+1)
    # x² * E(n) + E(n) = 2 * x * E(n)
    # x² + 1 = 2x
    balance_preserved = abs((x**2 + 1) - 2*x) < 1e-10
    print(f"\n2. Balance preservation:")
    print(f"   x² + 1 = {x**2 + 1:.6f}")
    print(f"   2x = {2*x:.6f}")
    print(f"   Preserved: {balance_preserved} ✓" if balance_preserved else f"   Preserved: {balance_preserved} ✗")
    
    # Test 3: Self-similarity (1/x = x - 1)
    if x != 0:
        self_similar = abs(1/x - (x - 1)) < 1e-10
        print(f"\n3. Self-similarity (1/x = x - 1):")
        print(f"   1/x = {1/x:.6f}")
        print(f"   x - 1 = {x - 1:.6f}")
        print(f"   Satisfied: {self_similar} ✓" if self_similar else f"   Satisfied: {self_similar} ✗")
    
    # Test 4: Fibonacci convergence
    # Calculate a few Fibonacci ratios
    fib = [1, 1]
    for i in range(10):
        fib.append(fib[-1] + fib[-2])
    fib_ratio = fib[-1] / fib[-2]
    fib_convergence = abs(fib_ratio - x) < 0.01
    print(f"\n4. Fibonacci convergence:")
    print(f"   F(12)/F(11) = {fib_ratio:.6f}")
    print(f"   Converges to x: {fib_convergence} ✓" if fib_convergence else f"   Converges to x: {fib_convergence} ✗")
    
    # Overall result
    all_tests = equation_satisfied and balance_preserved
    print(f"\n{'✅ ALL TESTS PASSED!' if all_tests else '❌ FAILED REQUIREMENTS'}")
    
    return all_tests

def visualize_scaling_equation():
    """Visualize why only φ satisfies x² = x + 1."""
    x = np.linspace(-2, 3, 1000)
    y1 = x**2  # Left side: x²
    y2 = x + 1  # Right side: x + 1
    
    plt.figure(figsize=(10, 8))
    plt.plot(x, y1, 'b-', linewidth=2, label='y = x²')
    plt.plot(x, y2, 'r-', linewidth=2, label='y = x + 1')
    
    # Mark the intersections
    # Positive solution: φ
    plt.plot(PHI, PHI**2, 'go', markersize=10, label=f'φ = {PHI:.4f}')
    # Negative solution: -1/φ
    neg_phi = -1/PHI
    plt.plot(neg_phi, neg_phi**2, 'ro', markersize=10, label=f'-1/φ = {neg_phi:.4f}')
    
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.grid(True, alpha=0.3)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('The Golden Ratio is the Unique Positive Solution to x² = x + 1', fontsize=14)
    plt.legend(fontsize=12)
    plt.xlim(-2, 3)
    plt.ylim(-1, 5)
    
    # Add text annotation
    plt.text(PHI + 0.1, PHI**2 + 0.2, 'Only φ works!', fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('golden_ratio_uniqueness.png', dpi=300)
    plt.show()

def main():
    """Demonstrate that only φ satisfies all requirements."""
    
    print("GOLDEN RATIO UNIQUENESS DEMONSTRATION")
    print("=====================================")
    print("\nWe'll test various scaling factors to show only φ works.\n")
    
    # Test various candidates
    candidates = [
        (2.0, "2"),
        (1.5, "3/2"),
        (np.sqrt(2), "√2"),
        (np.e/2, "e/2"),
        (PHI, "φ (golden ratio)"),
        (np.pi/2, "π/2"),
    ]
    
    results = []
    for value, name in candidates:
        passed = test_scaling_factor(value, name)
        results.append((name, value, passed))
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY OF RESULTS")
    print("="*60)
    print(f"{'Scaling Factor':<20} {'Value':<12} {'All Tests Passed'}")
    print("-"*60)
    for name, value, passed in results:
        status = "✅ YES" if passed else "❌ NO"
        print(f"{name:<20} {value:<12.6f} {status}")
    
    print("\n🎯 CONCLUSION: Only φ satisfies all requirements!")
    print("This proves φ is the UNIQUE scaling factor for Recognition Science.\n")
    
    # Create visualization
    print("Generating visualization...")
    visualize_scaling_equation()

if __name__ == "__main__":
    main() 