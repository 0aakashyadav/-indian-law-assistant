"""Evidence-first legal question endpoint."""
from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/chat", tags=["legal questions"])

class ChatRequest(BaseModel):
    question: str = Field(min_length=3, max_length=2000)
    language: Literal["en", "hi"] = "en"

class Source(BaseModel):
    title: str
    url: str
    authority: str
    status: str

class ChatResponse(BaseModel):
    status: Literal["sources_unavailable"]
    answer: str
    sources: list[Source]
    disclaimer: str

@router.post("", response_model=ChatResponse)
def ask_question(request: ChatRequest) -> ChatResponse:
    """Never invent legal answers when the verified document index is empty."""
    answer = (
        "The current legal-source index does not yet contain verified documents for this question. "
        "I cannot responsibly confirm the applicable law from the available evidence. Please consult India Code or a qualified lawyer."
        if request.language == "en" else
        "वर्तमान कानूनी स्रोत सूची में इस प्रश्न के लिए सत्यापित दस्तावेज़ उपलब्ध नहीं हैं। "
        उपलब्ध प्रमाणों के आधार पर मैं लागू कानून की पुष्टि नहीं कर सकता/सकती। कृपया India Code या किसी योग्य वकील से परामर्श करें।"
    )
    return ChatResponse(status="sources_unavailable", answer=answer, sources=[], disclaimer="General legal information only; not legal advice.")
