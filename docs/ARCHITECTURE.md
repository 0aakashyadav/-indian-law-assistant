# Architecture

## Current foundation

- FastAPI serves the mobile-first HTML interface and JSON API from one service.
- `GET /api/v1/health` reports process health only.
- `POST /api/v1/chat` validates a question and returns a clear no-evidence response. It does not pretend that a verified legal index exists.
- The interface supports English and Hindi fallback messages.

## Planned shared services

1. Source registry with approved official URLs and retrieval policy.
2. Document ingestion, parsing, content hashing, duplicate detection, versioning, and verification queue.
3. Durable database repositories and full-text retrieval with provenance.
4. Grounded answer generation behind an optional model interface.
5. Telegram worker calling the same legal-question service.

## Deployment notes

The Render blueprint is an initial web-service definition, not proof of deployment. Do not store durable legal data on an ephemeral filesystem. Configure exact CORS origins and production secrets before public release. A local language model is not part of this web container.
