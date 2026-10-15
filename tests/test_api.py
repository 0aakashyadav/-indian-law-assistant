from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat_does_not_invent_legal_answer_without_sources() -> None:
    response = client.post('/api/v1/chat', json={'question': 'What is the law?', 'language': 'en'})
    assert response.status_code == 200
    body = response.json()
    assert body['status'] == 'sources_unavailable'
    assert body['sources'] == []
    assert 'cannot responsibly confirm' in body['answer']

def test_chat_supports_hindi_fallback() -> None:
    response = client.post('/api/v1/chat', json={'question': 'कानून क्या है?', 'language': 'hi'})
    assert response.status_code == 200
    assert 'सत्यापित दस्तावेज़' in response.json()['answer']

def test_chat_rejects_too_short_question() -> None:
    response = client.post('/api/v1/chat', json={'question': 'a', 'language': 'en'})
    assert response.status_code == 422

def test_chat_rejects_oversized_question() -> None:
    response = client.post('/api/v1/chat', json={'question': 'x' * 2001, 'language': 'en'})
    assert response.status_code == 422
