# 📚 Assignment 1: API Integration & Google Authentication

This project demonstrates secure backend development using **FastAPI** for **LawVriksh**.
It includes:

* Project setup from scratch
* JWT-based user authentication
* Google OAuth 2.0 (Sign in with Google)
* Protected sample data API (`/api/posts`)
* Postman demonstration with all request/response flows

---

## 🚀 Tech Stack

* **Backend**: FastAPI (Python)
* **Authentication**: Google OAuth 2.0 & JWT
* **Database**: PostgreSQL
* **API Testing**: Postman

---

## ✅ Features

* **Secure Project Setup**: Linting & clean structure
* **Google Sign-In**: OAuth 2.0 integration with the Google Identity Platform
* **JWT Auth**: Secure endpoints with access tokens
* **Sample API**: `/api/posts` returns a JSON list of posts
* **Postman Collection**: Included for demonstrating OAuth and API flows

---

## 🗂️ How It Works

```mermaid
flowchart TD
    A[Client (Browser/Postman)] -->|Request Login| B[FastAPI /login/google]
    B -->|Redirect OAuth Consent| C[Google Identity Platform]
    C -->|User Grants Permission| D[Google Callback: /auth/google/callback]
    D -->|FastAPI Verifies Token| E[JWT Created]
    E -->|Send JWT to Client| A

    A -->|GET /api/posts + JWT| F[FastAPI /api/posts]
    F -->|Valid JWT?| G{Check JWT}
    G -- Yes --> H[Return Posts JSON]
    G -- No --> I[401 Unauthorized]
```

---

## 🔗 GitHub Repository

👉 [Apurva Singh’s Repo](https://github.com/Apurvanaruka/backend-intern-auth.git)

---

## ⚙️ Project Setup

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/Apurvanaruka/backend-intern-auth.git
cd backend-intern-auth
```

---

### 2️⃣ Create Virtual Environment

**On Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows (CMD):**

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 .env Configuration

Create a `.env` file in your project root with **your actual secrets**:

```env
GOOGLE_CLIENT_ID=YOUR_GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET=YOUR_GOOGLE_CLIENT_SECRET
SECRET_KEY=YOUR_SECRET_KEY
DATABASE_URL=postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@localhost:5432/YOUR_DB_NAME
CORS_ORIGINS=*
```

✅ **Example:**

* Replace `YOUR_GOOGLE_CLIENT_ID` with your OAuth Client ID
* Replace `YOUR_GOOGLE_CLIENT_SECRET` with your Client Secret
* Replace `YOUR_SECRET_KEY` with a strong random key
* Update your `DATABASE_URL` to match your PostgreSQL credentials

---

## 🔐 Google OAuth Configuration

1. Create OAuth credentials in [Google Cloud Console](https://console.cloud.google.com/).
2. Add `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in your `.env`.
3. Add your redirect URI: `http://localhost:8000/auth/google/callback`.

---

## 🗃️ API Endpoints

| Method | Endpoint                | Description                              |
| ------ | ----------------------- | ---------------------------------------- |
| `GET`  | `/login/google`         | Redirects to Google OAuth consent screen |
| `GET`  | `/auth/google/callback` | Google OAuth callback, generates JWT     |
| `GET`  | `/api/posts`            | Returns list of posts (JWT required)     |

---

## 📬 Postman Collection

A `Postman_Collection.json` is included:

* Test **Google OAuth flow**
* Call `/api/posts` with and without JWT
* Observe `200 OK` vs. `401 Unauthorized`

---

## ✨ Author

**Apurva Singh**
👉 [Gmail](mainto:apurvanaruka1@gmail.com)

---
