from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from openai import OpenAI
from config import settings
# The client will use the environment variable OPENAI_API_KEY,
# which is loaded via the settings object.
client = OpenAI(api_key=settings.openai_api_key)

# from dotenv import load_dotenv
# import os
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# client = OpenAI()

# if openai_api_key:
#     client = OpenAI(api_key=openai_api_key)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def instant():
    message = """
        You are on a website that has just been deployed to production for the first time!
        Please reply with an enthusiastic announcement to welcome visitors to the site, explaining that it is live on production for the first time!
    """
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content.replace("\n", "<br/>")
    html = f"<html><head><title>Live in an Instant!</title></head><body><p>{reply}</p></body></html>"
    return html