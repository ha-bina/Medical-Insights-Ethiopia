from pydantic import BaseModel
from typing import List, Optional

class ProductReport(BaseModel):
    product: str
    count: int

class ChannelActivity(BaseModel):
    channel_name: str
    message_count: int
    first_post: str
    last_post: str

class SearchResult(BaseModel):
    message_id: str
    content: str
    channel_name: str
    timestamp: str

