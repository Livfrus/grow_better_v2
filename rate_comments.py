import json 
from openai import OpenAI

# 1. json parsing
# 2. db update 요청까지 CommentRater 내부에 작성
class CommentRater:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/engines/davinci/completions"

    def rate_comment(self, comment):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        prompt = f"Generate a response based on comment: {comment}"
        data = {
            "prompt": prompt,
            "max_tokens": 50  # Adjust as needed
        }

        try:
            response = requests.post(self.endpoint, json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error interacting with GPT API: {e}")
            return {"error": str(e)}