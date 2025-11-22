// Get DOM elements
const themeInput = document.getElementById('themeInput');
const generateBtn = document.getElementById('generateBtn');
const loadingSpinner = document.getElementById('loadingSpinner');
const quoteDisplay = document.getElementById('quoteDisplay');
const quoteText = document.getElementById('quoteText');
const quoteTheme = document.getElementById('quoteTheme');
const errorDisplay = document.getElementById('errorDisplay');
const errorText = document.getElementById('errorText');

// Allow Enter key to trigger quote generation
themeInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        generateQuote();
    }
});

// Function to set theme from chip
function setTheme(theme) {
    themeInput.value = theme;
    themeInput.focus();
    generateQuote();
}

// Function to show loading state
function showLoading() {
    hideAllDisplays();
    loadingSpinner.classList.remove('hidden');
    generateBtn.disabled = true;
}

// Function to hide all display elements
function hideAllDisplays() {
    loadingSpinner.classList.add('hidden');
    quoteDisplay.classList.add('hidden');
    errorDisplay.classList.add('hidden');
}

// Function to show error
function showError(message) {
    hideAllDisplays();
    errorText.textContent = message;
    errorDisplay.classList.remove('hidden');
    generateBtn.disabled = false;
}

// Function to show quote
function showQuote(quote, theme) {
    hideAllDisplays();
    quoteText.textContent = quote;
    quoteTheme.textContent = theme;
    quoteDisplay.classList.remove('hidden');
    generateBtn.disabled = false;
}

// Main function to generate quote
async function generateQuote() {
    const theme = themeInput.value.trim();
    
    // Validate input
    if (!theme) {
        showError('Please enter a theme to generate a quote.');
        themeInput.focus();
        return;
    }
    
    showLoading();
    
    try {
        // Make API request to backend
        const response = await fetch('/generate-quote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ theme: theme })
        });
        
        const data = await response.json();
        
        if (response.ok && data.success) {
            // Display the generated quote
            showQuote(data.quote, data.theme);
        } else {
            // Show error message
            showError(data.error || 'Failed to generate quote. Please try again.');
        }
    } catch (error) {
        showError('Network error. Please check your connection and try again.');
        console.error('Error:', error);
    }
}

// Initialize: focus on input when page loads
window.addEventListener('load', function() {
    themeInput.focus();
});

