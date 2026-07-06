# 📝 AI Copywriting & Tone Transformer

An AI-powered command-line application that generates platform-specific marketing copy using the OpenRouter API. The application dynamically builds prompts based on user inputs such as product details, platform, tone, temperature, and top-p, then generates engaging copy using a Large Language Model (LLM).

---

## ✨ Features

- 🤖 AI-powered copy generation using OpenRouter API
- 🎯 Dynamic prompt compilation
- 📱 Platform-specific content generation
  - LinkedIn
  - Instagram
  - Email
- 🎭 Multiple writing tones
  - Professional
  - Friendly
  - Funny
  - Persuasive
- 🌡️ Adjustable Temperature
- 🎯 Adjustable Top-P
- 🔐 Secure API key management using `.env`
- 💻 Simple Command Line Interface (CLI)

---

## 🛠️ Tech Stack

- Python 3
- OpenRouter API
- Requests
- python-dotenv

---

## 📂 Project Structure

```text
copywriting-tone-transformer/
│
├── main.py
├── api.py
├── prompt.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Geetanshu29/copywriting-tone-transformer.git
```

Move into the project directory

```bash
cd copywriting-tone-transformer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 Example Workflow

```
Product Name:
Nike Air Max

Product Description:
Lightweight running shoes designed for athletes.

Platform:
Instagram

Tone:
Funny

Temperature:
0.8

Top P:
0.9
```

### Generated Output

```
🔥 Run faster than your excuses!

Meet the all-new Nike Air Max — built for speed,
comfort, and style.

🏃‍♂️ Grab yours today!

#Nike #Fitness #Running
```

---

## 📖 Learning Outcomes

This project demonstrates:

- Prompt Engineering
- Dynamic Prompt Generation
- OpenRouter API Integration
- LLM Parameter Tuning
- Environment Variable Management
- Python API Development

---

## 👨‍💻 Author

**Geetanshu Arora**

GitHub: https://github.com/Geetanshu29