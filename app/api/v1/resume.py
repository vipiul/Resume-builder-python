from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from app.services.pdf_service import generate_pdf
# from app.core.security import verify_token
from typing import Annotated
from playwright.async_api import async_playwright
import asyncio

router = APIRouter()

@router.post("/generate-resume")
def generate_resume(payload: dict):
    pdf_file = generate_pdf("resume.html", payload)
    return FileResponse(pdf_file, filename="resume.pdf", media_type="application/pdf")

@router.get("/job-list")
async def scrape_apna_jobs():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto("https://google.com", timeout=60000)
        title = await page.title()

        await browser.close()
        return {"title": title}
