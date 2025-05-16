import os
import PyPDF2
from groq import Groq
from langchain.schema import (
    HumanMessage,
    SystemMessage
)

class PDFProcessor:
    def __init__(self, pdf_path):
        """Initialize the PDF processor with the path to the PDF file."""
        self.pdf_path = pdf_path
        self.text_content = self._extract_text()
        
        # Initialize the Groq client
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Groq API key not found. Please set the GROQ_API_KEY environment variable.")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama3-70b-8192"
    
    def _extract_text(self):
        """Extract text from the PDF file."""
        text = ""
        try:
            with open(self.pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n\n"
                    
            return text
        except Exception as e:
            return f"Error extracting text from PDF: {str(e)}"
    
    def analyze_pdf(self):
        """Analyze the PDF content to determine document type and generate a summary."""
        # Truncate text if it's too long
        max_tokens = 12000  # Adjust based on model limits
        text_to_analyze = self.text_content[:max_tokens] if len(self.text_content) > max_tokens else self.text_content
        
        # Create prompt for document type classification
        type_prompt = f"""You are Suho, an expert PDF analyzer. 
        Analyze the provided PDF content and determine what type of document it is.
        Common document types include: offer letter, educational resource, script, legal document, 
        research paper, report, manual, brochure, invoice, resume, etc.
        Provide only the document type as a short phrase (2-4 words maximum).
        
        Here is the PDF content to analyze:
        
        {text_to_analyze}"""
        
        # Get document type
        type_response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": type_prompt}],
            temperature=0.2,
            max_tokens=20
        )
        doc_type = type_response.choices[0].message.content.strip()
        
        # Create prompt for summary generation
        summary_prompt = f"""You are Suho, an expert PDF analyzer.
        This document has been identified as: {doc_type}.
        Please provide a comprehensive summary of the document, including:
        1. Main topics or sections
        2. Key points or findings
        3. Important details specific to this type of document
        4. Any actionable items or deadlines mentioned
        
        Format your response with appropriate headings, bullet points, and emojis where relevant.
        Make the summary informative but concise.
        
        Here is the PDF content to summarize:
        
        {text_to_analyze}"""
        
        # Get summary
        summary_response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": summary_prompt}],
            temperature=0.2,
            max_tokens=2000
        )
        summary = summary_response.choices[0].message.content.strip()
        
        return doc_type, summary
