import os
import requests

def get_response(prompt):
    api_key = os.getenv('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')

    response = requests.post(
        'https://api.openai.com/v1/engines/davinci-codex/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        },
        json={
            'prompt': prompt,
            'max_tokens': 100
        }
    )

    return response.json()['choices'][0]['text'].strip()
