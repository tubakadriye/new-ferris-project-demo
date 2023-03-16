"""
Perform tweet sentiment analysis using OpenAI API.
Sentiment classifications are: positive, neutral, or negative
"""

import json
import sys
import openapi
from ferris_ef import context

payload = json.loads(sys.argv[1])
tweet = payload("tweet_text")
print("Tweet to analyze:", {tweet})

openai.api_key = context.secrets.get("OPENAI_API_KEY")

response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = f'Decide whether a Tweet\'s sentiment is positive, neutral, or negative.\n\nTweet: "{tweet}"\nSentiment:',
    temperature=0.7,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0,
)

print(f"Tweet sentiment: {response}")