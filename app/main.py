"""
SmartEscalate AI
Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

from app.database.database import Base
from app.database.database import engine

# Import models so SQLAlchemy can create tables
import app.database.models


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(

    title="SmartEscalate AI",

    version="1.0.0"

)


# CORS

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)


app.include_router(router)