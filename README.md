# FM AI Chatbot

An AI-powered Facility Management Chatbot designed to help users report issues, generate service tickets automatically, and interact with an intelligent assistant.

This system allows residents or employees to report problems such as electricity issues, lift malfunction, plumbing problems, or other facility-related complaints. The chatbot processes the request and generates a ticket for the facility management team.

---

## 🚀 Features

- AI-powered chatbot interaction
- Automatic ticket generation
- Conversation history stored in database
- Image recognition support for issue detection
- Backend API for facility issue management
- Simple and responsive web interface

---

## 🧠 AI Integration

The chatbot integrates AI models to understand user queries and provide responses.

Supported AI models:
- DeepSeek API
- Ollama (phi3:mini for local inference)
- OpenAI (optional)

---

## 🏗️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### AI
- DeepSeek API
- Ollama Local Models

### Frontend
- React.js
- HTML
- CSS
- JavaScript

### Other Tools
- Git
- GitHub
- Uvicorn Server

---

## 📂 Project Structure

FM_AI_CHATBOT
│
├── app
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── ai_integration.py
│ ├── utils.py
│ └── routers
│
├── frontend
│
├── venv
│
├── requirements.txt
│
└── README.md



---

## ⚙️ Installation

### 1. Clone the Repository
git clone https://github.com/pratipadamaastrix-netizen/FM-AI-CHATBOT.git


### 2. Navigate to the Project Folder
cd FM_AI_CHATBOT

### 3. Create Virtual Environment
python -m venv venv


### 4. Activate Virtual Environment

Windows:
venv\Scripts\activate


### 5. Install Dependencies
pip install -r requirements.txt


---

## ▶️ Running the Backend Server

Start the FastAPI server:
uvicorn app.main:app --reload


Server will start at:
http://127.0.0.1:8000


---

## 💬 Chatbot Workflow

1. User sends a message to the chatbot.
2. AI model processes the message.
3. If an issue is detected, a service ticket is generated.
4. Ticket is stored in the database.
5. Facility management team can review and resolve the issue.

---

## 🗄️ Database

The project uses **PostgreSQL** for storing:

- User messages
- Chat history
- Generated tickets
- Issue status

---


## 📌 Future Improvements

- Admin dashboard for ticket management
- Notification system
- Mobile app integration
- Multi-language chatbot
- Advanced AI issue detection

---

## 👨‍💻 Author

Pratipada Behera

---
