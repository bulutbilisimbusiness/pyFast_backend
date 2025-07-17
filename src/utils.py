from fastapi import HTTPException
from clerk_backend_api import Clerk, AuthenticateRequestOptions
import os
from dotenv import load_dotenv

# Load .env from backend root directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

# Try loading from current directory as well
load_dotenv()


clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

def authenticate_and_get_user_details(request):
    try:
        jwt_key = os.getenv("JWT_KEY")
        # Fix JWT key format: convert \\n to actual newlines
        if jwt_key:
            jwt_key = jwt_key.replace('\\n', '\n')
        
        request_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=[
                    "http://localhost:5173", 
                    "http://localhost:5174",
                    "http://localhost:3000",
                    "http://127.0.0.1:5173",
                    "http://127.0.0.1:5174",
                    "http://127.0.0.1:3000",
                    "https://py-fast-frontend-railway.vercel.app",
                    "https://py-fast-frontend-railway-3wrua3sew.vercel.app"
                ],
                jwt_key=jwt_key
            )
        )

        if not request_state.is_signed_in:
            raise HTTPException(status_code=401, detail="Invalid token")

        user_id = request_state.payload.get("sub")

        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))