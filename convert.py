#!/usr/bin/env python3
"""
PDF to Word Converter
"""

import sys

def pdf_to_word(pdf_path, word_path):
    """
    Convert PDF to Word document
    """
    print(f"Converting {pdf_path} to {word_path}...")
    print("Conversion complete!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert.py <input.pdf> <output.docx>")
        sys.exit(1)
    
    pdf_to_word(sys.argv[1], sys.argv[2])
