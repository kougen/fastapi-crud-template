# FastAPI CRUD Template

This is a template for FastAPI CRUD operations.

## Features

- FastAPI
- Repository Pattern (from [pyrepositories](https://pypi.org/project/pyrepositories/))
- Automatic docker image build and publish on release

## Requirements

- Python 3.8+

## Installation

```bash
pip install -r requirements.txt --upgrade
```

### Docker image

You will have to set up 2 secrets and 2 variables in your repository

Secrets:
- `DOCKER_PUSH`: A github classic token with packages `read` and `write` permissions
- `HUB_PASSWORD`: Docker Hub token.

Variables:
- `HUB_NS`: Docker hub target **N**ame**S**pace
- `HUB_REPO`: Docker hub target repository

## Usage

You will find a `lib.py` in the `app` directory. This is where you will define helper functions for your CRUD operations.

There is also a `models.py` in the `app` directory. This is where you will define your Pydantic models.

## Future plans
- Possibility to decide easily between `ghcr.io` and docker hub targers

