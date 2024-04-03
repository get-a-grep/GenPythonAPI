from doctest import Example
from unicodedata import name
from pydantic import BaseModel, Field

class BasicPost(BaseModel):

    type: str = Field(description="Name of the object", example="question")
    value: str = Field(description="Value of the object", example="How are you today?")
