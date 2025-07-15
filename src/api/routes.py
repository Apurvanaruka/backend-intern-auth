

from fastapi import APIRouter, Depends
from utils import get_current_user



router = APIRouter()


@router.get("/api/posts")
def read_posts(current_user: dict = Depends(get_current_user)):
    return [
        {"post_id": 1, "title": "Post One", "contentSnippet": "First post..."},
        {"post_id": 2, "title": "Post Two", "contentSnippet": "Second post..."}
    ]
