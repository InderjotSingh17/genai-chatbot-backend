from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database import get_connection
from app.auth import (
    hash_password,
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str


class RegisterResponse(BaseModel):
    message: str
    user_id: int


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


@router.post("/register", response_model=RegisterResponse)
def register(request: RegisterRequest):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM users
        WHERE username = %s OR email = %s
        """,
        (request.username, request.email)
    )

    existing_user = cur.fetchone()

    if existing_user:
        cur.close()
        conn.close()

        raise HTTPException(
            status_code=400,
            detail="Username or email already exists"
        )

    password_hash = hash_password(request.password)

    cur.execute(
        """
        INSERT INTO users
        (username, email, password_hash)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (
            request.username,
            request.email,
            password_hash
        )
    )

    user_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return RegisterResponse(
        message="User registered successfully",
        user_id=user_id
    )


@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, password_hash
        FROM users
        WHERE email = %s
        """,
        (request.email,)
    )

    user = cur.fetchone()

    cur.close()
    conn.close()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    user_id = user[0]
    password_hash = user[1]

    if not verify_password(
        request.password,
        password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(user_id)

    return LoginResponse(
        access_token=access_token,
        token_type="bearer"
    )