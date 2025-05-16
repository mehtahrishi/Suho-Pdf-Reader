document.addEventListener('DOMContentLoaded', function() {
    const fileUpload = document.getElementById('file-upload');
    const fileInput = document.getElementById('file-input');
    const fileName = document.getElementById('file-name');
    const analyzeBtn = document.getElementById('analyze-btn');
    const resultsSection = document.getElementById('results-section');
    const docTypeElement = document.getElementById('doc-type');
    const summaryElement = document.getElementById('summary-content');
    const loadingElement = document.getElementById('loading');
    const errorMessage = document.getElementById('error-message');
    
    // Handle file upload area click
    fileUpload.addEventListener('click', function() {
        fileInput.click();
    });
    
    // Handle file selection
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            
            // Check if file is PDF
            if (file.type !== 'application/pdf') {
                errorMessage.textContent = 'Please select a PDF file.';
                errorMessage.style.display = 'block';
                fileName.textContent = '';
                analyzeBtn.disabled = true;
                return;
            }
            
            fileName.textContent = file.name;
            analyzeBtn.disabled = false;
            errorMessage.style.display = 'none';
        } else {
            fileName.textContent = '';
            analyzeBtn.disabled = true;
        }
    });
    
    // Handle analyze button click
    analyzeBtn.addEventListener('click', function() {
        if (fileInput.files.length === 0) return;
        
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append('pdf', file);
        
        // Show loading
        loadingElement.style.display = 'block';
        resultsSection.style.display = 'none';
        errorMessage.style.display = 'none';
        analyzeBtn.disabled = true;
        
        // Send file to server
        fetch('/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Server error: ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            // Hide loading
            loadingElement.style.display = 'none';
            
            // Show results
            docTypeElement.textContent = data.doc_type;
            summaryElement.innerHTML = formatSummary(data.summary);
            resultsSection.style.display = 'block';
            analyzeBtn.disabled = false;
            
            // Scroll to results
            resultsSection.scrollIntoView({ behavior: 'smooth' });
        })
        .catch(error => {
            loadingElement.style.display = 'none';
            errorMessage.textContent = 'Error analyzing PDF: ' + error.message;
            errorMessage.style.display = 'block';
            analyzeBtn.disabled = false;
        });
    });
    
    // Format summary with emojis and markdown-like syntax
    function formatSummary(text) {
        // Replace markdown headings
        text = text.replace(/^# (.*?)$/gm, '<h2>$1</h2>');
        text = text.replace(/^## (.*?)$/gm, '<h3>$1</h3>');
        text = text.replace(/^### (.*?)$/gm, '<h4>$1</h4>');
        
        // Replace bullet points
        text = text.replace(/^- (.*?)$/gm, '<li>$1</li>');
        text = text.replace(/^• (.*?)$/gm, '<li>$1</li>');
        text = text.replace(/^(\d+)\. (.*?)$/gm, '<li><strong>$1.</strong> $2</li>');
        
        // Wrap lists
        let inList = false;
        let listType = '';
        let formattedText = '';
        
        text.split('\n').forEach(line => {
            if (line.match(/^<li>/)) {
                if (!inList) {
                    inList = true;
                    listType = line.match(/^<li><strong>\d+\.<\/strong>/) ? 'ol' : 'ul';
                    formattedText += `<${listType}>`;
                }
                formattedText += line;
            } else {
                if (inList) {
                    inList = false;
                    formattedText += `</${listType}>`;
                }
                formattedText += line + '\n';
            }
        });
        
        if (inList) {
            formattedText += `</${listType}>`;
        }
        
        text = formattedText;
        
        // Replace bold
        text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        text = text.replace(/__(.*?)__/g, '<strong>$1</strong>');
        
        // Replace italic
        text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
        text = text.replace(/_(.*?)_/g, '<em>$1</em>');
        
        // Replace newlines with <br>
        text = text.replace(/\n/g, '<br>');
        
        return text;
    }
    
    // Handle drag and drop
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        fileUpload.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }
    
    ['dragenter', 'dragover'].forEach(eventName => {
        fileUpload.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
        fileUpload.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight() {
        fileUpload.classList.add('highlight');
    }
    
    function unhighlight() {
        fileUpload.classList.remove('highlight');
    }
    
    fileUpload.addEventListener('drop', handleDrop, false);
    
    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        
        if (files.length > 0) {
            fileInput.files = files;
            
            // Trigger change event
            const event = new Event('change');
            fileInput.dispatchEvent(event);
        }
    }
});
