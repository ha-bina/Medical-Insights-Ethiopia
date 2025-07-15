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