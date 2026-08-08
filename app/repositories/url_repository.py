url_db={}

def save(short_code: str,original_url: str):
    url_db[short_code]=original_url

def get(short_code: str):
    return url_db.get(short_code)

def exists(short_code: str):
    return short_code in url_db

    