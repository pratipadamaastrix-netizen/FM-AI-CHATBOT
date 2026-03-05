# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import Base, engine
from backend.app.routes import chat

# Create database tables if not exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Facility Management AI Chatbot MVP",
    description="Backend for handling tenant and staff facility issue reports via chat",
    version="1.0.0"
)

# CORS settings
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api", tags=["Chat"])

# Root endpoint for testing
@app.get("/")
def root():
    return {"message": "Facility Management AI Chatbot Backend is running"}