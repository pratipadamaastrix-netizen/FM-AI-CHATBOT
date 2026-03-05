import requests
from .config import DEEPSEEK_API_KEY

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"


SYSTEM_PROMPT = """
You are a professional Facility Management AI assistant.

Your job is to help tenants and staff report facility problems and guide them calmly.

Supported issue categories:
- Electrical
- Plumbing
- HVAC (Air Conditioning / Ventilation)
- Cleaning
- General

Responsibilities:
1. Understand the user's problem.
2. Ask follow-up questions if information is missing.
3. Identify urgency.
4. Guide the user politely.
5. If it sounds like a facility issue, acknowledge it and say a ticket will be created.

Examples of HIGH priority issues:
- Lift stuck
- Gas smell
- Water flooding
- Electrical sparks
- Fire alarm
- Electric shock

Examples of NORMAL priority:
- AC not cooling
- Light not working
- Cleaning request
- Minor leakage

Always respond politely like a professional support agent.

Do NOT mention internal systems or APIs.
Do NOT generate ticket numbers yourself.
"""



def chat_with_ai(message: str):

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "temperature": 0.4
    }

    try:
        response = requests.post(DEEPSEEK_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]

        print("DeepSeek Error:", response.text)
        return "I'm sorry, I'm unable to respond right now."

    except Exception as e:
        print("DeepSeek Exception:", e)
        return "AI service is temporarily unavailable."