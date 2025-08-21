// WellMind AI Frontend JavaScript

class WellMindChat {
    constructor() {
        this.API_BASE = '/api';
        this.isLoading = false;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadInitialData();
    }

    setupEventListeners() {
        // Message input
        const messageInput = document.getElementById('messageInput');
        const sendButton = document.getElementById('sendButton');

        messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        messageInput.addEventListener('input', (e) => {
            sendButton.disabled = !e.target.value.trim();
        });

        // Close panels when clicking outside
        document.addEventListener('click', (e) => {
            if (!e.target.closest('.side-panel') && !e.target.closest('.btn')) {
                this.closePanels();
            }
        });

        // Close modal when clicking outside
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal')) {
                this.closeEmergency();
            }
        });
    }

    async loadInitialData() {
        await this.loadResources();
    }

    async sendMessage() {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();

        if (!message || this.isLoading) return;

        // Add user message to chat
        this.addMessage(message, 'user');
        messageInput.value = '';
        document.getElementById('sendButton').disabled = true;

        // Hide welcome section
        const welcomeSection = document.getElementById('welcomeSection');
        if (welcomeSection) {
            welcomeSection.style.display = 'none';
        }

        try {
            this.setLoading(true);
            const response = await this.makeRequest('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message })
            });

            if (response.status === 'success') {
                this.addMessage(response.response, 'bot');
            } else {
                this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        } catch (error) {
            console.error('Error sending message:', error);
            this.addMessage('Sorry, I\'m having trouble connecting. Please check your connection and try again.', 'bot');
        } finally {
            this.setLoading(false);
        }
    }

    async sendQuickMessage(message) {
        const messageInput = document.getElementById('messageInput');
        messageInput.value = message;
        await this.sendMessage();
    }

    addMessage(content, type) {
        const chatMessages = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}-message`;

        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = type === 'bot' ? '<i class="fas fa-robot"></i>' : '<i class="fas fa-user"></i>';

        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';

        const messageText = document.createElement('p');
        messageText.textContent = content;

        const messageTime = document.createElement('span');
        messageTime.className = 'message-time';
        messageTime.textContent = this.formatTime(new Date());

        messageContent.appendChild(messageText);
        messageContent.appendChild(messageTime);

        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    formatTime(date) {
        return date.toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit'
        });
    }

    async clearChat() {
        try {
            await this.makeRequest('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: 'clear' })
            });

            const chatMessages = document.getElementById('chatMessages');
            chatMessages.innerHTML = `
                <div class="message bot-message">
                    <div class="message-avatar">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="message-content">
                        <p>Hello! I'm WellMind AI, and I'm here to support your mental health and wellbeing. How are you feeling today?</p>
                        <span class="message-time">${this.formatTime(new Date())}</span>
                    </div>
                </div>
            `;

            // Show welcome section again
            const welcomeSection = document.getElementById('welcomeSection');
            if (welcomeSection) {
                welcomeSection.style.display = 'block';
            }
        } catch (error) {
            console.error('Error clearing chat:', error);
        }
    }

    async toggleHistory() {
        try {
            const response = await this.makeRequest('/history');
            if (response.status === 'success' && response.history.length > 0) {
                let historyHtml = '<div class="history-content"><h4>Recent Conversation:</h4>';
                response.history.slice(-10).forEach((exchange, index) => {
                    historyHtml += `
                        <div class="history-item">
                            <strong>You:</strong> ${exchange.user}<br>
                            <strong>WellMind AI:</strong> ${exchange.bot ? exchange.bot.substring(0, 100) + '...' : 'No response'}
                        </div>
                    `;
                });
                historyHtml += '</div>';
                this.showNotification('Conversation History', historyHtml);
            } else {
                this.showNotification('History', 'No conversation history available.');
            }
        } catch (error) {
            console.error('Error getting history:', error);
            this.showNotification('Error', 'Unable to load conversation history.');
        }
    }

    async toggleResources() {
        const panel = document.getElementById('resourcesPanel');
        const isActive = panel.classList.contains('active');

        this.closePanels();

        if (!isActive) {
            panel.classList.add('active');
            if (!panel.dataset.loaded) {
                await this.loadResources();
                panel.dataset.loaded = 'true';
            }
        }
    }

    async loadResources() {
        try {
            const response = await this.makeRequest('/resources');
            if (response.status === 'success') {
                const content = document.getElementById('resourcesContent');
                content.innerHTML = `
                    <div class="resources-section">
                        <h4><i class="fas fa-exclamation-triangle"></i> Emergency Resources</h4>
                        <div class="resource-content">${this.formatResourceText(response.emergency)}</div>
                    </div>
                    <div class="resources-section">
                        <h4><i class="fas fa-heart"></i> General Resources</h4>
                        <div class="resource-content">${this.formatResourceText(response.general)}</div>
                    </div>
                    <div class="resources-section">
                        <h4><i class="fas fa-graduation-cap"></i> Student Resources</h4>
                        <div class="resource-content">${this.formatResourceText(response.student)}</div>
                    </div>
                `;
            }
        } catch (error) {
            console.error('Error loading resources:', error);
            document.getElementById('resourcesContent').innerHTML = '<div class="error">Unable to load resources.</div>';
        }
    }

    toggleTechniques() {
        const panel = document.getElementById('techniquesPanel');
        const isActive = panel.classList.contains('active');

        this.closePanels();

        if (!isActive) {
            panel.classList.add('active');
        }
    }

    async loadTechniques(category) {
        try {
            const response = await this.makeRequest(`/techniques/${category}`);
            if (response.status === 'success') {
                const content = document.getElementById('techniqueDetails');
                content.innerHTML = `
                    <div class="technique-content">
                        <h4>${category.charAt(0).toUpperCase() + category.slice(1)} Techniques</h4>
                        <div class="technique-text">${this.formatResourceText(response.techniques)}</div>
                    </div>
                `;

                // Update active button
                document.querySelectorAll('.technique-btn').forEach(btn => btn.classList.remove('active'));
                event.target.closest('.technique-btn').classList.add('active');
            }
        } catch (error) {
            console.error('Error loading techniques:', error);
            document.getElementById('techniqueDetails').innerHTML = '<div class="error">Unable to load techniques.</div>';
        }
    }

    formatResourceText(text) {
        return text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/• /g, '<li>')
            .replace(/\n\n/g, '</ul><br><ul>')
            .replace(/^/, '<ul>')
            .replace(/$/, '</ul>')
            .replace(/<ul><\/ul>/g, '')
            .replace(/\n/g, '<br>');
    }

    showEmergency() {
        document.getElementById('emergencyModal').classList.add('active');
    }

    closeEmergency() {
        document.getElementById('emergencyModal').classList.remove('active');
    }

    closePanels() {
        document.querySelectorAll('.side-panel').forEach(panel => {
            panel.classList.remove('active');
        });
    }

    setLoading(loading) {
        this.isLoading = loading;
        const indicator = document.getElementById('loadingIndicator');
        const sendButton = document.getElementById('sendButton');

        if (loading) {
            indicator.classList.add('active');
            sendButton.disabled = true;
        } else {
            indicator.classList.remove('active');
            const messageInput = document.getElementById('messageInput');
            sendButton.disabled = !messageInput.value.trim();
        }
    }

    async makeRequest(endpoint, options = {}) {
        const url = `${this.API_BASE}${endpoint}`;
        const response = await fetch(url, {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }

    showNotification(title, content) {
        // Create a simple notification modal
        const modal = document.createElement('div');
        modal.className = 'modal active';
        modal.innerHTML = `
            <div class="modal-content">
                <div class="modal-header">
                    <h3>${title}</h3>
                    <button class="close-btn" onclick="this.closest('.modal').remove()">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                <div class="modal-body">
                    ${content}
                </div>
            </div>
        `;

        document.body.appendChild(modal);

        // Auto-remove after 10 seconds
        setTimeout(() => {
            if (modal.parentNode) {
                modal.remove();
            }
        }, 10000);
    }
}

// Global functions for HTML onclick handlers
let wellMindChat;

function sendMessage() {
    wellMindChat.sendMessage();
}

function sendQuickMessage(message) {
    wellMindChat.sendQuickMessage(message);
}

function clearChat() {
    wellMindChat.clearChat();
}

function toggleHistory() {
    wellMindChat.toggleHistory();
}

function toggleResources() {
    wellMindChat.toggleResources();
}

function toggleTechniques() {
    wellMindChat.toggleTechniques();
}

function loadTechniques(category) {
    wellMindChat.loadTechniques(category);
}

function showEmergency() {
    wellMindChat.showEmergency();
}

function closeEmergency() {
    wellMindChat.closeEmergency();
}

// Initialize the chat when the page loads
document.addEventListener('DOMContentLoaded', () => {
    wellMindChat = new WellMindChat();
});

// Add some utility functions for better UX
document.addEventListener('DOMContentLoaded', () => {
    // Add typing indicator
    function showTypingIndicator() {
        const chatMessages = document.getElementById('chatMessages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot-message typing-indicator';
        typingDiv.id = 'typingIndicator';
        typingDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-robot"></i>
            </div>
            <div class="message-content">
                <p class="typing-dots">
                    <span></span>
                    <span></span>
                    <span></span>
                </p>
            </div>
        `;
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function hideTypingIndicator() {
        const typingIndicator = document.getElementById('typingIndicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    // Add typing animation CSS
    const style = document.createElement('style');
    style.textContent = `
        .typing-dots {
            display: flex;
            gap: 4px;
            padding: 20px !important;
        }
        
        .typing-dots span {
            width: 8px;
            height: 8px;
            background: #667eea;
            border-radius: 50%;
            animation: typing 1.4s infinite;
        }
        
        .typing-dots span:nth-child(2) {
            animation-delay: 0.2s;
        }
        
        .typing-dots span:nth-child(3) {
            animation-delay: 0.4s;
        }
        
        @keyframes typing {
            0%, 60%, 100% {
                transform: scale(1);
                opacity: 0.5;
            }
            30% {
                transform: scale(1.2);
                opacity: 1;
            }
        }
        
        .resources-section {
            margin-bottom: 2rem;
        }
        
        .resources-section h4 {
            color: #667eea;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .resource-content {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #667eea;
        }
        
        .technique-content {
            margin-top: 1rem;
            padding: 1rem;
            background: #f8f9fa;
            border-radius: 0.5rem;
            border-left: 4px solid #667eea;
        }
        
        .technique-content h4 {
            color: #667eea;
            margin-bottom: 1rem;
        }
        
        .history-content {
            max-height: 300px;
            overflow-y: auto;
        }
        
        .history-item {
            padding: 1rem;
            margin-bottom: 1rem;
            background: #f8f9fa;
            border-radius: 0.5rem;
            border-left: 4px solid #667eea;
        }
        
        .error {
            color: #e74c3c;
            text-align: center;
            padding: 2rem;
        }
    `;
    document.head.appendChild(style);

    // Enhance the sendMessage function to show typing indicator
    const originalSendMessage = wellMindChat.sendMessage;
    wellMindChat.sendMessage = async function() {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();

        if (!message || this.isLoading) return;

        // Add user message to chat
        this.addMessage(message, 'user');
        messageInput.value = '';
        document.getElementById('sendButton').disabled = true;

        // Hide welcome section
        const welcomeSection = document.getElementById('welcomeSection');
        if (welcomeSection) {
            welcomeSection.style.display = 'none';
        }

        // Show typing indicator
        showTypingIndicator();

        try {
            this.setLoading(true);
            const response = await this.makeRequest('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message })
            });

            // Hide typing indicator
            hideTypingIndicator();

            if (response.status === 'success') {
                this.addMessage(response.response, 'bot');
            } else {
                this.addMessage('Sorry, I encountered an error. Please try again.', 'bot');
            }
        } catch (error) {
            console.error('Error sending message:', error);
            hideTypingIndicator();
            this.addMessage('Sorry, I\'m having trouble connecting. Please check your connection and try again.', 'bot');
        } finally {
            this.setLoading(false);
        }
    };
});
