import os
from dotenv import load_dotenv
import cohere
import json

# load environment variables from .env file
load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

# The user introduces a given business topic
def generate_business_idea(topic):
    prompt = f"""
Act as a startup consultant. I'm interested in building a business in the area of "{topic}".
Please generate:
1. A unique startup idea.
2. Target audience and market.
3. How it can make money.
4. A 3-step launch plan.
5. How feasible is this in 2025?

Respond in JSON format.
"""
    response = co.chat(message=prompt, model='command-r')
    return response.text

if __name__ == "__main__":
    topic = input("Enter a topic you're interested in: ")
    result = generate_business_idea(topic)
    try:
        parsed = json.loads(result)
        print(json.dumps(parsed, indent=2))
    except json.JSONDecodeError:
        print("Raw response:\n", result)
