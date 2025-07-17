import asyncio
import logging
from dotenv import load_dotenv
from src.scraping.telegram_scraper import TelegramScraper
from src.scraping.channel_registry import CHANNEL_REGISTRY

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraping.log'),
        logging.StreamHandler()
    ]
)

async def main():
    load_dotenv()
    scraper = TelegramScraper()
    
    async with scraper.client:
        for channel in CHANNEL_REGISTRY.values():
            await scraper.scrape_channel(channel)

if __name__ == '__main__':
    asyncio.run(main())
from fastapi import FastAPI
from typing import List
from schemas import ProductReport, ChannelActivity, SearchResult
import crud

app = FastAPI(title="Telegram Analytics API")

@app.get("/api/reports/top-products", response_model=List[ProductReport])
def top_products(limit: int = 10):
    return crud.get_top_products(limit)

@app.get("/api/channels/{channel_name}/activity", response_model=ChannelActivity)
def channel_activity(channel_name: str):
    return crud.get_channel_activity(channel_name)

@app.get("/api/search/messages", response_model=List[SearchResult])
def search_messages(query: str):
    return crud.search_messages(query)
