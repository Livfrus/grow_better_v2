from openai import OpenAI
import os
from dotenv import load_dotenv

# 1. json parsing
# class CommentRater: output은 json으로 return
# 항상 prompt.txt 가져오기 
class CommentRater:
  
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY') 

    def rate_comment(self, comment_content):
        
      client = OpenAI() # module import
      with open('prompt.txt', 'r') as f:
          content = f.read() # prompt file content에 저장
        
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          response_format={"type": "json_object"}, # output: json 활성화
          messages=[
              {"role": "system", "content": content},
              {"role": "user", "content": comment_content}
          ]
      )
        
      return_str = response.choices[0].message.content
      import json
      result_dict = json.loads(return_str) # return_str 불러와서 json 형식으로 변환
      
      # 결과값 json으로 리턴해 저장하기
      return result_dict