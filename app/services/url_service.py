from app.utils.shortener import generate_short_code
from app.repositories.url_repository import (save,get,exists,)

def create_short_url(original_url:str):
    short_code=generate_short_code()
    while exists(short_code):
        short_code=generate_short_code()
    save(short_code,original_url)
    return{
        "original_url":original_url,
        "short_code":short_code,
        "short_url":f"http://localhost:8000/{short_code}"
    }

def get_original_url(short_code:str):
    url=get(short_code)
    if url is None:
        return None
    return url.original_url#because over here the url will be a URL object defined by the URL model

