# navgurukul
# EduConnect — Live Video Classroom Platform (MVP)

## 🎯 Objective
EduConnect provides a simple yet powerful video conferencing platform designed for **teachers and students** to conduct live online classes. Teachers can create classes, share unique join links, and students can join via those links for real-time video and audio interaction.

---

## 🧩 Features Overview

### 1. User Authentication
- Secure registration and login system (JWT-based)
- Profile management (name, email)
- Password hashing for data safety

### 2. Live Class Management
- Teachers can create new live classes with title and description
- Automatic unique class link generation (shareable)
- Class dashboard for managing active and past sessions

### 3. Join via Link
- Public or authenticated access modes
- Waiting room/lobby before joining

### 4. Live Video Conferencing
- Real-time multi-user video and audio (powered by **Jitsi WebRTC**)
- Basic controls: mute/unmute, video on/off, leave class
- Host control: end session

### 5. Dashboard
- Active and past classes listed
- Quick access to start/join sessions

---

## 🏗️ Architecture Overview

**Frontend:** React + Jitsi SDK (for live video)  
**Backend:** FastAPI (Python)  
**Database:** PostgreSQL  
**Auth:** JWT Authentication  
**Deployment:** AWS EC2 (optional) + Docker Compose

### System Flow
```
[Frontend: React]  →  [Backend: FastAPI API + JWT Auth]  →  [Database: PostgreSQL]
                                   ↓
                             [Jitsi Video Server]
```

### Technology Choices
- **FastAPI** — lightweight, fast backend framework with async support
- **PostgreSQL** — reliable relational database for class/user storage
- **Jitsi Meet SDK** — handles real-time audio/video conferencing
- **React** — for responsive and interactive frontend
- **Docker** — for environment consistency and simplified deployment

---

## ⚙️ Installation & Setup

### Prerequisites
Ensure you have installed:
- Python ≥ 3.10
- Node.js ≥ 18
- PostgreSQL
- Docker & Docker Compose (for optional containerization)

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/educonnect.git
cd educonnect
```

### Step 2: Backend Setup
```bash
cd backend
cp .env.example .env
pip install -r requirements.txt
uvicorn main:app --reload
```

### Step 3: Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Step 4: Access
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

---

## 📡 API Documentation

### Auth Routes
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Authenticate and return JWT token |

### Class Routes
| Method | Endpoint | Description |
|--------|-----------|-------------|
| POST | `/classes/create` | Create a new class |
| GET | `/classes` | Get all classes for logged-in user |
| GET | `/classes/{id}` | Get specific class details |
| GET | `/classes/join/{class_code}` | Join a live class via unique code |

### Example Request: Create Class
```json
{
  "title": "Physics Lecture 1",
  "description": "Introduction to Mechanics"
}
```

### Example Response
```json
{
  "class_id": 1,
  "link": "https://educonnect.live/class/ABCD1234",
  "message": "Class created successfully"
}
```

---

## 🧮 Database Schema Design

### Tables

#### Users
| Column | Type | Description |
|---------|------|-------------|
| id | Integer (PK) | Unique user ID |
| name | String | User full name |
| email | String | Unique email ID |
| password | String | Hashed password |
| created_at | Timestamp | Registration date |

#### Classes
| Column | Type | Description |
|---------|------|-------------|
| id | Integer (PK) | Unique class ID |
| title | String | Class name/title |
| description | String | Class details |
| link | String | Unique class link |
| created_by | ForeignKey(User.id) | Host teacher |
| created_at | Timestamp | Creation date |

#### Participants
| Column | Type | Description |
|---------|------|-------------|
| id | Integer (PK) | Participant record ID |
| user_id | ForeignKey(User.id) | Participant reference |
| class_id | ForeignKey(Class.id) | Joined class reference |
| joined_at | Timestamp | Join timestamp |

---

## 🚧 Known Limitations
- No real-time chat (planned for future update)
- No screen sharing (optional integration with Jitsi API)
- Basic UI, minimal styling for MVP phase

---

## 🔮 Future Improvements
- Add chat, whiteboard, and hand-raise features
- Enable class recording & playback
- Introduce attendance and analytics
- Integrate with Google Classroom/Calendar
- Enhance mobile responsiveness and PWA support

---

## 📘 License
MIT License © 2025 EduConnect Team

---

**Developed with ❤️ using FastAPI, React, and Jitsi**
