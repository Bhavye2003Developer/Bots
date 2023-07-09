''''
	Link - https://rapidapi.com/liuzhaolong765481/api/chatgpt-chatgpt3-5-chatgpt4
	Get API_KEY from Pricing option, choose 0$ plan and get the key

	This basically provides :
		1. Analyse text data
		2. Analyse Code
		3. Custom Prompt
'''

import os
import requests
from dotenv import load_dotenv

load_dotenv("keys.env")

if not os.path.exists("analyse"):
	os.mkdir("analyse")

url = "https://chatgpt-chatgpt3-5-chatgpt4.p.rapidapi.com/v1/chat/completions"

def chat(prompt):
	payload = {
		"model": "gpt-3.5-turbo",
		"messages": [
			{
				"role": "user",
				"content": prompt
			}
		],
		"temperature": 0.8
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
		"X-RapidAPI-Host": "chatgpt-chatgpt3-5-chatgpt4.p.rapidapi.com"
	}

	try:
		response = requests.post(url, json=payload, headers=headers).json()['choices'][0]['message']['content']
	except:
		response = "Sorry, I don't understand that. Please try again."

	return response

def doWork(question, file):
	try:
		f = open(f"analyse/{file}", "r")
	except:
		os.system(f"touch analyse/{file}")
		f = open(f"analyse/{file}", "r")
	data = f.read()
	if data == "":
		data = "No data available"
	f.close()
	prompt = f"Analyse the data : {data}"
	if question == "exit":
		return -1
	prompt += f"\nAnswer this Question based on analysis done: {question}"
	return chat(prompt)