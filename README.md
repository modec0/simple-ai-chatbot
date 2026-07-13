simple-ai-chatbot
A simple AI chatbot built with Python using the OpenAI GPT API.
Features
Takes user input from the terminal
Sends it to GPT API
Returns AI-generated responses
Keeps conversation history in a session
Setup
```bash
git clone https://github.com/yourusername/simple-ai-chatbot.git
cd simple-ai-chatbot
pip install -r requirements.txt
cp .env.example .env
```
Edit `.env` and add your OpenAI API key.
Usage
```bash
python main.py
```
Type your message and press Enter. Type `exit` or `quit` to end the chat.
Project Structure
```
simple-ai-chatbot/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```
License
MIT
