from app.memory import add_to_history,get_history,create_conversation,conversation_exists
from fastapi import APIRouter,HTTPException,Depends
from app.schemas import ChatRequest,ChatResponse
from app.services.openrouter import generate_response
from app.dependencies import get_current_user
from fastapi.responses import StreamingResponse
from app.services.openrouter import generate_stream
router=APIRouter()
@router.post("/chat", response_model=ChatResponse)
def chat(request:ChatRequest, user_id: int = Depends(get_current_user)):
    if request.conversation_id is None:
        conversation_id=create_conversation(user_id)
    else:
        conversation_id=request.conversation_id
        if not conversation_belongs_to_user(conversation_id, user_id):
            raise HTTPException(status_code=404, detail="Conversation not found")
    add_to_history(conversation_id, "user", request.message)
    history=get_history(conversation_id)
    answer=generate_response(history)
    add_to_history(conversation_id, "assistant", answer)
    return ChatResponse(response=answer, conversation_id=conversation_id)

@router.post("/chat/stream")
def chat_stream(
    request: ChatRequest,
    user_id: int = Depends(get_current_user)
):
    if request.conversation_id is None:
        conversation_id = create_conversation(user_id)
    else:
        conversation_id = request.conversation_id
        if not conversation_belongs_to_user(
            conversation_id,
            user_id
        ):
            raise HTTPException(
                status_code=404,
                detail="Conversation not found"
            )
    add_to_history(
        conversation_id,
        "user",
        request.message
    )
    history = get_history(conversation_id)
    def generate():
        full_response = ""
        for chunk in generate_stream(history):
            full_response += chunk
            yield chunk
        add_to_history(
            conversation_id,
            "assistant",
            full_response
        )
    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )