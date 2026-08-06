from pydantic import BaseModel, HttpUrl

class URLRequest(BaseModel):#This class describes the shape of incoming data
    url: HttpUrl