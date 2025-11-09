#!/usr/bin/env python3
"""
Simple script to ask ChatGPT (GPT-4) to tell a joke.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "explain the ending of the movie TAR"}
    ]
)

print(response.choices[0].message.content)
