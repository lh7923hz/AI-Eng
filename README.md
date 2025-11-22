# 🌟 Motivational Quote Generator

An AI-powered web application that generates inspiring motivational quotes based on themes you provide. Built with Flask backend and modern HTML/CSS/JavaScript frontend, powered by OpenAI's GPT.

## ✨ Features

- **AI-Powered Quotes**: Generates unique motivational quotes using OpenAI's GPT-3.5-turbo
- **Theme-Based**: Enter any theme (success, courage, dreams, etc.) to get relevant quotes
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Quick Themes**: Pre-selected theme chips for instant inspiration
- **Error Handling**: Graceful error messages and loading states

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. **Clone or navigate to the project directory**

2. **Set up virtual environment** (if not already activated):
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create a `.env` file in the project root:
     ```bash
     # Windows
     copy .env.example .env
     
     # macOS/Linux
     cp .env.example .env
     ```
   - Open `.env` and add your OpenAI API key:
     ```
     OPENAI_API_KEY=sk-your-actual-api-key-here
     ```

### Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Start generating quotes!**
   - Enter a theme in the input field
   - Click "Generate Quote" or press Enter
   - Enjoy your personalized motivational quote!

## 🎨 Usage Examples

Try these themes:
- **Success** - Get quotes about achieving your goals
- **Perseverance** - Find inspiration to keep going
- **Courage** - Discover your inner strength
- **Dreams** - Be motivated to chase your aspirations
- **Growth** - Learn about personal development
- **Happiness** - Find joy and positivity

## 📁 Project Structure

```
AI-Eng/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .env.example          # Environment variables template
├── templates/
│   └── index.html        # Main HTML page
└── static/
    ├── style.css         # Styling
    └── script.js         # Frontend JavaScript
```

## 🛠️ Tech Stack

- **Backend**: Flask, OpenAI Python SDK
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **AI**: OpenAI GPT-3.5-turbo
- **Styling**: Custom CSS with gradient backgrounds and animations

## 🔧 Configuration

### Customizing the AI Behavior

You can modify the OpenAI parameters in `app.py`:

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",        # Change model if needed
    temperature=0.9,               # Adjust creativity (0.0-1.0)
    max_tokens=100                 # Max length of response
)
```

### Customizing the UI

- Edit `static/style.css` to change colors, fonts, and layouts
- Modify gradient colors in the CSS to match your brand
- Update `templates/index.html` to add more features

## 🚨 Troubleshooting

**Issue**: "OpenAI API key not configured"
- **Solution**: Make sure you've created a `.env` file with your API key

**Issue**: Module not found errors
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: Port 5000 already in use
- **Solution**: Change the port in `app.py`: `app.run(port=5001)`

## 📝 API Endpoints

### POST `/generate-quote`
Generate a motivational quote based on a theme.

**Request Body**:
```json
{
  "theme": "success"
}
```

**Response**:
```json
{
  "success": true,
  "quote": "Your generated quote here",
  "theme": "success"
}
```

## 🌐 Deployment

To deploy this application:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server (e.g., Gunicorn)
3. Set up environment variables on your hosting platform
4. Consider rate limiting for the API endpoint

## 📄 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork this project and make your own improvements!

---

Made with ❤️ and OpenAI

