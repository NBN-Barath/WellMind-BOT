#!/usr/bin/env python3
"""
WellMind AI Chatbot - Main Application
A friendly and supportive student mental health and wellbeing chatbot.

This chatbot helps students manage stress, stay motivated, and find useful mental health 
resources without giving medical or clinical advice.
"""

import sys
import os
from wellmind_ai import WellMindAI
from resources import MentalHealthResources


def print_welcome():
    """Print welcome message and introduction."""
    print("=" * 60)
    print("🌟 Welcome to WellMind AI 🌟")
    print("Your friendly mental health and wellbeing support companion")
    print("=" * 60)
    print()
    print("💙 I'm here to help you with:")
    print("   • Stress management techniques")
    print("   • Motivation and study tips")
    print("   • General wellbeing advice")
    print("   • Mental health resources")
    print()
    print("💡 Remember: I provide support and resources, not medical advice.")
    print("   For emergencies, please contact professional help immediately.")
    print()
    print("Type 'help' for commands, 'resources' for mental health resources,")
    print("or 'quit' to exit. Let's start our conversation!")
    print("-" * 60)


def print_help():
    """Print available commands."""
    print("\n🔧 Available Commands:")
    print("• 'help' - Show this help message")
    print("• 'resources' - View mental health resources")
    print("• 'emergency' - Get crisis support information")
    print("• 'techniques' - View wellness techniques")
    print("• 'quote' - Get a motivational quote")
    print("• 'clear' - Clear conversation history")
    print("• 'history' - View conversation history")
    print("• 'quit' or 'exit' - End the conversation")
    print("-" * 40)


def print_emergency_info():
    """Print emergency mental health information."""
    print("\n🚨 EMERGENCY MENTAL HEALTH RESOURCES 🚨")
    print()
    print("If you're in immediate danger or having thoughts of self-harm:")
    print("• Call 988 (Suicide & Crisis Lifeline) - Available 24/7")
    print("• Text HOME to 741741 (Crisis Text Line)")
    print("• Call 911 or go to your nearest emergency room")
    print("• Contact your local emergency services")
    print()
    print("🫂 Remember: You are not alone. Help is available.")
    print("   Your life has value and meaning.")
    print("-" * 50)


def handle_special_commands(user_input, chatbot, resources):
    """
    Handle special commands that don't require AI response.
    
    Args:
        user_input (str): User's input
        chatbot (WellMindAI): The chatbot instance
        resources (MentalHealthResources): Resources instance
        
    Returns:
        bool: True if command was handled, False otherwise
    """
    command = user_input.lower().strip()
    
    if command in ['quit', 'exit', 'bye', 'goodbye']:
        print("\n💙 Thank you for using WellMind AI!")
        print("Remember to take care of yourself and reach out when you need support.")
        print("You're stronger than you think! 🌟")
        return True
        
    elif command == 'help':
        print_help()
        return False
        
    elif command == 'emergency':
        print_emergency_info()
        return False
        
    elif command == 'resources':
        print("\n" + resources.get_general_resources())
        print(resources.get_student_resources())
        return False
        
    elif command == 'techniques':
        print("\n" + resources.get_all_wellness_techniques())
        return False
        
    elif command == 'quote':
        response = chatbot.get_response("motivational quote")
        print(f"\n🌟 {response}")
        return False
        
    elif command == 'clear':
        chatbot.clear_conversation()
        print("\n✅ Conversation history cleared.")
        return False
        
    elif command == 'history':
        history = chatbot.get_conversation_history()
        if not history:
            print("\n📝 No conversation history yet.")
        else:
            print("\n📝 Conversation History:")
            print("-" * 30)
            for i, exchange in enumerate(history, 1):
                print(f"{i}. You: {exchange['user']}")
                if exchange['bot']:
                    print(f"   WellMind AI: {exchange['bot'][:100]}...")
                print()
        return False
    
    return False


def main():
    """Main application loop."""
    try:
        # Initialize the chatbot and resources
        chatbot = WellMindAI()
        resources = MentalHealthResources()
        
        # Print welcome message
        print_welcome()
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                user_input = input("\n💬 You: ").strip()
                
                # Skip empty inputs
                if not user_input:
                    continue
                
                # Handle special commands
                should_quit = handle_special_commands(user_input, chatbot, resources)
                if should_quit:
                    break
                
                # Get AI response for regular conversation
                if not any(cmd in user_input.lower() for cmd in ['help', 'emergency', 'resources', 'techniques', 'clear', 'history']):
                    response = chatbot.get_response(user_input)
                    print(f"\n🤖 WellMind AI: {response}")
                
            except KeyboardInterrupt:
                print("\n\n💙 Goodbye! Take care of yourself! 🌟")
                break
                
            except Exception as e:
                print(f"\n❌ Sorry, I encountered an error: {str(e)}")
                print("Please try again or type 'help' for available commands.")
    
    except Exception as e:
        print(f"❌ Failed to start WellMind AI: {str(e)}")
        print("Please check your installation and try again.")
        sys.exit(1)


if __name__ == "__main__":
    main()
