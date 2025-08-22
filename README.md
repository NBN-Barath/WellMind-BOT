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
- No additional dependencies required (uses only standard library)

### Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Run the chatbot:
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
├── main.py           # Main application and user interface
├── wellmind_ai.py    # Core chatbot logic and response generation
├── resources.py      # Mental health resources and wellness techniques
└── README.md         # This file
```

### File Descriptions

- **`main.py`**: Contains the main application loop, user interface, and command handling
- **`wellmind_ai.py`**: Core chatbot class with response generation logic and conversation management
- **`resources.py`**: Mental health resources, crisis information, and wellness techniques database

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


