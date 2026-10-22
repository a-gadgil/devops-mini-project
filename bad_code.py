# test_bad_code.py
import os  # Unused import -> Flake8 will fail on F401

def hello():
    x = 1 # Indentation or spacing issue
    print("Hello World")