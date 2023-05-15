from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = openai.get_response(message)
    return jsonify({ 'response': response })

if __name__ == "__main__":
    app.run(port=5000)
