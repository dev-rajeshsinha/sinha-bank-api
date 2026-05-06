<div align="center">

# 🏦 Sinha Bank API

**The core REST API backend for Sinha Bank**

A modern, scalable virtual banking platform built with Python, FastAPI, and Docker.

[![Python](https://img.shields.io/badge/Python-3.12.3-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136.1-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-2.13.3-E92063?style=flat&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat)](https://opensource.org/licenses/MIT)

</div>

---

## 📖 Overview

**Sinha Bank API** is the backend REST API for the Sinha Bank virtual banking platform. It is built with [FastAPI](https://fastapi.tiangolo.com/) and follows modern Python development practices — environment-based configuration, containerized deployment, and auto-generated interactive API documentation.

---

## ✨ Features

- ⚡ **High performance** — Built on FastAPI and Uvicorn for async request handling
- 🔧 **Environment-based configuration** — All settings managed via `.env` using Pydantic Settings
- 📄 **Auto-generated API docs** — Interactive Swagger UI and ReDoc out of the box
- 🐳 **Dockerized** — Production-ready Docker image with a slim Python base
- 🔒 **Secure defaults** — No hardcoded secrets; `.env` excluded from Docker image

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Docker (optional, for containerized deployment)

### 1. Clone the repository

```bash
git clone https://github.com/dev-rajeshsinha/sinha-bank-api.git
cd sinha-bank-api
```

### 2. Set up environment variables

```bash
cp .env.example .env
# Edit .env and fill in your values
```

### 3. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the development server

```bash
uvicorn src.main:sinha_bank_api --reload
```

The API will be available at `http://localhost:8000`.

---

## 🐳 Docker

### Build the image

```bash
docker build -t sinha-bank-api .
```

### Run the container

```bash
docker run --env-file .env -p 8000:8000 sinha-bank-api
```

---

## 📡 API Endpoints

| Method | Path          | Description                                          |
| ------ | ------------- | ---------------------------------------------------- |
| `GET`  | `/api/health` | Health check — returns app name, version, and status |

### Interactive Documentation

| UI           | URL                                      |
| ------------ | ---------------------------------------- |
| Swagger UI   | `http://localhost:8000/api/docs`         |
| ReDoc        | `http://localhost:8000/api/redoc`        |
| OpenAPI JSON | `http://localhost:8000/api/openapi.json` |

---

## ⚙️ Environment Variables

Copy `.env.example` to `.env` and set the following values:

| Variable           | Description                          |
| ------------------ | ------------------------------------ |
| `PROJECT_TITLE`    | Display name of the API              |
| `PROJECT_VERSION`  | Current version of the API           |
| `PROJECT_URL`      | Project URL (e.g. GitHub repository) |
| `APPLICATION_NAME` | Internal application identifier      |
| `LICENSE_NAME`     | License name (e.g. MIT License)      |
| `LICENSE_URL`      | URL to the license text              |
| `CONTACT_NAME`     | Maintainer's name                    |
| `CONTACT_EMAIL`    | Maintainer's email address           |
| `DOCS_URL`         | Path for Swagger UI                  |
| `REDOC_URL`        | Path for ReDoc                       |
| `OPENAPI_URL`      | Path for OpenAPI JSON schema         |

---

## 🛠️ Tech Stack

| Layer         | Technology                  |
| ------------- | --------------------------- |
| Language      | Python 3.12.3               |
| Framework     | FastAPI 0.136.1             |
| Server        | Uvicorn 0.46.0              |
| Validation    | Pydantic 2.13.3             |
| Configuration | pydantic-settings 2.14.0    |
| Container     | Docker (python:3.12.3-slim) |

---

## 📄 License

This project is licensed under the **MIT License** — see [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT) for details.

---

## 👤 Contact

**Rajesh Sinha**

- GitHub: [@dev-rajeshsinha](https://github.com/dev-rajeshsinha)
- Email: rajeshsinha97@outlook.com
