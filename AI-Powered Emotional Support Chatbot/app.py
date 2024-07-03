
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_session import Session  # Additional import for better session management
import openai
import os
import traceback  # For better error logging

app = Flask(__name__)
CORS(app)  # Enable CORS
app.secret_key = os.getenv('SECRET_KEY', 'your_fallback_secret_key')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"  # Configure server-side session handling
Session(app)  # Initialize the session service

openai.api_key = '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'  # Always use environment variables for keys

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a compassionate and thoughtful therapist. "
        "In urgent situations like wanting to harm oneself, suggest calling mental health hotlines. "
        "Here are some hotlines: [911, local mental health hotline]. "
        "Try to ask the user for their emotional state, and ask the user if he's happy or sad on a scale from one to ten"
        "Keep track of any emotional progress in the conversation, and if there's any imporovement adjust the emotional state scale."
        "You aim to understand and alleviate distress while ensuring professional help is sought when necessary."
    )
}

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        if 'chat_history' not in session:
            session['chat_history'] = [SYSTEM_PROMPT]
        
        session['chat_history'].append({"role": "user", "content": user_message})

        if "suicide" in user_message.lower() or "harm myself" in user_message.lower():
            urgent_response = "Please call 911 or a local mental health hotline immediately."
            session['chat_history'].append({"role": "assistant", "content": urgent_response})
            return jsonify({'response': urgent_response})
        
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=session['chat_history']
        )
        
        response_message = response.choices[0].message['content']
        session['chat_history'].append({"role": "assistant", "content": response_message})
        return jsonify({'response': response_message})
    except Exception as e:
        traceback.print_exc()  # This will print the stack trace to stderr
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
