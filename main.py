import keyboard
import requests
import json
import openai
from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap
import random
import os
import time

openai.api_key = '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'
for i in range(10):
    url = "https://inshorts.deta.dev/news?category=all"
    response = requests.get(url)

    # Check if the response contains valid JSON data
    try:
        json_data = response.json()
    except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON data")
        json_data = None

    # Continue with the rest of your program only if valid JSON data was retrieved
    if json_data:
        # Use a set to keep track of spoken titles
        spoken_titles = set()

        # Open the news.txt file in read mode
        with open("news.txt", "r") as f:
            # Read all the lines from the file
            existing_titles = set(f.read().splitlines())

        # Add the existing titles to the spoken titles set
        spoken_titles |= existing_titles

        # Open the news.txt file in append mode
        with open("news.txt", "a", encoding='utf-8') as f:
            for news_item in json_data["data"]:
                title = news_item["title"].strip()

                # Replace Rupee sign with Rupees word
                title = title.replace('₹', 'Rupees')

                # Replace Dollar sign with Dollars word
                title = title.replace('$', 'Dollars')

                # Replace Euro sign with Euros word
                title = title.replace('€', 'Euros')

            
                with open("news.txt", "r") as file:
                    news = file.read().strip()
                    
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": f"re write this + {title}"}
                    ]
                )
                OP = response['choices'][0]['message']['content']
                OP = OP.replace('"', '')
                with open("news.txt", "r") as file:
                    if OP in file.read():
                        print("This line has already been added to the file.")
                    else:
                        with open("news.txt", "a") as file:
                            file.write(OP + "\n")
                            print("Added the following line to the file: " + OP)

                        

