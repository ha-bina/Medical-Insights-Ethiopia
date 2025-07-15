# Ethiopian Medical Business Data Pipeline

## Data Flow Architecture
Medical insights eth6iopia
├── data/               # Data storage
├── docs/               # Documentation
├── src/
│   ├── scraping/       # Telegram collectors
│   ├── nlp/           # Text processing
│   ├── database/      # Data persistence
│   └── analytics/     # Insight generation
├── tests/             # Test cases
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
# Extract: Scrape Telegram channels

# Transform: Clean and translate content

Load: Store in PostgreSQL

# Analyze: Generate insights and visualizations

# Adding New Channels
Register the channel in src/scraping/channel_registry.py

# Add test cases in tests/scraping/test_channels.py

The system will automatically include it in the next scrape

# Common Issues:

Telegram API Limits:

Implemented automatic retry with exponential backoff

Check scraping.log for details

Amharic Text Encoding:

# Ensure proper handling:
text.encode('utf-8').decode('utf-8')
Database Connection Issues:

Verify PostgreSQL is running: docker-compose ps

Check logs: docker-compose logs db
