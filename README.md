SD Hack Night 2025 Demo
===========================



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

Start the dev server:

```shell
npm run build                          # Build static assets

uv run ./manage.py migrate             # Create a local development database
uv run ./manage.py runserver           # Starts a local development server at http://localhost:8000
```

Also star



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


## Docker

To test the Dockerfile that is used for deployment,
you can build the container and run it locally:

```shell
# Setup your local environment variables used with Docker
# This only needs to be run once
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


## Deploying

This site is deployed to [Fly.io](https://fly.io/).
It is deployed automatically when code is merged to the `main` branch
via GitHub Actions.


To deploy manually, you will need to be a member of the San Diego Python team on Fly.
Once you're a member of the team, you can deploy with:

```shell
make deploy
```
