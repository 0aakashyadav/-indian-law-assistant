# Security

- Secrets are environment-only; `.env` is ignored by Git.
- CORS uses an explicit allowlist and credentials are disabled.
- Legal question length is capped at 2,000 characters and Pydantic validates language values.
- The current endpoint does not persist user questions or call external AI providers.
- User-facing errors do not include stack traces.

## Not yet implemented

Rate limiting, admin authentication, persistent audit events, a production database, dependency vulnerability scanning, full security headers, and ingestion isolation must be implemented before a production launch. Do not expose an admin interface until authentication and authorization are tested.
