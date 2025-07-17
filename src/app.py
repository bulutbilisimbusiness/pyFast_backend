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
    jwt_key_raw = os.getenv("JWT_KEY")
    jwt_key_fixed = jwt_key_raw.replace('\\n', '\n') if jwt_key_raw else None
    return {
        "jwt_key_exists": bool(jwt_key_raw),
        "jwt_key_length_raw": len(jwt_key_raw) if jwt_key_raw else 0,
        "jwt_key_length_fixed": len(jwt_key_fixed) if jwt_key_fixed else 0,
        "jwt_key_starts_with_raw": jwt_key_raw[:30] if jwt_key_raw else None,
        "jwt_key_starts_with_fixed": jwt_key_fixed[:30] if jwt_key_fixed else None,
        "jwt_key_lines_raw": jwt_key_raw.count('\n') if jwt_key_raw else 0,
        "jwt_key_lines_fixed": jwt_key_fixed.count('\n') if jwt_key_fixed else 0,
        "jwt_backslash_n_count": jwt_key_raw.count('\\n') if jwt_key_raw else 0
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