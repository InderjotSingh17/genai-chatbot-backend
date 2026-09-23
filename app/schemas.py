from pydantic import BaseModel
class ChatRequest(BaseModel):
    message:str
    conversation_id:int | None = None
class ChatResponse(BaseModel):
    response:str
    conversation_id:int
class LoginRequest(BaseModel):
    email:str
    password:str
class LoginResponse(BaseModel):
    acess_token:str
    token_type:str