from fastapi import HTTPException
from clerk_backend_api import Clerk, AuthenticateRequestOptions
import os
from dotenv import load_dotenv

# Load .env from backend root directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
print(f"DEBUG utils.py - Loading .env from: {dotenv_path}")
print(f"DEBUG utils.py - .env exists: {os.path.exists(dotenv_path)}")
load_dotenv(dotenv_path=dotenv_path)

# Try loading from current directory as well
load_dotenv()

print("DEBUG utils.py - CLERK_SECRET_KEY:", bool(os.getenv("CLERK_SECRET_KEY")))
print("DEBUG utils.py - JWT_KEY:", bool(os.getenv("JWT_KEY")))
clerk_key = os.getenv('CLERK_SECRET_KEY', 'NOT_FOUND')
print(f"DEBUG utils.py - CLERK_SECRET_KEY value: {clerk_key[:20]}...")


clerk_sdk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

def authenticate_and_get_user_details(request):
    try:
        jwt_key = os.getenv("JWT_KEY")
        print(f"DEBUG: JWT_KEY exists: {bool(jwt_key)}")
        print(f"DEBUG: JWT_KEY preview: {jwt_key[:50] + '...' if jwt_key else 'None'}")
        print(f"DEBUG: Request headers: {dict(request.headers)}")
        
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
                    "https://py-fast-frontend-railway-j6a5a3vgz.vercel.app"
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