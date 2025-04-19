# backend/src/router.py
from fastapi import APIRouter, Request
from pydantic import BaseModel
from src.contacts.scraper import LinkedInGoogleScraper  # 你剛剛完成的 Scraper！

router = APIRouter()

# defind the data passed from front end
class MarketsAnalyzer(BaseModel):
    role: str

@router.get("/analyze-marketing")
async def keyword_analyzing(req: MarketsAnalyzer):
    print(f"KeyWord analyzing in src.markets")

    # return the data to front end
    return [
        {
            "keywords": [],
            "role": "Role that requested"
        }
    ]
