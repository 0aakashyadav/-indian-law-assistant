# Mobile-only setup

You do not need a laptop to maintain this repository. GitHub Actions runs tests in GitHub-hosted runners. Files can be reviewed through GitHub's mobile web interface or edited in GitHub Codespaces when available.

## Review automated tests

1. Open the repository on GitHub.
2. Tap Actions and select the latest Tests workflow.
3. Open the `test` job and read the test output.
4. A green check means that specific workflow run passed; it does not prove a live deployment.

## Deployment

Use the Render dashboard to create a new Blueprint from the repository and select `render.yaml`. Confirm the service name and settings before applying. After creation, check deployment logs and open `/api/v1/health` on the assigned Render URL. Free-tier availability, quotas, sleep, and persistence can change; never use ephemeral disk for durable legal data.

Never paste Telegram tokens, database passwords, or other secrets into chat, commits, issues, or screenshots. Enter them only in the provider's secret/environment settings.
