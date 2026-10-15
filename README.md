# Indian Law AI Assistant

A source-grounded Indian legal-information assistant for a public website and Telegram bot. Development is staged; legal coverage is not comprehensive, and documents are not treated as verified until collected, checked, and indexed.

## Current status

**Phase 1 foundation in progress.** The API has a health endpoint and initial automated tests. Legal retrieval, the website, Telegram integration, and a production database are not implemented yet.

## Requirements

- Python 3.11 or compatible supported version
- GitHub repository
- Optional: browser-based GitHub Codespaces

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/`, API docs at `/docs`, and health at `/api/v1/health`.

## Tests

```bash
pytest
```

## Legal safety

This project provides general legal information, not legal representation or individualized legal advice. Answers must cite retrieved source documents and state when evidence or current legal status cannot be verified. Do not describe the database as comprehensive without an audited source inventory.

## Secrets

Never commit `.env`, Telegram bot tokens, database passwords, API keys, or private keys. Configure production secrets in the hosting provider's environment settings.

## Planned architecture

The target includes a shared FastAPI backend, source registry and retrieval, responsive website, Telegram worker, automated tests, and deployment configuration. Features will be added and verified in stages.