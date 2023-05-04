import openai
from .env import env

openai.api_key = env.openai_key

test = openai.ChatCompletion.create(
    model="text-davinci-002",
    prompt="What the wheather?",
    temperature=0,
    frequency_penalty=0,
    presence_penalty=0.6,
    max_tokens=240
)

print(test)