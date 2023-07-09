import requests
import json
from PIL import Image
import requests

url = "https://stablediffusionapi.com/api/v3/text2img"
key = "Vh9xnTAnytJX6u2jPyCtbyG7xU2fsrUvXtose4iNQFPbYMbUOZxYJ3wqpOYu"

def createImage(prompt):

  payload = json.dumps({
    "key": key,
    "prompt": prompt,
    "negative_prompt": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "20",
    "seed": None,
    "guidance_scale": 7.5,
    "safety_checker": "yes",
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "webhook": None,
    "track_id": None
  })

  headers = {
    'Content-Type': 'application/json'
  }

  try:
    response = requests.request("POST", url, headers=headers, data=payload).json()['output'][0]
    img = Image.open(requests.get(response, stream=True).raw)
    img.show()
  except:
    response = "Sorry, I don't understand that. Please try again."
  # print(response)
  return response