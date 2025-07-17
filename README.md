# 🚀 PyFast Backend - AI Challenge API

FastAPI ile geliştirilmiş, AI destekli kodlama soruları oluşturan modern REST API.

![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green) ![Python](https://img.shields.io/badge/Python-3.11-blue) ![Groq](https://img.shields.io/badge/AI-Groq-purple) ![SQLite](https://img.shields.io/badge/DB-SQLite-orange)

## ✨ Özellikler

- 🤖 **AI Integration**: Groq API ile gerçek zamanlı soru üretimi
- 🔐 **Secure Auth**: Clerk JWT authentication
- 📊 **Quota System**: Kullanıcı bazlı günlük limit
- 🗄️ **Database**: SQLAlchemy + SQLite
- ⚡ **Fast API**: Async/await ile yüksek performans
- 🔄 **Auto-reset**: 24 saatlik quota reset
- 📱 **CORS Ready**: Frontend entegrasyonu
- 🎯 **RESTful**: Modern API design
- 🪝 **Webhooks**: Clerk user management

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.104.1
- **Database**: SQLite + SQLAlchemy 2.0
- **AI Model**: Groq (Llama 3.3 70B)
- **Authentication**: Clerk JWT
- **Server**: Uvicorn
- **Language**: Python 3.11

## 🚀 Canlı API

🌐 **Base URL**: `https://yfast-backend.up.railway.app`


## 🏁 Hızlı Başlangıç

### Gereksinimler
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
- Python 3.11+
- pip

### Kurulum

```bash
# Repository'i klonlayın
git clone https://github.com/bulutbilisimbusiness/pyfast-backend.git
cd pyfast-backend

# Virtual environment oluşturun
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Dependencies yükleyin
pip install -r requirements.txt

# Environment variables ayarlayın
cp .env.example .env
# .env dosyasını düzenleyin

# Database oluşturun
python -c "from src.database.models import create_tables; create_tables()"

# Development server başlatın
uvicorn src.app:app --reload
```

### Environment Variables

```env
CLERK_SECRET_KEY=sk_test_your_clerk_secret_key
OPENAI_API_KEY=gsk_your_groq_api_key
CLERK_WEBHOOK_SECRET=whsec_your_webhook_secret
JWT_KEY="-----BEGIN PUBLIC KEY-----\n...\n-----END PUBLIC KEY-----"
```

## 📁 Proje Yapısı

### 🗂️ Ana Klasörler
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
- `src/` - Ana uygulama kodu
- `src/database/` - Database modelleri ve işlemleri
- `src/routes/` - API endpoint'leri
- `src/utils.py` - Yardımcı fonksiyonlar

### 🔧 Core Files
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
- `src/app.py` - FastAPI ana uygulaması
- `src/ai_generator.py` - AI soru üretimi
- `requirements.txt` - Python dependencies
- `Procfile` - Deployment konfigürasyonu

### 🗄️ Database
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
- `database.db` - SQLite veritabanı
- `models.py` - SQLAlchemy modelleri
- `db.py` - Database işlemleri

## 🔌 API Endpoints

### 🧩 Challenge Management

```http
POST /api/generate-challenge
Content-Type: application/json
Authorization: Bearer <clerk_jwt_token>

{
  "difficulty": "easy"  // easy | medium | hard
}
```

**Response:**
<<<<<<< HEAD

```json
{
	"id": 1,
	"difficulty": "easy",
	"title": "Basic Python List Operation",
	"options": ["option1", "option2", "option3", "option4"],
	"correct_answer_id": 0,
	"explanation": "Detailed explanation...",
	"timestamp": "2025-01-16T10:30:00",
	"is_fallback": false,
	"quota_consumed": true
=======
```json
{
  "id": 1,
  "difficulty": "easy",
  "title": "Basic Python List Operation",
  "options": ["option1", "option2", "option3", "option4"],
  "correct_answer_id": 0,
  "explanation": "Detailed explanation...",
  "timestamp": "2025-01-16T10:30:00",
  "is_fallback": false,
  "quota_consumed": true
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
}
```

### 📊 Quota Management

```http
GET /api/quota
Authorization: Bearer <clerk_jwt_token>
```

**Response:**
<<<<<<< HEAD

```json
{
	"user_id": "user_123",
	"quota_remaining": 45,
	"last_reset_date": "2025-01-16T00:00:00"
=======
```json
{
  "user_id": "user_123",
  "quota_remaining": 45,
  "last_reset_date": "2025-01-16T00:00:00"
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
}
```

### 📚 Challenge History

```http
GET /api/challenges
Authorization: Bearer <clerk_jwt_token>
```

**Response:**
<<<<<<< HEAD

```json
[
	{
		"id": 1,
		"difficulty": "easy",
		"title": "Python List Operations",
		"date_created": "2025-01-16T10:30:00"
	}
=======
```json
[
  {
    "id": 1,
    "difficulty": "easy",
    "title": "Python List Operations",
    "date_created": "2025-01-16T10:30:00"
  }
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
]
```

### 🪝 Webhooks

```http
POST /webhooks/clerk
Content-Type: application/json
svix-id: <webhook_id>
svix-timestamp: <timestamp>
svix-signature: <signature>

{
  "type": "user.created",
  "data": {
    "id": "user_123"
  }
}
```

## 🤖 AI Integration

### Groq API Kullanımı

```python
from openai import OpenAI

client = OpenAI(
    api_key="gsk_your_groq_key",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Generate a {difficulty} coding challenge"}
    ],
    response_format={"type": "json_object"}
)
```

### Fallback System
<<<<<<< HEAD

AI başarısız olduğunda otomatik örnek soru sistemi:

=======
AI başarısız olduğunda otomatik örnek soru sistemi:
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```python
{
  "title": "Basic Python List Operation",
  "options": ["correct_answer", "wrong1", "wrong2", "wrong3"],
  "correct_answer_id": 0,
  "explanation": "Explanation text",
  "is_fallback": True  # Quota tüketilmez
}
```

## 🔐 Authentication Flow

### 1. Clerk JWT Verification
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```python
from src.utils import authenticate_and_get_user_details

user_details = authenticate_and_get_user_details(request)
user_id = user_details.get("user_id")
```

### 2. User Creation (Webhook)
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```python
# Yeni kullanıcı için otomatik quota oluşturma
create_challenge_quota(db, user_id)  # 50 challenge
```

### 3. Quota Check
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```python
quota = get_challenge_quota(db, user_id)
if quota.quota_remaining <= 0:
    raise HTTPException(status_code=429, detail="Quota exhausted")
```

## 🗄️ Database Schema

### ChallengeQuota Model
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```sql
CREATE TABLE challenge_quotas (
    id INTEGER PRIMARY KEY,
    user_id VARCHAR NOT NULL UNIQUE,
    quota_remaining INTEGER DEFAULT 50,
    last_reset_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Challenge Model
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```sql
CREATE TABLE challenges (
    id INTEGER PRIMARY KEY,
    difficulty VARCHAR NOT NULL,
    date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR NOT NULL,
    title VARCHAR NOT NULL,
    options TEXT NOT NULL,  -- JSON array
    correct_answer_id INTEGER NOT NULL,
    explanation TEXT NOT NULL
);
```

## 🌐 Deployment
<<<<<<< HEAD

### Railway

#### 1. Railway Setup

=======
### Railway 

#### 1. Railway Setup
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```bash
# Railway'e kayıt ol
# https://railway.app - GitHub ile sign up

# Repository'i push et
git add .
git commit -m "Add Railway deployment config"
git push origin main
```

#### 2. Railway'de Deploy
<<<<<<< HEAD

```bash
# 1. https://railway.app dashboard
# 2. "New Project"
=======
```bash
# 1. https://railway.app dashboard
# 2. "New Project" 
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
# 3. "Deploy from GitHub repo"
# 4. Repository seç
# 5. Root directory: backend/ (otomatik algılanır)
```

<<<<<<< HEAD
## 🧪 Testing

### Unit Tests

=======


## 🧪 Testing

### Unit Tests
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```bash
# Test framework
pip install pytest pytest-asyncio

# Tests çalıştır
pytest tests/
```

### Manual API Testing
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```bash
# Health check
curl https://pyfast-backend.up.railway.app/api/health

# Test challenge generation
curl -X POST https://your-api-url.com/api/generate-challenge \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"difficulty": "easy"}'
```

## 📊 Monitoring

### Logs
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```bash
# Development
uvicorn src.app:app --reload --log-level debug
```

### Health Check
<<<<<<< HEAD

=======
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
```http
GET /api/health
```

Response:
<<<<<<< HEAD

```json
{
	"status": "healthy",
	"message": "PyFast API is running"
=======
```json
{
  "status": "healthy",
  "message": "PyFast API is running"
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
}
```

## 🔧 Available Scripts

```bash
# Development server
uvicorn src.app:app --reload

# Production server
uvicorn src.app:app --host 0.0.0.0 --port 8000

# Database migrations
python -c "from src.database.models import create_tables; create_tables()"

# Requirements update
pip freeze > requirements.txt
```

## 👨‍💻 Geliştirici

**Erhan** - [@username](https://github.com/bulutbilisimbusiness)

<<<<<<< HEAD
_PyFast Backend - AI-powered coding challenges! 🚀_
=======



*PyFast Backend - AI-powered coding challenges! 🚀*
>>>>>>> 57825c7c30021a0ccf5bbb9e8f0dbae3a2552766
