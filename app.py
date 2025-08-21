#!/usr/bin/env python3
"""
WellMind AI Chatbot - Web API Server
A Flask-based web server for the WellMind AI chatbot frontend.
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import sys
from wellmind_ai import WellMindAI
from resources import MentalHealthResources

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)  # Enable CORS for frontend-backend communication

# Initialize the chatbot
chatbot = WellMindAI()
resources = MentalHealthResources()

@app.route('/')
def index():
    """Serve the main chat interface."""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages from the frontend."""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Handle special commands
        command = user_message.lower()
        
        if command == 'emergency':
            response = resources.get_emergency_resources()
        elif command == 'resources':
            response = resources.get_general_resources() + "\n\n" + resources.get_student_resources()
        elif command == 'techniques':
            response = resources.get_all_wellness_techniques()
        elif command in ['clear', 'reset']:
            chatbot.clear_conversation()
            response = "Conversation history cleared. How can I help you today?"
        else:
            # Get AI response
            response = chatbot.get_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/resources')
def get_resources():
    """Get mental health resources."""
    try:
        return jsonify({
            'emergency': resources.get_emergency_resources(),
            'general': resources.get_general_resources(),
            'student': resources.get_student_resources(),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/techniques/<category>')
def get_techniques(category):
    """Get wellness techniques for a specific category."""
    try:
        techniques = resources.get_wellness_technique(category)
        return jsonify({
            'techniques': techniques,
            'category': category,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/quote')
def get_quote():
    """Get a motivational quote."""
    try:
        response = chatbot.get_response("motivational quote")
        return jsonify({
            'quote': response,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.route('/api/history')
def get_history():
    """Get conversation history."""
    try:
        history = chatbot.get_conversation_history()
        return jsonify({
            'history': history,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}',
            'status': 'error'
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    os.makedirs('static/js', exist_ok=True)
    
    print("🌟 Starting WellMind AI Web Server...")
    print("📱 Frontend will be available at: http://localhost:5000")
    print("🔧 API endpoints available at: http://localhost:5000/api/")
    print("💙 Ready to help with your mental health and wellbeing!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
