from fastapi import Request
async def log_requests(request: Request, call_next):
    print(f"Incoming Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response Status: {response.status_code}")
    return response