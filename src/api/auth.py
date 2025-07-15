from fastapi import APIRouter, Request
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from utils import create_access_token
import os
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
load_dotenv()


router = APIRouter()
config = Config(".env")

oauth = OAuth(config)
oauth.register(
    name='google',
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://oauth2.googleapis.com/token',
    api_base_url='https://www.googleapis.com/oauth2/v2/',
    client_kwargs={'scope': 'email profile'},
    jwks_uri = "https://www.googleapis.com/oauth2/v3/certs"
)

@router.get("/auth/google")
async def auth_google(request: Request):
    redirect_uri = request.url_for('auth_google_callback')
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/auth/google/callback")
async def auth_google_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    resp = await oauth.google.get("userinfo", token=token)
    user_info = resp.json()

    email = user_info["email"]
    name = user_info.get("name", email.split("@")[0])

    jwt_token = create_access_token({
        "email": email,
        "name": name
    })

    return JSONResponse(content={
        "message": "Login successful",
        "token": jwt_token,
        "user": {
            "email": email,
            "name": name
        }
    })
