from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import challenge, webhooks

app = FastAPI(title="PyFast API", version="1.0.0")

# Health check endpoint for deployment platforms
@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "message": "PyFast API is running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(challenge.router, prefix="/api")
app.include_router(webhooks.router, prefix="/webhooks")