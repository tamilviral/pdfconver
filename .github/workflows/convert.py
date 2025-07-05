#!/usr/bin/env python3
from pdf2docx import Converter
import sys
import os

def convert_pdf_to_word(pdf_path, docx_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
        return True
    except Exception as e:
        print(f"Conversion failed: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.pdf output.docx")
        sys.exit(1)
    
    input_pdf = sys.argv[1]
    output_docx = sys.argv[2]
    
    if not os.path.exists(input_pdf):
        print(f"Input file {input_pdf} not found")
        sys.exit(1)
    
    if convert_pdf_to_word(input_pdf, output_docx):
        print(f"Successfully converted {input_pdf} to {output_docx}")
    else:
        print("Conversion failed")
        sys.exit(1)
