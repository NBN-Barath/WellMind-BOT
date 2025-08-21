# WellMind AI Chatbot 🌟

A friendly and supportive student mental health and wellbeing chatbot designed to help students manage stress, stay motivated, and find useful mental health resources.

## 🎯 Purpose

WellMind AI provides:
- Stress management techniques and coping strategies
- Motivational messages and quotes
- General wellbeing advice (sleep hygiene, healthy habits)
- Access to verified mental health resources and helplines
- Supportive, non-judgmental conversation

**Important:** WellMind AI provides support and resources but does not give medical or clinical advice.

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- Flask and Flask-CORS (see requirements.txt)

### Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the web application:
   ```bash
   python app.py
   ```
5. Open your browser and go to: `http://localhost:5000`

### Alternative: Console Version
For the console-only version:
```bash
python main.py
```

## 💬 How to Use

### Starting a Conversation
Simply run the program and start typing! WellMind AI will respond to various topics including:

- **Stress and overwhelm:** "I'm feeling really stressed about exams"
- **Motivation:** "I need help staying motivated to study"
- **Anxiety:** "I'm feeling anxious about my presentation"
- **Sleep issues:** "I can't sleep because I'm worried"
- **General support:** "I'm having a tough day"

### Available Commands
- `help` - Show available commands
- `resources` - View mental health resources
- `emergency` - Get crisis support information
- `techniques` - View wellness and coping techniques
- `quote` - Get a motivational quote
- `clear` - Clear conversation history
- `history` - View conversation history
- `quit` or `exit` - End the conversation

## 🧠 Features

### Intelligent Response System
WellMind AI uses keyword recognition to provide appropriate responses for:
- Stress management
- Motivation and study tips
- Anxiety support
- Exam preparation
- Sleep hygiene
- General emotional support

### Mental Health Resources
Access to verified resources including:
- Crisis hotlines and emergency support
- National mental health organizations
- Student-specific resources
- Online support platforms
- Wellness apps and tools

### Wellness Techniques
Built-in techniques for:
- Breathing exercises (Box breathing, 4-7-8 technique)
- Stress management strategies
- Time management tips
- Sleep hygiene practices
- Mindfulness and grounding techniques

## 📋 Example Interactions

### Stress Management
```
You: I'm feeling overwhelmed with exams
WellMind AI: I'm sorry you're feeling stressed. Try taking a 5-minute break 
to breathe deeply: inhale for 4 seconds, hold for 4, exhale for 4. 
Would you like more quick stress relief tips?
```

### Motivation Support
```
You: I need motivation to study
WellMind AI: Every small step counts! Even 20 minutes of focused study is 
progress. Want me to share a motivational quote with you?
```

### Resource Access
```
You: I think I need professional help
WellMind AI: [Provides emergency resources and general mental health resources]
```

## 🛡️ Safety & Ethics

### What WellMind AI Does:
- Provides emotional support and encouragement
- Shares coping strategies and wellness techniques
- Offers access to professional mental health resources
- Maintains a supportive, non-judgmental tone

### What WellMind AI Does NOT Do:
- Provide medical diagnoses or clinical advice
- Replace professional mental health treatment
- Store personal information or conversation data permanently
- Judge or criticize users' feelings or experiences

### Emergency Situations
If you're in crisis or having thoughts of self-harm:
- **Call 988** (Suicide & Crisis Lifeline) - Available 24/7
- **Text HOME to 741741** (Crisis Text Line)
- **Call 911** or go to your nearest emergency room

## 🏗️ Project Structure

```
ChatBot/
├── app.py               # Flask web server and API endpoints
├── main.py              # Console application interface
├── wellmind_ai.py       # Core chatbot logic and response generation
├── resources.py         # Mental health resources and wellness techniques
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Web interface HTML template
├── static/
│   ├── css/
│   │   └── style.css    # Frontend styling
│   └── js/
│       └── app.js       # Frontend JavaScript functionality
└── README.md            # This file
```

### File Descriptions

- **`app.py`**: Flask web server providing REST API endpoints for the frontend
- **`main.py`**: Console-based interface for terminal usage
- **`wellmind_ai.py`**: Core chatbot class with response generation logic and conversation management
- **`resources.py`**: Mental health resources, crisis information, and wellness techniques database
- **`templates/index.html`**: Modern, responsive web interface with chat functionality
- **`static/css/style.css`**: Beautiful styling with gradients, animations, and responsive design
- **`static/js/app.js`**: Frontend JavaScript handling user interactions and API communication

## 🎨 Customization

### Adding New Responses
To add new response categories or improve existing ones:

1. Edit `wellmind_ai.py` to add new keyword lists and response arrays
2. Update the `get_response()` method to handle new categories
3. Add corresponding resources in `resources.py` if needed

### Adding New Resources
To add new mental health resources:

1. Edit the dictionaries in `resources.py`
2. Update the display methods as needed
3. Ensure all resources are verified and appropriate

## 🤝 Contributing

This is an educational project designed to demonstrate supportive AI chatbot development. If you'd like to contribute:

1. Ensure all mental health resources are verified and current
2. Maintain the supportive, non-judgmental tone
3. Test thoroughly to ensure appropriate responses
4. Follow ethical guidelines for mental health support tools

## ⚠️ Disclaimer

WellMind AI is designed for educational and support purposes only. It is not a substitute for professional mental health care, medical advice, diagnosis, or treatment. 

If you're experiencing a mental health crisis or emergency, please contact:
- Emergency services (911)
- National Suicide Prevention Lifeline (988)
- Crisis Text Line (Text HOME to 741741)
- Your local mental health crisis center

Always seek the advice of qualified health providers with any questions regarding mental health conditions.

## 📞 Support & Resources

### National Resources (US)
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **SAMHSA National Helpline**: 1-800-662-4357
- **National Sexual Assault Hotline**: 1-800-656-4673

### Online Resources
- National Alliance on Mental Illness (NAMI): nami.org
- Mental Health America: mhanational.org
- Anxiety and Depression Association: adaa.org

---

**Remember: You are not alone. Help is available, and your mental health matters.** 💙
