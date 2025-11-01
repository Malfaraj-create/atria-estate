from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Atria Estate API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Atria Estate API", "version": "1.0.0", "status": "live"}

@app.get("/health")
def health():
    return {"status": "healthy", "database": "connected"}

@app.get("/api/properties")
def get_properties():
    return {
        "properties": [
            {
                "id": 1,
                "title": "Modern Studio in University City",
                "price": 1450,
                "bedrooms": 0,
                "bathrooms": 1,
                "city": "Philadelphia",
                "verified": True
            }
        ]
    }
