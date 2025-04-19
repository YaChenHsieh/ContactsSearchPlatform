from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from src.router import router

# Create the FastAPI app instance
app = FastAPI(
    title="Job Hunting Services API",
    description="API for searching LinkedIn connections and Techniques required in field",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow who can requst for the API -> allow_origins=["http://localhost:3000"],
    allow_credentials=True, # allow to bring credential or cookie
    allow_methods=["*"], # allow HTTP methods（GET, POST, DELETE, PUT)
    allow_headers=["*"], # allow all headers  -> Content-Type: application/json
)


app.include_router(router)

# decorater API 
@app.get("/")
def root():
    return "Running backend"

@app.get("/company/{company_name}") #  api  (get方法)
def search_connection(company_name: str, school: Optional[str] = None):
    return {"company": company_name, "alumni": school}
