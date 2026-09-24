# Senior Design Team 02 - Cooking Core

This is the core backend API for all of the functions of the cooking assistant.

## Setup

Install `uv` package manager: https://docs.astral.sh/uv/getting-started/installation/

```sh
uv sync
```

## Run

Development: auto-reloads:

```sh
uv run fastapi dev
```

Release: doesn't auto-reload, reachable from other devices on the network:

```sh
uv run fastapi run
```
