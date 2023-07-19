from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow requests from any origin

# Set up OpenAI API credentials
openai.api_key = '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'  # Replace with your OpenAI API key

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']

    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=message,
            max_tokens=1000,
            temperature=0.6,
            n=1,
            stop=None
        )
        reply = response.choices[0].text.strip()
    except Exception as e:
        reply = "I apologize, but I'm unable to provide a response at the moment."

    # Add CORS headers to the response
    response = jsonify({'reply': reply})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Set the Access-Control-Allow-Origin header to allow all origins
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
