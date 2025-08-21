import random
import re
from resources import MentalHealthResources


class WellMindAI:
    """
    WellMind AI - A friendly and supportive student mental health and wellbeing chatbot.
    
    This chatbot helps students manage stress, stay motivated, and find useful mental health 
    resources without giving medical or clinical advice.
    """
    
    def __init__(self):
        self.resources = MentalHealthResources()
        self.conversation_history = []
        
        # Predefined responses for common mental health topics
        self.stress_responses = [
            "I'm sorry you're feeling stressed. Try taking a 5-minute break to breathe deeply: inhale for 4 seconds, hold for 4, exhale for 4. Would you like more quick stress relief tips?",
            "Stress is really tough to deal with. One technique that helps many students is the 5-4-3-2-1 grounding method: name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste.",
            "I understand stress can feel overwhelming. Try breaking your tasks into smaller, manageable chunks. Even completing one small task can help you feel more in control.",
            "When stress hits, remember that it's temporary. Take three deep breaths and remind yourself: 'I can handle this one step at a time.' What's one small thing you could do right now?"
        ]
        
        self.motivation_responses = [
            "Every small step counts! Even 20 minutes of focused study is progress. Want me to share a motivational quote with you?",
            "You've got this! Remember, progress isn't always linear - some days are harder than others, and that's completely normal.",
            "It's okay to feel unmotivated sometimes. Try setting a tiny goal for yourself - even 10 minutes of work is better than none. Small wins lead to bigger ones!",
            "Remember why you started this journey. You're capable of more than you know, and taking breaks doesn't mean you're lazy - it means you're human."
        ]
        
        self.anxiety_responses = [
            "Anxiety can feel really overwhelming. Try the box breathing technique: breathe in for 4, hold for 4, breathe out for 4, hold for 4. Repeat until you feel calmer.",
            "I hear you're feeling anxious. Sometimes it helps to write down your worries - getting them out of your head and onto paper can provide relief.",
            "Anxiety is your mind trying to protect you, but sometimes it gets a bit overprotective. Try naming your anxiety and thanking it, then gently redirecting your focus to the present moment.",
            "When anxiety peaks, remember the STOP technique: Stop what you're doing, Take a breath, Observe your thoughts and feelings, Proceed mindfully."
        ]
        
        self.exam_responses = [
            "Exam stress is so common - you're not alone in feeling this way. Try creating a study schedule that includes regular breaks and self-care time.",
            "I understand exam pressure can be intense. Remember to get enough sleep, stay hydrated, and don't skip meals - your brain needs fuel to work well!",
            "Exams can feel overwhelming, but you've prepared for this. Trust in your abilities and remember that one exam doesn't define your worth or future.",
            "Consider using active recall techniques like flashcards or teaching concepts out loud. And don't forget - it's okay to take study breaks!"
        ]
        
        self.sleep_responses = [
            "Good sleep is so important for mental health! Try to keep a consistent bedtime, avoid screens 1 hour before sleep, and create a relaxing bedtime routine.",
            "Sleep troubles can really affect how we feel. Consider making your bedroom cool, dark, and quiet. A warm bath or gentle stretching before bed might help too.",
            "If your mind races at bedtime, try the 'worry window' technique: set aside 10 minutes earlier in the day to write down your concerns, then remind yourself at bedtime that worry time is over."
        ]
        
        self.motivational_quotes = [
            "\"You are braver than you believe, stronger than you seem, and smarter than you think.\" - A.A. Milne",
            "\"Progress, not perfection.\" - Anonymous",
            "\"You don't have to be great to get started, but you have to get started to be great.\" - Les Brown",
            "\"Every expert was once a beginner.\" - Helen Hayes",
            "\"It's okay to be a masterpiece and a work in progress simultaneously.\" - Sophia Bush",
            "\"You are enough, just as you are.\" - Anonymous",
            "\"Small steps in the right direction can turn out to be the biggest step of your life.\" - Anonymous",
            "\"Your mental health is a priority. Your happiness is essential. Your self-care is a necessity.\" - Anonymous"
        ]
        
        # Keywords for pattern matching
        self.stress_keywords = ['stress', 'stressed', 'overwhelm', 'pressure', 'burden', 'too much']
        self.motivation_keywords = ['motivation', 'motivated', 'inspire', 'lazy', 'procrastinate', 'give up']
        self.anxiety_keywords = ['anxiety', 'anxious', 'worry', 'worried', 'panic', 'nervous', 'fear']
        self.exam_keywords = ['exam', 'test', 'assignment', 'study', 'grade', 'deadline']
        self.sleep_keywords = ['sleep', 'tired', 'insomnia', 'rest', 'exhausted']
        self.quote_keywords = ['quote', 'inspiration', 'motivational', 'inspire me']
        self.resource_keywords = ['help', 'support', 'counseling', 'therapy', 'crisis', 'helpline']
    
    def get_response(self, user_input):
        """
        Generate an appropriate response based on user input.
        
        Args:
            user_input (str): The user's message
            
        Returns:
            str: WellMind AI's response
        """
        user_input_lower = user_input.lower()
        
        # Store conversation
        self.conversation_history.append({"user": user_input, "bot": None})
        
        # Check for different types of requests
        if self._contains_keywords(user_input_lower, self.quote_keywords):
            response = self._get_motivational_quote()
        elif self._contains_keywords(user_input_lower, self.resource_keywords):
            response = self._get_resources_response()
        elif self._contains_keywords(user_input_lower, self.stress_keywords):
            response = random.choice(self.stress_responses)
        elif self._contains_keywords(user_input_lower, self.motivation_keywords):
            response = random.choice(self.motivation_responses)
        elif self._contains_keywords(user_input_lower, self.anxiety_keywords):
            response = random.choice(self.anxiety_responses)
        elif self._contains_keywords(user_input_lower, self.exam_keywords):
            response = random.choice(self.exam_responses)
        elif self._contains_keywords(user_input_lower, self.sleep_keywords):
            response = random.choice(self.sleep_responses)
        elif self._is_greeting(user_input_lower):
            response = self._get_greeting_response()
        elif self._is_goodbye(user_input_lower):
            response = self._get_goodbye_response()
        else:
            response = self._get_general_support_response()
        
        # Store bot response
        self.conversation_history[-1]["bot"] = response
        
        return response
    
    def _contains_keywords(self, text, keywords):
        """Check if text contains any of the specified keywords."""
        return any(keyword in text for keyword in keywords)
    
    def _is_greeting(self, text):
        """Check if the input is a greeting."""
        greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
        return any(greeting in text for greeting in greetings)
    
    def _is_goodbye(self, text):
        """Check if the input is a goodbye."""
        goodbyes = ['bye', 'goodbye', 'see you', 'talk later', 'thanks']
        return any(goodbye in text for goodbye in goodbyes)
    
    def _get_greeting_response(self):
        """Return a warm greeting response."""
        greetings = [
            "Hello! I'm WellMind AI, and I'm here to support your mental health and wellbeing. How are you feeling today?",
            "Hi there! I'm here to help with stress, motivation, and general wellbeing. What's on your mind?",
            "Welcome! I'm WellMind AI, your friendly mental health support companion. How can I help you today?"
        ]
        return random.choice(greetings)
    
    def _get_goodbye_response(self):
        """Return a supportive goodbye response."""
        goodbyes = [
            "Take care of yourself! Remember, you're stronger than you think. Feel free to chat with me anytime you need support.",
            "Goodbye for now! Remember to be kind to yourself and take things one step at a time. I'm here whenever you need me.",
            "See you later! Keep taking care of your mental health - you're doing great by reaching out. Stay strong!"
        ]
        return random.choice(goodbyes)
    
    def _get_motivational_quote(self):
        """Return a motivational quote."""
        quote = random.choice(self.motivational_quotes)
        return f"Here's something to inspire you: {quote}"
    
    def _get_resources_response(self):
        """Return information about mental health resources."""
        return self.resources.get_emergency_resources() + "\n\n" + self.resources.get_general_resources()
    
    def _get_general_support_response(self):
        """Return a general supportive response."""
        responses = [
            "I'm here to listen and support you. Sometimes just talking about what's bothering you can help. What's on your mind?",
            "Thank you for sharing with me. Remember, it's completely normal to have ups and downs. You're not alone in this.",
            "I hear you, and your feelings are valid. Taking care of your mental health is really important. Is there a specific area you'd like support with?",
            "It sounds like you might be going through a tough time. Remember, seeking support is a sign of strength, not weakness. How can I help?"
        ]
        return random.choice(responses)
    
    def get_conversation_history(self):
        """Return the conversation history."""
        return self.conversation_history
    
    def clear_conversation(self):
        """Clear the conversation history."""
        self.conversation_history = []
