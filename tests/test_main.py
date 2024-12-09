import pytest
import sys
import os

# Add the src directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the function to test
from main import load_data

# Define the test function
def test_load_data():
    df = load_data()
    print(f"DataFrame shape: {df.shape}")  # Debugging information
    assert not df.empty, "DataFrame should not be empty"
    
