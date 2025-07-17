from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks
import os

app = FastAPI(title="PyFast API", version="1.0.0")

# Health check endpoint for deployment platforms
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "PyFast API is running"}

# JWT Key debug endpoint
@app.get("/api/debug-jwt")
async def debug_jwt():
    jwt_key = os.getenv("JWT_KEY")
    return {
        "jwt_key_exists": bool(jwt_key),
        "jwt_key_length": len(jwt_key) if jwt_key else 0,
        "jwt_key_starts_with": jwt_key[:30] if jwt_key else None,
        "jwt_key_ends_with": jwt_key[-30:] if jwt_key else None,
        "jwt_key_lines": jwt_key.count('\n') if jwt_key else 0
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(challenge.router, prefix="/api")
app.include_router(webhooks.router, prefix="/webhooks")