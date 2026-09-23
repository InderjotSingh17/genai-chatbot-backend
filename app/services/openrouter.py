from openai import OpenAI
from app.config import OPENROUTER_API_KEY,MODEL_NAME,SYSTEM_PROMPT,TEMPERATURE,MAX_TOKENS
client=OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
def generate_response(messages:list)->str:
    messages_with_system_prompt=[
        {
            "role":"system",
            "content":SYSTEM_PROMPT
        }
    ]+messages
    response=client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages_with_system_prompt,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE

    )
    return response.choices[0].message.content

def generate_stream(messages: list):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        max_tokens=300,
        stream=True
    )
    for chunk in response:
        if not chunk.choices:
            continue
        content = chunk.choices[0].delta.content
        if content:
            yield content