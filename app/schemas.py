from pydantic import BaseModel

# Created for validation of input data
class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    title: str
    content: str
