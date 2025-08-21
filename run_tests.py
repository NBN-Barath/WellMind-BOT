#!/usr/bin/env python3
"""
Simple Test Runner for WellMind AI Chatbot
"""

import unittest
import sys

def main():
    """Run the test suite."""
    print("🧪 Running WellMind AI Tests...")
    print("-" * 40)
    
    # Load and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromName('test_wellmind_ai')
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print results
    print("-" * 40)
    if result.failures or result.errors:
        print(f"❌ {len(result.failures)} failures, {len(result.errors)} errors")
        sys.exit(1)
    else:
        print(f"✅ All {result.testsRun} tests passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()