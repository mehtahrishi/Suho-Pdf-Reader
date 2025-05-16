# Suho PDF Reader 📚✨

![Suho PDF Reader Logo](static/images/logo.svg)

A smart, elegant PDF analysis tool that uses AI to identify document types and provide comprehensive summaries.

## ✨ Features

- 📄 **Smart Document Analysis**: Automatically identifies document types (offer letters, educational resources, scripts, legal documents, etc.)
- 📝 **Comprehensive Summaries**: Generates detailed summaries with key points, findings, and actionable items
- 🎨 **Beautiful Glassmorphic UI**: Modern, responsive interface with glass-like transparency effects
- 🔄 **Intuitive User Experience**: Simple drag-and-drop functionality for easy document uploads
- 🧠 **Powered by Llama 3**: Utilizes Groq's implementation of Llama 3 70B model for high-quality analysis
- 🔒 **Privacy-Focused**: Files are processed locally and not stored permanently

## 📋 Table of Contents

- [Installation](#-installation)
- [Usage](#-usage)
- [Web Interface](#web-interface)
- [Command Line Interface](#command-line-interface)
- [Technologies](#-technologies)
- [Project Structure](#-project-structure)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key (sign up at [groq.com](https://groq.com))

### Setup Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/mehtahrishi/suho-pdf-reader.git
   cd suho-pdf-reader
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your Groq API key:
   ```bash
   echo "GROQ_API_KEY=your_groq_api_key_here" > .env
   ```

## 🖥️ Usage

### Web Interface

To use the beautiful glassmorphic web interface:

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the Flask app
python server.py
```

This will start a local web server at http://localhost:8080 where you can access the application.

![Web Interface Screenshot](static/images/screenshot.png)

### Command Line Interface

For quick analysis without a web interface:

```bash
# Activate the virtual environment
source venv/bin/activate

# Run the CLI tool
python cli.py /path/to/your/document.pdf
```

Example output:
```
🔍 Analyzing PDF: example.pdf
⏳ This may take a moment...

================================================================================
📑 Document Type: Research Paper
================================================================================

📝 Summary:
# Research on Quantum Computing Applications

## Main Topics:
• Quantum computing fundamentals
• Quantum algorithms and their advantages
• Practical applications in cryptography
• Future directions in quantum computing research

## Key Findings:
1. Quantum computers can solve certain problems exponentially faster than classical computers
2. Shor's algorithm poses significant threats to current encryption methods
3. Quantum machine learning shows promising results for complex data analysis
...
================================================================================
```

## 🛠️ Technologies

- **Backend**:
  - Python 3.12
  - Flask 2.3.3 (Web Server)
  - PyPDF2 3.0.1 (PDF processing)
  - Groq API (Document analysis with Llama 3 70B model)

- **Frontend**:
  - HTML5/CSS3/JavaScript
  - Font Awesome (Icons)
  - Google Fonts (Poppins)

## 📁 Project Structure

```
suho-pdf-reader/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       ├── favicon.ico
│       ├── logo.png
│       └── screenshot.png
├── templates/
│   └── index.html
├── cli.py
├── server.py
├── pdf_processor.py
├── requirements.txt
├── .env
└── README.md
```

## 🎨 Customization

### Changing the Theme

You can easily customize the look and feel by modifying the CSS variables in `static/css/style.css`:

```css
:root {
  --primary-color: #6c63ff;  /* Change to your preferred primary color */
  --secondary-color: #4db6ac;
  --background-color: #f5f7fa;
  --card-bg-color: rgba(255, 255, 255, 0.15);
  --text-color: #333;
  --light-text: #fff;
  /* ... other variables ... */
}
```

### Modifying Analysis Parameters

To adjust how the AI analyzes documents, modify the prompts in `pdf_processor.py`:

```python
# Create prompt for document type classification
type_prompt = f"""You are Suho, an expert PDF analyzer. 
Analyze the provided PDF content and determine what type of document it is.
# ... customize the prompt here ... #
"""
```

## ❓ Troubleshooting

### Installation Issues

If you encounter issues with dependencies, you may need to install system dependencies:

```bash
sudo apt-get update
sudo apt-get install -y libjpeg-dev zlib1g-dev
```

### API Key Problems

If you see an error about the Groq API key:
1. Make sure you've created a `.env` file with your API key
2. Verify the API key is valid and has not expired
3. Try exporting the key directly: `export GROQ_API_KEY=your_key_here`

### PDF Processing Errors

If you encounter issues with specific PDFs:
1. Ensure the PDF is not password-protected
2. Try with a simpler PDF to see if the issue persists
3. Check if the PDF contains extractable text (some scanned documents may not)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with ❤️ by [Your Name]

*Suho PDF Reader is not affiliated with Groq or Meta. Llama 3 is a trademark of Meta.*
