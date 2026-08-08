from fastapi import APIRouter,HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import URLRequest
from  app.services.url_service import (
    create_short_url,
    get_original_url
)

router = APIRouter()


@router.post("/shorten",status_code=201)
def shorten_url(request: URLRequest):
    return create_short_url(str(request.url))

@router.get("/{short_code}")
def redirect(short_code:str):# :str is a python annotation and it tells the fastapi that the path parameter should be interpreted as a string 
    original_url=get_original_url(short_code)
    if original_url is None:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )
    return RedirectResponse(
        url=original_url,
        status_code=307
    )
