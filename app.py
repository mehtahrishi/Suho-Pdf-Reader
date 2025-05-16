from flask import Flask, render_template, request, jsonify
import os
import tempfile
from dotenv import load_dotenv
from pdf_processor import PDFProcessor

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Check if the post request has the file part
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['pdf']
    
    # If user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Check if the file is a PDF
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'File must be a PDF'}), 400
    
    try:
        # Save the file temporarily
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
        file.save(temp_file.name)
        temp_file.close()
        
        # Process the PDF
        processor = PDFProcessor(temp_file.name)
        doc_type, summary = processor.analyze_pdf()
        
        # Clean up
        os.unlink(temp_file.name)
        
        return jsonify({
            'doc_type': doc_type,
            'summary': summary
        })
    
    except Exception as e:
        # Clean up in case of error
        if 'temp_file' in locals() and os.path.exists(temp_file.name):
            os.unlink(temp_file.name)
        
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Check if GROQ_API_KEY is set
    if not os.getenv("GROQ_API_KEY"):
        print("Error: GROQ_API_KEY environment variable is not set.")
        print("Please set it in the .env file or export it in your shell.")
        exit(1)
    
    app.run(debug=True, host='0.0.0.0', port=8080)
