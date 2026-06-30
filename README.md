# 🚀 Luminous BI  
### AI-Powered Conversational Analytics Platform

<div align="center">

**Transform raw business data into intelligent decisions using AI-powered analytics, interactive dashboards, and natural-language conversations.**

</div>

---

## 📌 Overview

**Luminous BI** is a full-stack conversational business intelligence platform that allows users to upload CSV datasets, ask questions in natural language, and receive automated analytics with:

- 📊 Interactive visualizations
- 🤖 AI-generated insights
- 📝 SQL-like query explanations
- 💡 Decision recommendations
- 🔮 What-if business simulations
- 📁 Saved dashboards
- 🕒 Query history

The platform bridges the gap between raw data and business decisions by combining modern web technologies with AI-assisted analytics.

---

# ✨ Features

## 📂 Intelligent Data Upload

- Upload CSV datasets securely
- Automatic schema detection
- Dataset preview and metadata extraction
- Persistent storage using Supabase Storage

---

## 💬 Conversational Analytics

Ask questions like:

> "Which product generated the highest revenue?"

> "Show monthly sales trends"

> "Which region has the lowest performance?"

The system converts business questions into structured analytics responses.

---

## 🤖 AI-Powered Analysis

Powered by:

- Google Gemini API
- Configurable LLM providers
- Intelligent fallback mechanisms

Generates:

✅ Business summaries  
✅ Key insights  
✅ Charts  
✅ SQL-style queries  
✅ Data explanations  

---

## 🧠 Decision Copilot

Transforms analytics into actionable strategies:

Example:

**Input:**
```
How can we improve sales performance?
```

**Output:**

```
1. Increase marketing spend in high-performing regions
   Expected Impact: +12-15% revenue growth
   Confidence: High

2. Optimize low-performing product categories
   Expected Impact: +8-10% improvement
   Confidence: Medium
```

---

## 🔮 What-If Simulation

Perform business scenario analysis using natural language.

Example:

```
Increase product price by 5%
```

Returns:

- Expected KPI changes
- Revenue impact range
- Simulation assumptions

---

## 📊 Dashboard Management

Users can:

- Save analytics results
- Create reusable dashboards
- View previous analysis
- Manage saved insights

---

# 🏗️ System Architecture

```
                 User
                  |
                  |
            React Frontend
                  |
                  |
             FastAPI Backend
                  |
     ----------------------------
     |            |             |
 PostgreSQL   Supabase       Gemini AI
 Database     Storage        Engine
     |
 Authentication
 Query History
 Dashboards

```

---

# 🛠️ Tech Stack

## Backend

| Technology | Purpose |
|---|---|
| FastAPI | REST API Framework |
| Python | Backend Development |
| SQLAlchemy Async | Database ORM |
| PostgreSQL | Persistent Storage |
| Pandas | Data Processing |
| Gemini API | AI Analytics |
| Supabase Storage | CSV File Storage |

---

## Frontend

| Technology | Purpose |
|---|---|
| React 18 | UI Framework |
| TypeScript | Type Safety |
| Vite | Build Tool |
| Tailwind CSS | Styling |
| Radix UI | Components |
| Recharts | Data Visualization |
| React Router | Navigation |

---

# 📁 Project Structure

```
Luminous_BI/

├── backend/
│
│── app.py
│── config.py
│── database.py
│
├── routes/
│   ├── auth.py
│   ├── upload.py
│   ├── analyze.py
│   └── dashboard.py
│
├── services/
│   ├── ai_service.py
│   ├── analytics.py
│   └── storage.py
│
├── models/
│
└── frontend/

    ├── src/
    │
    ├── pages/
    ├── components/
    └── lib/

```

---

# 🔄 Application Workflow

```
1. User Authentication
        ↓
2. Upload CSV Dataset
        ↓
3. Dataset Schema Analysis
        ↓
4. Ask Business Question
        ↓
5. AI Processing
        ↓
6. Generate Insights + Charts
        ↓
7. Save Dashboard / History
        ↓
8. Decision Recommendations

```

---

# 🔐 Security

Implemented:

- Secure password hashing using PBKDF2-HMAC-SHA256
- Random session tokens
- SHA256 token storage
- User-scoped dataset access
- Environment-based secret management
- Protected API routes

---

# 🚀 Local Installation

## Requirements

- Python 3.11+
- Node.js 18+
- PostgreSQL
- npm
- uv package manager


## Backend Setup

```bash
cd backend

uv venv --python 3.11

uv sync
```

Run backend:

```bash
uv run uvicorn app:app --config uvicorn.toml
```

Backend:

```
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://127.0.0.1:5173
```

---

# ⚙️ Environment Variables

Create:

```
backend/.env
```

Example:

```env
DATABASE_URL=your_postgres_url

SUPABASE_URL=your_supabase_url

SUPABASE_SERVICE_KEY=your_key

GEMINI_API_KEY=your_api_key

GEMINI_MODEL=gemini-2.5-flash

LLM_PRIMARY_PROVIDER=gemini

LLM_FALLBACK_PROVIDER=openrouter
```

---

# 🌐 API Endpoints

## Authentication

```
POST /auth/signup
POST /auth/signin
POST /auth/logout
GET  /auth/me
```

---

## Dataset

```
POST /upload
GET  /upload
```

---

## Analytics

```
POST /analyze

POST /decision-copilot

POST /what-if
```

---

## Dashboard

```
POST /dashboard

GET /dashboard

DELETE /dashboard/{id}
```

---

# 📈 Future Improvements

- Real-time streaming analytics
- More visualization types
- Multi-file dataset joins
- Advanced ML forecasting
- Role-based enterprise access
- Automated report generation

---

# 👨‍💻 Author

**Shayari TD**

Software Developer | AI & Full Stack Engineer

---

⭐ If you find this project useful, consider starring the repository!
