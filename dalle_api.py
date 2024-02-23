from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

client = OpenAI(
  organization='org-lbyAxolBvL4LR9S8bN1gbcfS',
)



# Function to call the Dalle-3 API
def get_dalle_image(prompt, size='1024x1024', n=1):
  api_key = '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'
  headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
  }
  data = {
    'model': 'dall-e-3',
    'prompt': prompt,
    'n': n,
    'size': size
  }
  response = requests.post('https://api.openai.com/v1/images/generations', headers=headers, json=data)

  if response.status_code == 200:
    response_json = response.json()  # Returns the JSON response containing the image
    image_url = response_json['data'][0]['url']  # Extract the image URL

    image_response = requests.get(image_url)
    if image_response.status_code == 200:
      image = Image.open(BytesIO(image_response.content))
      return image
    else:
      return f"Error fetching image: {image_response.status_code}"
  else:
    return f"Error: {response.status_code}, {response.text}"


