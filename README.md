# 🤖 AI Chatbot API

A production-style **AI Chatbot Backend API** built with **FastAPI, PostgreSQL, JWT Authentication, and OpenRouter/Gemini**.

The project provides persistent conversations, user authentication, conversation ownership, and real-time streaming responses through a clean REST API architecture.

---

## 🚀 Features

* ⚡ FastAPI backend
* 🤖 Gemini AI through OpenRouter
* 💬 Persistent conversation memory
* 🗂️ Multiple conversations per user
* 👤 User registration and login
* 🔐 JWT-based authentication
* 🔑 Bcrypt password hashing
* 🛡️ Protected API endpoints
* 🔒 Conversation ownership authorization
* 🌊 Streaming AI responses
* 🗄️ PostgreSQL database
* 📊 Database indexes for efficient queries
* ⚠️ Global error handling
* 🧩 Modular backend architecture
* 🔐 Environment variables for secrets and configuration

---

## 🏗️ Architecture

```text
Client
   │
   ▼
FastAPI
   │
   ├── Authentication / JWT
   │
   ├── Request Middleware
   │
   ├── Chat Router
   │
   ├── Conversation Memory
   │
   ▼
PostgreSQL
   │
   ▼
OpenRouter API
   │
   ▼
Gemini Model
```

---

## 🛠️ Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Backend development         |
| FastAPI    | REST API framework          |
| PostgreSQL | Persistent database         |
| Psycopg    | PostgreSQL connection       |
| OpenRouter | AI model API                |
| Gemini     | LLM                         |
| OpenAI SDK | OpenRouter API integration  |
| JWT        | Authentication              |
| Bcrypt     | Password hashing            |
| Pydantic   | Request/response validation |
| Uvicorn    | ASGI server                 |

---

## 📁 Project Structure

```text
AI CHATBOT API/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── dependencies.py
│   ├── middleware.py
│   ├── memory.py
│   ├── database.py
│   ├── auth.py
│   │
│   ├── routers/
│   │   ├── chat.py
│   │   └── auth.py
│   │
│   └── services/
│       └── openrouter.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication

The API uses **JWT-based authentication**.

### Registration

```http
POST /auth/register
```

Example request:

```json
{
  "username": "inder",
  "email": "inder@example.com",
  "password": "yourpassword"
}
```

---

### Login

```http
POST /auth/login
```

The API returns an access token:

```json
{
  "access_token": "YOUR_JWT_TOKEN",
  "token_type": "bearer"
}
```

Use this token to access protected endpoints.

```text
Authorization: Bearer YOUR_JWT_TOKEN
```

---

## 💬 Chat API

### Create a New Conversation

```http
POST /chat
```

Request:

```json
{
  "message": "My name is Inder",
  "conversation_id": null
}
```

Response:

```json
{
  "response": "Nice to meet you, Inder!",
  "conversation_id": 1
}
```

---

### Continue a Conversation

```json
{
  "message": "What is my name?",
  "conversation_id": 1
}
```

The API retrieves the previous messages from PostgreSQL and sends the conversation history to the AI model.

---

## 🌊 Streaming Responses

The project also supports real-time AI response streaming.

```http
POST /chat/stream
```

Instead of waiting for the complete AI response, the server streams generated text as it becomes available.

This provides a more responsive chatbot experience.

---

## 🗄️ Database Design

The project uses PostgreSQL with three main tables.

### Users

```text
users
├── id
├── username
├── email
├── password_hash
└── created_at
```

### Conversations

```text
conversations
├── id
├── user_id
└── created_at
```

### Messages

```text
messages
├── id
├── conversation_id
├── role
├── content
└── created_at
```

Relationships:

```text
User
 │
 └── Conversations
        │
        └── Messages
```

Foreign keys and indexes are used to maintain data integrity and improve query performance.

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_api_key
MODEL_NAME=your_model_name
DATABASE_URL=your_postgresql_connection_string
JWT_SECRET=your_secret_key
```

> Never commit your `.env` file or API keys to GitHub.

---

## ▶️ Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/InderjotSingh17/genai-chatbot-backend.git
cd genai-chatbot-backend
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create `.env` and add your:

* OpenRouter API key
* Model name
* PostgreSQL database URL
* JWT secret

### 6. Start the server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to:

* Register users
* Login
* Authorize using JWT
* Send chat messages
* Continue conversations
* Test streaming endpoints

---

## 🔒 Security

The project implements several security practices:

* Passwords are hashed using bcrypt
* JWT tokens protect authenticated endpoints
* Conversations are associated with specific users
* Users cannot access another user's conversations
* Secrets are stored in environment variables
* `.env` is excluded from Git
* `.venv` is excluded from Git

---

## 🧠 What This Project Demonstrates

This project demonstrates practical backend and GenAI engineering concepts including:

* REST API development
* Authentication and authorization
* JWT implementation
* Password security
* LLM API integration
* Conversation memory
* Database design
* PostgreSQL integration
* Streaming responses
* Middleware
* Error handling
* API architecture
* Environment-based configuration

---

## 🚧 Future Improvements

Possible future extensions include:

* Redis-based caching
* Rate limiting
* Conversation management endpoints
* Message pagination
* WebSocket-based streaming
* RAG with document ingestion
* Tool calling
* AI agents
* Frontend chatbot interface
* Docker deployment
* Cloud deployment

---

## 👨‍💻 Author

**Inderjot Singh**

B.Tech CSE (AI/ML)

GitHub:
https://github.com/InderjotSingh17

LinkedIn:
https://www.linkedin.com/in/inderjot-singh-0471a6237/

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
