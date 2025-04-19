# backend/src/router.py
from fastapi import APIRouter, Request

from src.contacts.router import router as contacts_router
from src.markets.router import router as markets_router


router = APIRouter()

router.include_router(contacts_router, prefix="/contacts")
router.include_router(markets_router, prefix="/markets")