from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

res = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hola, qui ets?"}]
)
print(res.choices[0].message.content)

