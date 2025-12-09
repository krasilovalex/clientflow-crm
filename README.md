````md
# ClientFlow CRM

A lightweight CRM system for client and deal management.  
This project is being developed as a **production-ready backend service** with a strong focus on:

- security,
- clean architecture,
- scalability,
- real-world business use cases.

Perfect for:
- internship portfolios (banks, IT companies),
- freelance & Kwork projects,
- startup MVPs and internal business tools.

---

## 🚀 Project Status

✅ Implemented:

- FastAPI project architecture
- Configuration via `.env` (no secrets in GitHub)
- Health-check endpoint (`/health`)
- Database layer (SQLAlchemy engine & session)
- Base ORM model `User`
- Pydantic schemas for users
- Secure password hashing (bcrypt)
- User CRUD logic

⏳ In Progress / Planned:

- Alembic database migrations
- JWT authentication
- Clients (Client)
- Deals (Deal)
- Notes (Note)
- Analytics & statistics
- Docker & PostgreSQL (after environment stabilization)

---

## 🧱 Project Architecture

```text
clientflow-crm/
 ├─ app/
 │   ├─ core/          # configuration & security
 │   ├─ db/            # database engine & session
 │   ├─ models/        # ORM models (User, Client, Deal...)
 │   ├─ schemas/       # Pydantic schemas
 │   ├─ crud/          # business logic & DB operations
 │   ├─ api/           # FastAPI routers
 │   └─ main.py        # application entry point
 ├─ tests/
 ├─ .env.example
 ├─ .gitignore
 ├─ requirements.txt
 └─ README.md
````

The architecture follows:

* separation of concerns,
* secure data access,
* scalable structure,
* production-ready patterns.

---

## 🔐 Security

* All secrets are stored **only in `.env`**
* `.env` is excluded from version control via `.gitignore`
* Passwords are stored **only as bcrypt hashes**
* JWT-based authentication will be used
* Role system (`user`, `admin`) is planned

---

## 🛠 Tech Stack

* **Python 3.12**
* **FastAPI**
* **SQLAlchemy**
* **Alembic** (in progress)
* **Pydantic**
* **Passlib (bcrypt)**
* **PostgreSQL** (planned)
* **Docker** (planned)

---

## ⚙️ Local Development

The project currently runs in local mode (without Docker):

```bash
python -m uvicorn app.main:app --reload
```

Health check:

```
GET /health
```

Expected response:

```json
{"status":"ok","env":"dev"}
```

---

## 👤 Users (User)

Implemented features:

* User ORM model
* API schemas
* Secure password hashing
* CRUD operations:

  * get by id
  * get by email
  * create user

---

## 🧭 Roadmap

* [x] Base project architecture
* [x] SQLAlchemy integration
* [x] User ORM model
* [x] Password security layer
* [x] User CRUD logic
* [ ] Alembic migrations
* [ ] JWT authentication
* [ ] Clients (Client)
* [ ] Deals (Deal)
* [ ] Notes (Note)
* [ ] Analytics & statistics
* [ ] Docker & PostgreSQL
* [ ] Deployment

---

## 💼 Commercial Use

This project can be used as a base for:

* agency CRMs
* client & order tracking systems
* internal business tools
* admin dashboards
* corporate backend services

It is designed as a **universal business-ready backend template**.

---

## 📌 Author

Developer: **Alexandr**
Specialization:

* Backend Development (FastAPI, Python)
* Telegram Mini Apps
* AI integrations
* Parsers & automation

---

If you find this project useful — feel free to ⭐ star it.

```
