from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from passlib.context import CryptContext
from app.config import JWT_SECRET_KEY
from fastapi import HTTPException
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)->bool:
    return pwd_context.verify(plain_password, hashed_password)
def create_access_token(user_id:int,expires_minutes:int=60)->str:
    expire=datetime.now(timezone.utc)+timedelta(minutes=expires_minutes)
    payload={"sub":str(user_id),"exp":expire}
    return jwt.encode(payload,JWT_SECRET_KEY,algorithm="HS256")

def get_user_id_from_token(token: str) -> int:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=["HS256"]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return int(user_id)

    except (JWTError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )