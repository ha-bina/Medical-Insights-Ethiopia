import os
import json
import logging
from datetime import datetime
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhotophoto
from .storage_manager import write_to_datalake
from .channel_registry import CHANNEL_REGISTRY

class TelegramScraper:
    def __init__(self, session_name='ethio_medical'):
        self.client = TelegramClient(
            session_name,
            int(os.getenv('TELEGRAM_API_ID')),
            os.getenv('TELEGRAM_API_HASH')
        )
        self.logger = logging.getLogger('telegram_scraper')
        
    async def scrape_channel(self, channel_name, limit=1000):
        """Scrape messages from a Telegram channel"""
        try:
            self.logger.info(f"Starting scrape for {channel_name}")
            entity = await self.client.get_entity(channel_name)
            messages = []
            
            async for message in self.client.iter_messages(entity, limit=limit):
                message_data = {
                    'id': message.id,
                    'date': message.date.isoformat(),
                    'text': message.text,
                    'views': message.views,
                    'media': self._process_media(message.media),
                    'channel': channel_name
                }
                messages.append(message_data)
                
                # Download images if present
                if isinstance(message.media, MessageMediaPhoto):
                    await self._download_media(message, channel_name)
            
            # Store messages
            date_str = datetime.now().strftime('%Y-%m-%d')
            write_to_datalake(
                data=messages,
                data_type='messages',
                channel=channel_name,
                date=date_str
            )
            
            self.logger.info(f"Completed scrape for {channel_name}. {len(messages)} messages collected")
            return True
            
        except Exception as e:
            self.logger.error(f"Error scraping {channel_name}: {str(e)}")
            return False
    
    def _process_media(self, media):
        """Extract media information"""
        if not media:
            return None
        return {
            'type': str(media.__class__.__name__),
            'size': getattr(media, 'size', None)
        }
    
    async def _download_media(self, message, channel_name):
        """Download media files"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        output_dir = os.path.join(
            'data', 'raw', 'telegram', 'images', 
            date_str, channel_name
        )
        os.makedirs(output_dir, exist_ok=True)
        
        await message.download_media(file=os.path.join(
            output_dir, 
            f'media_{message.id}.jpg'
        ))