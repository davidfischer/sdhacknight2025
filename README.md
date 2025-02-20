SD Hack Night 2025 Demo
===========================

This app detects American Sign Language (ASL) in uploaded images.
For this project, we are using the [EyePop.ai](https://eyepop.ai) API
to detect hands and fingers in uploaded images.
With more than ~2 hours, we would have more sophisticated detection and a custom model.

This was presented at SD Hack Night 2025.

Team: David Fischer & Jeremy Langley

## Developing

### Prerequisites

* [uv](https://docs.astral.sh) (see [uv installation](https://docs.astral.sh/uv/getting-started/installation/))
* Node v20
* An API key from [EyePop.ai](https://eyepop.ai)


### Getting started

Install Python 3.13 with uv:

```shell
uv python install
```

Build static assets:

```shell
npm run build                          # Build static assets
```

Test run app locally:

```shell
# Setup your local environment variables used with Docker
# This only needs to be run once
# Your EyePop API key needs to be put into `.env/local`.
cp .env/local.sample .env/local

# Build the docker image
# Use Docker compose to have Redis and PostgreSQL just like in production
# Note: Docker is used in production but Docker compose is just for development
make dockerbuild

# Start a development web server on http://localhost:8000
# Use ctrl+C to stop
make dockerserve

# While the server is running,
# you can start a bash shell to the container with the following:
# Once you have a bash shell, you can run migrations,
# manually connect to the local Postgres database or anything else
make dockershell
```



## Testing

Testing relies on uv's ["tools"](https://docs.astral.sh/uv/guides/tools/) concept.


```shell
# Installing tools only needs to run once ever
uv tool install pre-commit

# Install pre-commit so it runs before every commit
# This also only needs to run once
uvx pre-commit install

# Run pre-commit
uvx pre-commit run --all-files
```

### Debugging

Get a virtualenv shell with all dependencies (declared in `pyproject.toml`) installed:

```shell
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
.venv/bin/python
```
