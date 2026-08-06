from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from app.schemas import URLRequest
from app.utils.shortener import generate_short_code

app=FastAPI()
url_db={}

@app.get("/")
def root():
    print(len(url_db))
    for u in url_db:
        print(u)
        print(url_db[u])
    return {
        "message":"Welcome to the URL shortener API"
    }

@app.post("/shorten",status_code=201)#If this function completes successfully, send HTTP 201.
def shorten_url(request: URLRequest):# the working of this is like when a request is sent the function looks at the pydantic model present as an argument and then it sends the body of the request to the pydantic model specified which is validated and if the validation is a success only then the function is executed 
    short_code=generate_short_code()
    url_db[short_code]=str(request.url)# converting it to str because request.url is of the type of HttpUrl
    return{
        "original_url": str(request.url),
        "short_url":f"http://localhost:8000/{short_code}"
    }

@app.get("/{short_code}")# whatever that comes after the / is stored as short_code
def redirect_to_original(short_code: str):
    original_url = url_db.get(short_code)
    if original_url is None:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )
    print(original_url)
    return RedirectResponse(#fastapi tells the browser to automatically redirect to the original url
        url=original_url,
        status_code=307
    )
