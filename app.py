from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/generate-quote', methods=['POST'])
def generate_quote():
    """Generate a motivational quote based on the provided theme"""
    try:
        data = request.get_json()
        theme = data.get('theme', '').strip()
        
        if not theme:
            return jsonify({'error': 'Please provide a theme'}), 400
        
        # Check if API key is set
        if not openai.api_key:
            return jsonify({'error': 'OpenAI API key not configured. Please add OPENAI_API_KEY to your .env file'}), 500
        
        # Create OpenAI client
        client = openai.OpenAI(api_key=openai.api_key)
        
        # Call OpenAI API to generate a motivational quote
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a wise motivational speaker who creates inspiring and uplifting quotes. Generate original, powerful motivational quotes that resonate deeply with people."
                },
                {
                    "role": "user",
                    "content": f"Generate a powerful and inspiring motivational quote about '{theme}'. Make it memorable, concise, and impactful. Just return the quote itself, without quotation marks or attribution."
                }
            ],
            temperature=0.9,
            max_tokens=100
        )
        
        quote = response.choices[0].message.content.strip()
        
        return jsonify({
            'success': True,
            'quote': quote,
            'theme': theme
        })
        
    except openai.APIError as e:
        return jsonify({'error': f'OpenAI API error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

