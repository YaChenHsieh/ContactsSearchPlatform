# 🧠 Backend Architecture Overview – ConnectionSearchPlatform

This backend is built using **FastAPI** and integrates multiple services including LinkedIn contact scraping, alumni discovery, and market-driven job analysis. The server is designed with modularity in mind, separating logic across feature-based folders.

---

## 🚀 How to Run

Start the FastAPI server:

```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

API Documentation (Swagger UI):  
👉 http://127.0.0.1:8000/docs#

---

## 📁 Project Structure

```
backend/
│
├── main.py                 # App entry point, sets up FastAPI, middleware, and loads all routers
│
├── src/                    # Main application logic
│   ├── router.py           # Root router that includes feature-specific routers (e.g., contacts, markets)
│   │
│   ├── contacts/           # 👤 Handles LinkedIn search functionalities (hunters & alumni)
│   │   ├── router.py       # API endpoints for /hunters and /alumni
│   │   ├── service.py      # Builds Google search queries (site:linkedin.com...) based on user input
│   │   └── scraper.py      # Uses Playwright to extract name + LinkedIn URL from Google search result pages
│   │
│   └── markets/            # 📊 Extracts key job market skills from job descriptions
│       ├── router.py       # API endpoints for market/tech trend analysis (e.g., /market/trends)
│       └── service.py      # Processes job descriptions via ETL pipeline and extracts key skills using OpenAI API
```

---

## 🔄 File Descriptions

### 🧩 `main.py`
- Initializes the **FastAPI** app.
- Adds **CORS middleware** to allow frontend requests.
- Mounts all routers using `app.include_router()`.
- Entry point when launching the backend server.

---

### 📍 `src/router.py`
- The **central router** that includes all feature-specific routers like:
  - `contacts.router` → LinkedIn searching APIs
  - `markets.router` → Market/JD analysis APIs

---

### 👥 `contacts/` module

#### 🔹 `router.py`
- API endpoints:
  - `POST /contacts/hunters`: Find recruiters, PMs, CEOs, HR from LinkedIn using Google Search.
  - `POST /contacts/alumni`: Find alumni working at a specific company and school.
- Calls the `service` and `scraper` to complete full flow.

#### 🔹 `service.py`
- Builds a dynamic **Google search query** using `site:linkedin.com/in OR /pub` and user-provided keywords (company, job title, school, etc).
- Returns a clean query string and limit for scraping.

#### 🔹 `scraper.py`
- Uses **Playwright** (headless browser automation) to:
  - Load Google search result pages
  - Extract contact names from `<h3>` tags
  - Extract LinkedIn profile links from search results
- Supports `headless=True` mode for production automation.
- Can be upgraded with **stealth mode** to avoid Google CAPTCHA detection.

---

### 📊 `markets/` module

#### 🔹 `router.py`
- Future API endpoints (e.g., `POST /markets/skills`) for analyzing job description trends.

#### 🔹 `service.py`
- Handles:
  - **ETL flow** for cleaning and extracting skills from job description text.
  - Integrates **OpenAI API** to extract and summarize technical keywords (e.g., "React", "AWS", "SQL", etc.)
  - May be extended to analyze **industry demand** for different roles.

---

## 💡 Suggestions for Future Enhancements

- Add **API authentication** (e.g., API key or JWT).
- Add **unit tests** for query builders and scraping modules.
- Log scraping results to a database (e.g., MongoDB or DynamoDB).
- Add retry/fallback if Playwright gets blocked by CAPTCHA.
- Add a unified `utils/` folder for shared code (logging, formatting, etc).

