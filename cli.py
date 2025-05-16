#!/usr/bin/env python3
import os
import sys
import argparse
from dotenv import load_dotenv
from pdf_processor import PDFProcessor

def main():
    # Load environment variables
    load_dotenv()
    
    # Check if GROQ_API_KEY is set
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY environment variable is not set.")
        print("Please set it in the .env file or export it in your shell.")
        sys.exit(1)
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Suho PDF Reader - Analyze and summarize PDF documents")
    parser.add_argument("pdf_path", help="Path to the PDF file to analyze")
    args = parser.parse_args()
    
    # Check if the file exists
    if not os.path.exists(args.pdf_path):
        print(f"Error: File '{args.pdf_path}' does not exist.")
        sys.exit(1)
    
    # Check if the file is a PDF
    if not args.pdf_path.lower().endswith('.pdf'):
        print(f"Error: File '{args.pdf_path}' is not a PDF file.")
        sys.exit(1)
    
    print(f"🔍 Analyzing PDF: {args.pdf_path}")
    print("⏳ This may take a moment...")
    
    try:
        # Process the PDF
        processor = PDFProcessor(args.pdf_path)
        doc_type, summary = processor.analyze_pdf()
        
        # Display results
        print("\n" + "="*80)
        print(f"📑 Document Type: {doc_type}")
        print("="*80)
        print("\n📝 Summary:")
        print(summary)
        print("\n" + "="*80)
        
    except Exception as e:
        print(f"❌ Error processing PDF: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
