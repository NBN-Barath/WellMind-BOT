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
            "Every small step counts, and I'm proud of you for reaching out! Even 20 minutes of focused study is real progress. Remember, motivation often comes after action, not before - so even if you don't feel motivated right now, starting small can help build that momentum. Try the '2-minute rule': commit to just 2 minutes of the task. Often, you'll find yourself continuing once you've started. Want me to share a motivational quote with you, or would you like to talk about what's making it hard to get started?",
            "You've got this! I know it might not feel like it right now, but you're stronger than you realize. Remember, progress isn't always linear - some days are harder than others, and that's completely normal. Think about how far you've already come. Every expert was once a beginner, and every successful person has had days where they didn't feel motivated. The fact that you're here asking for help shows you haven't given up.",
            "It's completely okay to feel unmotivated sometimes - it's a sign you're human, not lazy! Try setting a tiny goal for yourself, something so small it feels almost silly not to do it. Maybe it's reading just one page, writing one sentence, or organizing just one section of your notes. Small wins lead to bigger ones, and momentum builds on itself. Remember, you don't have to be perfect; you just have to begin.",
            "Remember why you started this journey in the first place. What dreams or goals motivated you when you began? Sometimes reconnecting with our 'why' can reignite that spark. You're capable of more than you know, and taking breaks doesn't mean you're lazy - it means you're taking care of yourself so you can perform your best. Self-compassion is just as important as determination.",
            "Motivation can be elusive, but discipline and self-compassion can carry you through. Try changing your environment - sometimes a new location can spark new energy. Consider the Pomodoro Technique: work for 25 minutes, then take a 5-minute break. This makes tasks feel less overwhelming and gives you regular rewards. Also, remember to celebrate small victories along the way!",
            "I understand feeling unmotivated can be frustrating, especially when you know what you need to do but can't seem to get started. Try the 'motivation follows action' principle: start with the easiest or most interesting part of your task. Sometimes we get stuck because we think we need to start at the beginning, but you can start anywhere that feels manageable right now."
        ]
        
        self.anxiety_responses = [
            "I hear you're feeling anxious, and I want you to know that anxiety is incredibly common - you're definitely not alone. Try the box breathing technique: breathe in for 4, hold for 4, breathe out for 4, hold for 4. Repeat this cycle 4-6 times. Anxiety often makes us breathe shallowly, which can make the feelings worse. Deep breathing activates your body's relaxation response. Remember, anxiety is temporary and manageable. Would you like to talk about what's triggering these feelings?",
            "Anxiety can feel really overwhelming, like your mind is racing and you can't catch up. Sometimes it helps to write down your worries - getting them out of your head and onto paper can provide immediate relief. Try this: set a timer for 5 minutes and write down everything that's making you anxious. Don't worry about grammar or making sense, just let it all out. This 'brain dump' technique can help you feel less overwhelmed.",
            "I understand anxiety can make everything feel more intense and difficult. Anxiety is your mind trying to protect you, but sometimes it gets a bit overprotective, like an overzealous security guard. Try naming your anxiety - some people call it their 'worry monster' or 'anxious brain.' Thank it for trying to keep you safe, then gently redirect your focus to the present moment. What are three things you can see around you right now?",
            "When anxiety peaks, it can feel like you're drowning in worried thoughts. Try the STOP technique: Stop what you're doing, Take a breath, Observe your thoughts and feelings without judgment, and Proceed mindfully with what you were doing. Anxiety often comes from our mind jumping to worst-case scenarios, but most of the things we worry about never actually happen.",
            "Anxiety can make your heart race and your mind feel scattered. Remember that anxiety is not dangerous, even though it feels uncomfortable. Try the 54321 grounding technique: name 5 things you can see, 4 things you can touch, 3 things you can hear, 2 things you can smell, and 1 thing you can taste. This helps anchor you in the present moment rather than getting lost in anxious thoughts about the future.",
            "I want you to know that having anxiety doesn't make you weak or broken - it makes you human. Anxiety often stems from caring deeply about things that matter to us. Try gentle self-talk: instead of 'I can't handle this,' try 'This is difficult, but I can get through it one moment at a time.' Your feelings are valid, and you have more strength than you realize."
        ]
        
        self.exam_responses = [
            "Exam stress is incredibly common - you're definitely not alone in feeling this way. The pressure to perform can feel overwhelming, but remember that one exam doesn't define your intelligence or your future. Try creating a study schedule that includes regular breaks and self-care time. Break your material into smaller chunks and use active recall techniques like flashcards or explaining concepts out loud. Most importantly, make sure you're getting enough sleep, staying hydrated, and eating regular meals - your brain needs fuel to work at its best!",
            "I understand exam pressure can feel intense, like there's so much riding on your performance. Remember that you've been preparing for this, and trust in the work you've already done. Consider using the 'teach someone else' method - explaining concepts to a friend, family member, or even a pet can help solidify your understanding. Also, practice exam conditions at home to reduce anxiety on the actual day. You've got this!",
            "Exams can feel overwhelming, especially when you're worried about the outcome. But remember, you've prepared for this moment, and you have more knowledge than you think. Trust in your abilities and try to view the exam as an opportunity to show what you've learned rather than a test of your worth as a person. Consider doing some light exercise before studying - it can help reduce stress and improve focus.",
            "The lead-up to exams can be stressful, but you're stronger than you know. Try the 'chunk and check' method: study for 25-30 minutes, then take a 5-10 minute break to do something completely different. This helps prevent burnout and keeps your mind fresh. Remember, it's better to study consistently over time than to cram everything at the last minute. And don't forget - it's okay to take study breaks and do things you enjoy!",
            "Exam anxiety is your mind's way of showing you care about your performance, which shows you're a dedicated student. Try visualization: imagine yourself feeling calm and confident during the exam, successfully answering questions. This mental rehearsal can help reduce anxiety. Also, prepare not just academically but practically - know where your exam is, what to bring, and have a good breakfast that morning. Being prepared helps reduce uncertainty.",
            "Remember that exams are just one way to measure learning, not your worth as a person. If you're feeling overwhelmed, try the 'worst case scenario' exercise: what would actually happen if you didn't do as well as hoped? Often, we'll realize the consequences aren't as catastrophic as our anxiety makes them seem. Focus on doing your best with the time you have, rather than achieving perfection."
        ]
        
        self.sleep_responses = [
            "Good sleep is absolutely crucial for mental health, academic performance, and overall wellbeing! Try to keep a consistent bedtime and wake-up time, even on weekends - your body loves routine. Avoid screens for at least 1 hour before sleep as the blue light can interfere with your natural sleep hormones. Create a relaxing bedtime routine: perhaps a warm bath, some gentle stretching, reading, or listening to calming music. Your bedroom should be your sleep sanctuary - cool, dark, and quiet.",
            "Sleep troubles can really affect how we feel during the day, making everything seem harder. Consider making your bedroom environment optimal: aim for around 65-68°F (18-20°C), use blackout curtains or an eye mask, and minimize noise. A warm bath before bed can help your body temperature drop afterward, which signals sleepiness. Some people find gentle stretching, meditation, or reading helps them unwind.",
            "If your mind races at bedtime with worries or tomorrow's tasks, try the 'worry window' technique: set aside 10-15 minutes earlier in the day (not near bedtime) to write down your concerns and potential solutions. Then, when those thoughts pop up at bedtime, remind yourself that worry time is over and you've already addressed them. This helps create boundaries between productive problem-solving and unproductive nighttime anxiety.",
            "Sleep hygiene is like personal hygiene - it requires consistent daily habits to be effective. Try to avoid caffeine after 2 PM, as it can stay in your system for 6-8 hours. Also, while it might seem like alcohol helps you fall asleep, it actually disrupts your sleep quality later in the night. If you can't fall asleep within 20 minutes, get up and do a quiet, non-stimulating activity until you feel sleepy.",
            "Creating a 'sleep ritual' can signal to your brain that it's time to wind down. This might include dimming lights 1-2 hours before bed, doing some gentle yoga or stretching, journaling about three good things from your day, or practicing gratitude. Your brain needs time to transition from the active day to restful night. Consistency is key - try to do the same routine every night.",
            "If sleep problems persist, it might be worth examining your daytime habits too. Getting natural sunlight in the morning helps regulate your circadian rhythm, and regular exercise (but not too close to bedtime) can improve sleep quality. Also, try to use your bed only for sleep - not for studying, watching TV, or scrolling your phone. This helps your brain associate your bed with sleep."
        ]
        
        self.motivational_quotes = [
            "\"You are braver than you believe, stronger than you seem, and smarter than you think.\" - A.A. Milne",
            "\"Progress, not perfection.\" - Anonymous",
            "\"You don't have to be great to get started, but you have to get started to be great.\" - Les Brown",
            "\"Every expert was once a beginner.\" - Helen Hayes",
            "\"It's okay to be a masterpiece and a work in progress simultaneously.\" - Sophia Bush",
            "\"You are enough, just as you are.\" - Anonymous",
            "\"Small steps in the right direction can turn out to be the biggest step of your life.\" - Anonymous",
            "\"Your mental health is a priority. Your happiness is essential. Your self-care is a necessity.\" - Anonymous",
            "\"The only impossible journey is the one you never begin.\" - Tony Robbins",
            "\"Believe you can and you're halfway there.\" - Theodore Roosevelt",
            "\"Success is not final, failure is not fatal: it is the courage to continue that counts.\" - Winston Churchill",
            "\"You have been assigned this mountain to show others it can be moved.\" - Mel Robbins",
            "\"The comeback is always stronger than the setback.\" - Anonymous",
            "\"Your current situation is not your final destination.\" - Anonymous",
            "\"Difficult roads often lead to beautiful destinations.\" - Zig Ziglar",
            "\"You are never too old to set another goal or to dream a new dream.\" - C.S. Lewis",
            "\"The only way to do great work is to love what you do.\" - Steve Jobs",
            "\"Don't watch the clock; do what it does. Keep going.\" - Sam Levenson",
            "\"It always seems impossible until it's done.\" - Nelson Mandela",
            "\"The future belongs to those who believe in the beauty of their dreams.\" - Eleanor Roosevelt"
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
