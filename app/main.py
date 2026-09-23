from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.routers.chat import router as chat_router
from app.middleware import log_requests
from app.routers.auth import router as auth_router

app = FastAPI()

@app.middleware("http")
async def logging_middleware(request, call_next):
    return await log_requests(request, call_next)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Chatbot API "
    }
app.include_router(chat_router)
app.include_router(auth_router)
@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    print(f"Unexpected error: {exc}")

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error"
        }
    )