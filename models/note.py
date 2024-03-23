from pydantic import BaseModel, field_validator


class Note(BaseModel):
    title: str
    description: str
    important: bool

    @field_validator('important')
    @classmethod
    def parse_bool(cls, v):
        return v.lower() in ('true', '1', 'on', 'yes') if isinstance(v, str) else False
