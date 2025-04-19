# backend/src/router.py
from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Optional

# import API services
from src.contacts.scraper import LinkedInGoogleScraper
from src.contacts.service import LinkedInSearchQueryBuilder


router = APIRouter()

# Response model - JobContacts
class JobContactsRequest(BaseModel):
    
    # data from frontend
    company: str
    position: str
    role_type: str
    location: Optional[str] = None

@router.post("/hunters")
# async def search_hunters(req: JobContactsRequest):
def search_hunters(req: JobContactsRequest):
    print(f"[Hunters]")

    searcher = LinkedInSearchQueryBuilder(
        company = req.company,
        position = req.position,
        location = req.location,
        role_type = req.role_type # role_type for hunter's position
    )

    # Search the link from google site search
    linkedin_results = searcher.search(limit = 5)
    qyery_line, limit = searcher.get_query_and_limit(limit=5) # get the queryline for google scraper

    # Scrape the name from the search using scraper
    scraper = LinkedInGoogleScraper(headless=False)
    linkedin_name_results = scraper.extract_names_from_google(qyery_line, limit=5)

    # data return to frontend
    return [
        {   
            "company": req.company,
            "name": r['title'],  # get name from list item
            "url": r['url']
        }
        for r in linkedin_name_results # iterate the list [{company,name,url},{]}]
    ]


# Response model - Search Alumni
class AlumniContactsRequest(BaseModel):

    # data from frontend
    company: str
    position: str
    location: Optional[str] = None
    school: str


@router.post("/alumni")
# async def search_alumni(req: AlumniContactsRequest):
def search_alumni(req: AlumniContactsRequest):
    print(f"[Alumni]")

    searcher = LinkedInSearchQueryBuilder(

        company = req.company,
        position = req.position,
        location = req.location,
        school= req.school # school for searching alumni
    )

    # Search the link from google site search
    linkedin_results = searcher.search(limit = 5)
    qyery_line, limit = searcher.get_query_and_limit(limit=5) # get the queryline for google scraper

    # Scrape the name from the search using scraper
    scraper = LinkedInGoogleScraper(headless=False)
    linkedin_name_results = scraper.extract_names_from_google(qyery_line, limit=5)

    # data return to frontend
    return [
        {   
            "company": req.company,
            "name": r['title'].split(" - ")[0],  # get name only
            "url": r['url']
        }
        for r in linkedin_name_results
    ]
