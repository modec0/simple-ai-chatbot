import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

SYSTEM_PROMPT = "You are a helpful, friendly AI assistant."


def get_response(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return response.choices[0].message.content


def main():
    print("Simple AI Chatbot (type 'exit' to quit)")
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Bot: Goodbye!")
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            reply = get_response(messages)
        except Exception as e:
            print(f"Bot: Error - {e}")
            continue

        messages.append({"role": "assistant", "content": reply})
        print(f"Bot: {reply}")


if __name__ == "__main__":
    main()
