class MentalHealthResources:
    """
    A collection of verified mental health resources and support information.
    
    This class provides access to crisis helplines, counseling services, 
    and general mental health resources for students.
    """
    
    def __init__(self):
        # Crisis and emergency resources
        self.crisis_resources = {
            "National Suicide Prevention Lifeline": {
                "phone": "988",
                "description": "24/7 crisis support",
                "website": "suicidepreventionlifeline.org"
            },
            "Crisis Text Line": {
                "phone": "Text HOME to 741741",
                "description": "24/7 text-based crisis support",
                "website": "crisistextline.org"
            },
            "National Sexual Assault Hotline": {
                "phone": "1-800-656-4673",
                "description": "24/7 confidential support",
                "website": "rainn.org"
            },
            "SAMHSA National Helpline": {
                "phone": "1-800-662-4357",
                "description": "24/7 treatment referral service",
                "website": "samhsa.gov"
            }
        }
        
        # General mental health resources
        self.general_resources = {
            "National Alliance on Mental Illness (NAMI)": {
                "website": "nami.org",
                "description": "Mental health education, support groups, and advocacy"
            },
            "Mental Health America": {
                "website": "mhanational.org",
                "description": "Mental health screening tools and resources"
            },
            "Anxiety and Depression Association of America": {
                "website": "adaa.org",
                "description": "Information and resources for anxiety and depression"
            },
            "Headspace": {
                "website": "headspace.com",
                "description": "Meditation and mindfulness app (student discounts available)"
            },
            "Calm": {
                "website": "calm.com",
                "description": "Sleep stories, meditation, and relaxation app"
            },
            "7 Cups": {
                "website": "7cups.com",
                "description": "Free emotional support through trained listeners"
            }
        }
        
        # Student-specific resources
        self.student_resources = {
            "Campus Counseling Centers": "Most colleges offer free or low-cost counseling services. Check your student portal or contact student services.",
            "Student Health Centers": "Many universities provide mental health services as part of student health programs.",
            "Academic Support": "If stress is academic-related, consider tutoring services, study groups, or meeting with academic advisors.",
            "Student Organizations": "Join clubs or support groups related to mental health awareness and peer support."
        }
        
        # Wellness tips and techniques
        self.wellness_techniques = {
            "Breathing Exercises": [
                "Box Breathing: Inhale for 4, hold for 4, exhale for 4, hold for 4",
                "4-7-8 Breathing: Inhale for 4, hold for 7, exhale for 8",
                "Deep Belly Breathing: Place one hand on chest, one on belly. Focus on breathing so only the belly hand moves"
            ],
            "Stress Management": [
                "Take regular 5-10 minute breaks while studying",
                "Practice the Pomodoro Technique: 25 minutes work, 5 minute break",
                "Try progressive muscle relaxation",
                "Go for a short walk or do light exercise",
                "Listen to calming music or nature sounds"
            ],
            "Time Management": [
                "Use a planner or digital calendar",
                "Break large tasks into smaller, manageable steps",
                "Set realistic goals and deadlines",
                "Prioritize tasks using the Eisenhower Matrix",
                "Learn to say no to non-essential commitments"
            ],
            "Sleep Hygiene": [
                "Keep a consistent sleep schedule",
                "Avoid screens 1 hour before bedtime",
                "Create a relaxing bedtime routine",
                "Keep your bedroom cool, dark, and quiet",
                "Avoid caffeine late in the day"
            ],
            "Mindfulness": [
                "Practice 5-minute daily meditation",
                "Try the 5-4-3-2-1 grounding technique",
                "Keep a gratitude journal",
                "Practice mindful eating",
                "Take mindful walks without distractions"
            ]
        }
    
    def get_emergency_resources(self):
        """Return emergency/crisis mental health resources."""
        response = "🚨 **IMMEDIATE HELP NEEDED?** 🚨\n\n"
        response += "If you're in crisis or having thoughts of self-harm:\n"
        response += "• Call 988 (Suicide & Crisis Lifeline) - Available 24/7\n"
        response += "• Text HOME to 741741 (Crisis Text Line)\n"
        response += "• Call 911 or go to your nearest emergency room\n\n"
        response += "Remember: You are not alone, and help is available. Your life has value."
        return response
    
    def get_general_resources(self):
        """Return general mental health resources."""
        response = "💙 **Mental Health Resources** 💙\n\n"
        
        for name, info in self.general_resources.items():
            response += f"• **{name}**: {info['description']}\n"
            response += f"  Website: {info['website']}\n\n"
        
        return response
    
    def get_student_resources(self):
        """Return student-specific mental health resources."""
        response = "🎓 **Student Mental Health Resources** 🎓\n\n"
        
        for resource, description in self.student_resources.items():
            response += f"• **{resource}**: {description}\n\n"
        
        return response
    
    def get_wellness_technique(self, category):
        """
        Get wellness techniques for a specific category.
        
        Args:
            category (str): Category of wellness technique
            
        Returns:
            str: Formatted wellness techniques
        """
        if category.title() in self.wellness_techniques:
            techniques = self.wellness_techniques[category.title()]
            response = f"**{category.title()} Techniques:**\n\n"
            for technique in techniques:
                response += f"• {technique}\n"
            return response
        else:
            available_categories = ", ".join(self.wellness_techniques.keys())
            return f"Available categories: {available_categories}"
    
    def get_all_wellness_techniques(self):
        """Return all wellness techniques organized by category."""
        response = "🌱 **Wellness Techniques & Tips** 🌱\n\n"
        
        for category, techniques in self.wellness_techniques.items():
            response += f"**{category}:**\n"
            for technique in techniques:
                response += f"• {technique}\n"
            response += "\n"
        
        return response
    
    def search_resources(self, keyword):
        """
        Search for resources containing a specific keyword.
        
        Args:
            keyword (str): The keyword to search for
            
        Returns:
            list: List of matching resources
        """
        keyword_lower = keyword.lower()
        matches = []
        
        # Search in general resources
        for name, info in self.general_resources.items():
            if keyword_lower in name.lower() or keyword_lower in info['description'].lower():
                matches.append(f"**{name}**: {info['description']} - {info['website']}")
        
        # Search in crisis resources
        for name, info in self.crisis_resources.items():
            if keyword_lower in name.lower() or keyword_lower in info['description'].lower():
                matches.append(f"**{name}**: {info['description']} - {info['phone']}")
        
        # Search in wellness techniques
        for category, techniques in self.wellness_techniques.items():
            if keyword_lower in category.lower():
                matches.append(f"**{category} Techniques**: {', '.join(techniques[:2])}...")
            else:
                for technique in techniques:
                    if keyword_lower in technique.lower():
                        matches.append(f"**{category}**: {technique}")
        
        return matches if matches else [f"No resources found for '{keyword}'. Try searching for: stress, anxiety, sleep, breathing, or meditation."]
