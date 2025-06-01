# Image Moderation API

A secure, containerized REST API for automated image moderation, built with **FastAPI**, **MongoDB**, and a minimal **HTML/JS frontend**. This project enables detection and blocking of harmful, illegal, or unwanted imagery (e.g., violence, hate symbols, nudity, self-harm, propaganda).

---

## 🚀 Features

- **REST API** with FastAPI
- **Bearer token authentication** (admin and user roles)
- **MongoDB** for token management and usage tracking
- **Dockerized** backend, frontend, and database
- **Minimal frontend** for easy testing and demonstration
- **Usage logging** for every API request
- **Best practices**: modular code, Pydantic validation, .env config, and CI-ready

---

## 🗂️ Project Structure

```
image-moderation-api/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entrypoint
│   │   ├── models.py        # MongoDB data models
│   │   ├── database.py      # Database connection
│   │   ├── auth.py          # Token management/auth
│   │   ├── moderate.py      # Image moderation logic
│   │   ├── schemas.py       # Pydantic schemas
│   │   └── utils.py         # Utility functions
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Backend Dockerfile
├── frontend/
│   ├── index.html           # Minimal HTML/JS UI
│   └── Dockerfile           # Frontend Dockerfile (NGINX)
├── docker-compose.yml       # Compose config for all services
├── backend/.env.example     # Example environment variables
├── .gitignore
└── README.md
```

---

## ⚡ Getting Started

### 1. Clone the Repository

```sh
git clone <repository-url>
cd image-moderation-api
```

### 2. Configure Environment Variables

```sh
cp backend/.env.example backend/.env
# Edit backend/.env with your MongoDB URI and other settings
```

### 3. Build and Start All Services

```sh
docker-compose up --build
```

- **Backend:** [http://localhost:7000](http://localhost:7000)
- **Frontend:** [http://localhost:8080](http://localhost:8080)
- **MongoDB:** Exposed on port 27017 (for development)

### 4. API Documentation

Visit [http://localhost:7000/docs](http://localhost:7000/docs) for interactive Swagger UI.

---

## 🛠️ API Endpoints

### Authentication (Admin Only)

| Method | Endpoint              | Description              |
|--------|----------------------|--------------------------|
| POST   | `/auth/tokens`       | Create a new bearer token|
| GET    | `/auth/tokens`       | List all tokens          |
| DELETE | `/auth/tokens/{token}` | Delete a specific token |

> **Note:** Requires a token with `isAdmin: true` in the `Authorization: Bearer <token>` header.

### Image Moderation

| Method | Endpoint     | Description                  |
|--------|-------------|------------------------------|
| POST   | `/moderate` | Upload image for moderation  |

> **Note:** Requires any valid bearer token.

---

## 🖥️ Frontend Usage

1. Open [http://localhost:8080](http://localhost:8080)
2. Paste a valid token into the input field.
3. Upload an image file.
4. Submit and view the moderation report (categories + confidence scores).

---

## 🗄️ MongoDB Collections

- **tokens:**  
  Stores bearer tokens  
  Fields: `token` (str), `isAdmin` (bool), `createdAt` (datetime)

- **usages:**  
  Logs each API request  
  Fields: `token` (str), `endpoint` (str), `timestamp` (datetime)

---

## 🔒 Authentication & Usage Tracking

- All API endpoints require a Bearer token:
  ```
  Authorization: Bearer <your_token>
  ```
- Admin endpoints (`/auth/*`) require tokens with `isAdmin: true`.
- Every request is logged in the `usages` collection for auditing.

---

## 🧑‍💻 Local Development (Without Docker)

```sh
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 7000
# Visit http://localhost:7000/docs
```
Frontend can be opened by simply launching `frontend/index.html` in your browser.

---

## ✅ Best Practices

- Modular codebase with clear separation of concerns
- Pydantic schemas for validation
- Environment-based configuration
- Usage logging and clean error handling
- Ready for CI/CD and deployment

---

## 📝 License

MIT License

---

## 🙋 Need Help?

Open an issue or discussion on this repository!


